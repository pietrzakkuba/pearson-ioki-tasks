import pandas as pd

# read data
class_df = pd.read_csv('corrected-files/class.csv', sep=';')
test_df = pd.read_csv('corrected-files/test.csv', sep=';')

# keep authorized and marked as scoring_scored tests only
test_df = test_df.loc[(test_df['test_status'] == 'SCORING_SCORED') & (test_df['authorized_at'].notnull())]

# keep necessary columns only
class_df = class_df[['id', 'name', 'teaching_hours']]
test_df = test_df[['created_at', 'authorized_at', 'overall_score', 'class_id']]

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

# rename columns
rename_dict = {
   'id': 'class_id',
   'name': 'class_name',
   'created_at': 'test_created_at',
   'authorized_at': 'test_authorized_at'
}
merged_df.rename(columns=rename_dict, inplace=True)

# create final DataFrame
# skipping test_created_at and test_authorized_at because they refer to only one test each row, not a group of tests we calculate mean for, thus they are unneeded
avg_scored_df = merged_df.groupby(['class_id', 'class_name', 'teaching_hours'])['overall_score'].mean().to_frame().reset_index()

# rename new column's name
avg_scored_df.rename(columns={'overall_score': 'avg_class_test_overall_score'}, inplace=True)

#save
avg_scored_df.to_csv('test_average_scores.csv', sep=';', index=False)
