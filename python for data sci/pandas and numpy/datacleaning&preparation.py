import numpy as np
import pandas as pd

#MISSING DATA

data = {'Name': ['Alice', 'Bob', 'Charlie','Jenny'],
        'Age': [25, np.nan, 35, np.nan],
        'City': ['New York', 'Los Angeles',np.nan, 'Chicago']}


df = pd.DataFrame(data)
print(df)

print(" -------------------")

df_filled = df.fillna({'Age': df['Age'].mean(),'City': 'Unknown'})

print(df_filled)

print(" -------------------")
#Removing duplicate entries

print(" ---------BEFORE REMOVING DUPLICATES----------")

data2 = {'Name': ['Alice', 'Bob', 'Charlie', 'Alice'],
        'Age': [25, 30, 35, 25],
        'City': ['New York', 'Los Angeles', 'Chicago', 'New York']}


df2 = pd.DataFrame(data2)
print(df2)
print(" ---------AFTER REMOVING DUPLICATES----------")
df2_dup = df2.drop_duplicates()
print(df2_dup)