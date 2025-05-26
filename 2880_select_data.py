'''
2880. Select Data

DataFrame students
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| student_id  | int    |
| name        | object |
| age         | int    |
+-------------+--------+

Write a solution to select the name and age of the student with student_id = 101.
'''

import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    result_101 = students[students["student_id"]==101]
    result = result_101[["name", "age"]]
    return result

