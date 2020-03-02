import pandas as pd

df = pd.read_csv('class_original.csv', sep=';')

# check if each row has all compulsory values not null
not_null_columns = ['id', 'institution_id', 'owner_id', 'name', 'created_at', 'updated_at', 'teaching_hours', 'has_student_with_scored_test'] # all but latest_test_time
for index, row in df.iterrows():
    values = row[not_null_columns]
    if values.isnull().values.any():
        df.drop(index, inplace=True)

# save filtered data
df.to_csv('class.csv', sep=';', index=False)