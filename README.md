# pearson-ioki-tasks

### 1. Requirements:
Python 3 and pandas. <br>
I were using Python 3.8.2 32-bit and pandas 1.0.1 <br>
### 2. Files and folders naming:
a) received files are stored in received-files folder<br>
b) corrected files (Task 2) are stored in corrected-files folder<br>
c) scripts for tasks 2-6 are named accordingly to a task number (task#)<br>
d) task2 is divided into 2 scripts (correcting data for each csv file separately -> suffixes _class and _test)<br>
e) unit tests for Task 3 and Task 4 are in files suffixed with _unittest<br>
f) database (SQLite3) created in Task 6 is named tests.db<br>
g) final datasets are named test_utilization.csv and test_average_scores.csv<br>
### 3. Task 4 columns' problem:
I skipped test_created_at and test_authorized_at columns in test_average_scores, because values in these columns refer to only one test each row, not a group of tests of one class, thus their presence and meaning seemed unclear to me <br>
