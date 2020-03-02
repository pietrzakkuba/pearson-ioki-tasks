import pandas as pd

df = pd.read_csv('received-files/test.csv', sep=';')


# check if each row has all compulsory values not null
not_null_columns = ['id', 'student_id', 'class_id', 'created_at', 'updated_at', 'institution_id', 'test_level_id', 'licence_id']
for index, row in df.iterrows():
    if row[not_null_columns].isnull().values.any():
        df.drop(index, inplace=True)

# delete rows where test_status is scoring_scored but overall score value is null 
for index, row in df.loc[df['test_status'] == 'SCORING_SCORED'].iterrows():
    if row[['overall_score']].isnull().values.all():
        df.drop(index, inplace=True)

# save filtered data
df.to_csv('corrected-files/test.csv', sep=';', index=False)

