import numpy as np
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, np.nan, 30, 22, np.nan],
    'Salary': [50000, 60000, np.nan, 45000,40000]
}


df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)


missing_data = df.isnull()
print("\nMissing Data:")
print(missing_data)


print("handling missing data")



print("------------------")


df_dropped  = df.dropna()
print("DataFrame after dropping rows with any missing values:\n", df_dropped)

