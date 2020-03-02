import pandas as pd

test_df = pd.read_csv('test.csv', sep=';')

# get overall score values from first class
print(test_df.loc[(test_df['class_id'] == 1) & (test_df['overall_score'].notnull())]['overall_score'])

# calculate mean 'manually'
expected_value = pd.Series([(16.0 + 17.0) / 2.0])
expected_value.rename('avg_class_test_overall_score', inplace=True)

# get calculated value
df = pd.read_csv('test_average_scores.csv', sep=';')
actual_value = df.loc[df['class_id'] == 1]['avg_class_test_overall_score']

# test
pd.testing.assert_series_equal(expected_value, actual_value)
