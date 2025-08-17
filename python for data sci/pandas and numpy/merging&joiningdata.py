# useful when we have te related data separated across the multiple level or dataset
#merging two dataframes using common column

import pandas as pd

df1 = pd.DataFrame({'ID': [1, 2, 3, 4],
                     'Name': ['Alice', 'Bob', 'Charlie', 'David']})

df2 = pd.DataFrame({'ID': [1,2,3,4],
                     'Salary': [70000, 80000, 90000, 100000]})



merged_df = pd.merge(df1,df2,on='ID')
print("Merged DataFrame:")
print(merged_df)

print("------------------")
      
      
#joining two dataframes


df3 = pd.DataFrame({'EmpID': [1, 2, 3, 4],
                     'Department': ['HR', 'Finance', 'IT', 'Marketing']})

df4 = pd.DataFrame({'ID': [1, 2, 3, 4],
                    'Grade': ['A', 'B', 'A', 'C']})


joined_df = pd.merge(df3,df4,left_on = 'EmpID',right_on= 'ID')
print("Joined DataFrame:\n",joined_df )


