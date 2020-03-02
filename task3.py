import pandas as pd

# read data
class_df = pd.read_csv('corrected-files/class.csv', sep=';')
test_df = pd.read_csv('corrected-files/test.csv', sep=';')

# keep necessary columns only
class_df = class_df[['id', 'name', 'teaching_hours']]
test_df = test_df[['id', 'created_at', 'authorized_at', 'test_level_id', 'class_id']]

# keep authorized tests only
test_df = test_df.loc[test_df['authorized_at'].notnull()]

# merge test and class dataframes
merged_df = pd.merge(
    left=class_df,
    right=test_df,
    how='inner',
    left_on='id',
    right_on='class_id',
    suffixes=('_class', '_test')
)
merged_df.drop(merged_df.columns[-1], inplace=True, axis=1) # drop redundant class id

# reorder columns
correct_order = ['id_class', 'name', 'teaching_hours', 'id_test', 'test_level_id', 'created_at', 'authorized_at']
merged_df = merged_df[correct_order]

# rename columns
rename_dict = {
   'id_class': 'class_id',
   'name': 'class_name',
   'id_test': 'test_id',
   'test_level_id': 'test_level',
   'created_at': 'test_created_at',
   'authorized_at': 'test_authorized_at'
}
merged_df.rename(columns=rename_dict, inplace=True)

# add last column -> cumulative count (+1 since we count inclusively), grouped by class id
merged_df['class_test_number'] = merged_df.groupby('class_id').cumcount() + 1

#save
merged_df.to_csv('test_utilization.csv', sep=';', index=False)
