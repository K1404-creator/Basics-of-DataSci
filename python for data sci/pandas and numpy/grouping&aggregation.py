import pandas as pd

data = {'çategory': ['electronics','clothing','electronics','clothing','groceries'],
        'sales': [200, 150, 300, 100, 250]}


df = pd.DataFrame(data)

group_df = df.groupby('çategory').sum()
print(group_df)

print('-------------------------------')
#aggregation


def sales_range(x):
    return x.max() - x.min()

grouped_df = df.groupby('çategory').agg({'sales':  sales_range})


print(grouped_df)