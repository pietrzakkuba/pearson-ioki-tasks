import pandas as pd

df = pd.read_csv('test_utilization.csv', sep=';')

df.drop(df.columns[-1], inplace=True, axis=1) # drop calculated row class_test_number

df = df.head(10) # trim data

print(df) # print data to calculate expected results 'manually'

expected_results = pd.Series([1, 2, 3, 1, 2, 1, 1, 2, 3, 4])

actual_results = df.groupby('class_id').cumcount() + 1

# test
pd.testing.assert_series_equal(expected_results, actual_results)