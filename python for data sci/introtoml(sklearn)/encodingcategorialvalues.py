import pandas as pd
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder

data = ['Low', 'Medium', 'High', 'Medium', 'Low']

encoder = LabelEncoder()
encoded_data = encoder.fit_transform(data)
print("Encoded Data:", encoded_data)


print("----------------------------------------------")


# For ordinal encoding, where the order matters
df  = pd.DataFrame({
    'Quality': ['Low', 'Medium', 'High', 'Medium', 'Low']
})


ordinal_encoder = OrdinalEncoder(categories=[['Low', 'Medium', 'High']])
ordinal_encoded_data = ordinal_encoder.fit_transform(df)
print("Ordinal Encoded Data:\n", ordinal_encoded_data)

print("----------------------------------------------")

# For one-hot encoding, where the order does not matter


df1 = pd.DataFrame({'Color': ['Red', 'Blue', 'Green', 'Blue', 'Red']})

one_hot_encoded_Data = pd.get_dummies(df1, columns=['Color'])
print("One-Hot Encoded Data:\n", one_hot_encoded_Data)