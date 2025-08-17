import pandas as pd

data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [24, 30, 22, 29],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston'],
        'score': [85, 90, 78, 88]}
        
        
df = pd.DataFrame(data)

# sorted_df = df.sort_values(by='Age', ascending=True)
sorted_multi_df = df.sort_values(by =['score', 'Age'], ascending=[False, True])
print(sorted_multi_df)



#filtering

filtered_df = df[df['score']>85]
print("\nFiltered DataFrame (score > 85):\n", filtered_df)