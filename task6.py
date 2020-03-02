import pandas as pd
import sqlite3
from datetime import datetime

# read data
test_average_scores_df = pd.read_csv('test_average_scores.csv', sep=';')
test_utilization_df = pd.read_csv('test_utilization.csv', sep=';')

# convert timestamp format to YY-MM-DD HH:MM
given_timestamp_format = '%d.%m.%y %H:%M'
correct_timestamp_format = '%Y-%m-%d %H:%M'
new_dates_created_at = list()
new_dates_authorized_at = list()
for row in range(test_utilization_df.shape[0]):
    date = test_utilization_df['test_created_at'][row]
    datetime_object = datetime.strptime(date, given_timestamp_format)
    new_dates_created_at.append(datetime.strftime(datetime_object, correct_timestamp_format))
    date = test_utilization_df['test_authorized_at'][row]
    datetime_object = datetime.strptime(date, given_timestamp_format)
    new_dates_authorized_at.append(datetime.strftime(datetime_object, correct_timestamp_format))

# replace timestamps 
test_utilization_df['test_created_at'] = new_dates_created_at
test_utilization_df['test_authorized_at'] = new_dates_authorized_at

 # connect to database and crate cursor
conn = sqlite3.connect('tests.db')
c = conn.cursor()

# creating sql tables accoridingly to data in dataframes 
create_test_average_scores_table = '''
    CREATE TABLE IF NOT EXISTS TEST_AVERAGE_SCORES
    (
        class_id INTEGER,
        class_name TEXT,
        teaching_hours TEXT,
        avg_class_test_overall_score REAL
    )
'''
create_test_utilization_table = '''
    CREATE TABLE IF NOT EXISTS TEST_UTILIZATION
    (
        class_id INTEGER,
        class_name TEXT,
        teaching_hours TEXT,
        test_id INTEGER,
        test_level INTEGER,
        test_created_at TEXT,
        test_authorized_at TEXT,
        class_test_number INTEGER
    )
'''
c.execute(create_test_average_scores_table)
c.execute(create_test_utilization_table)
conn.commit()

# inserting dataframes data to newly created sql tables
test_average_scores_df.to_sql(
    name='TEST_AVERAGE_SCORES',
    con=conn,
    if_exists='replace',
    index=False
    )

test_utilization_df.to_sql(
    name='TEST_UTILIZATION',
    con=conn,
    if_exists='replace',
    index=False
    )

# printing data from database
cursor = c.execute('SELECT * FROM TEST_AVERAGE_SCORES')

print(tuple(map(lambda desc: desc[0], cursor.description))) # column names
for row in c.fetchmany(10):
    print(row)

cursor = c.execute('SELECT * FROM TEST_UTILIZATION')

print(tuple(map(lambda desc: desc[0], cursor.description))) # column names
for row in c.fetchmany(10):
    print(row)


conn.close()