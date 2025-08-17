#series is a one-dimensional labeled array capable of holding any data type.
#series is veru useful for handling labeled data and performing operations such as filetring.
import pandas as pd

data = [10,20,30,40]

series = pd.Series(data, index= ['a', 'b', 'c', 'd'])
print(series)


#Data frames are two-dimensional labeled data structures with columns that can be of different types.
# Data frames are similar to SQL tables or Excel spreadsheets.

data1 = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']}


df = pd.DataFrame(data1)
print(df)