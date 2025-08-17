import pandas as pd

data = {'Scores': [60, 70, 80, 90, 100]}


df = pd.dataFrame(data)

range_value = df['Scores'].max() - df['Scores'].min()



print(range_value)


# variance : avg square deviation of each data point from the mean


variance_value = df['Scores'].var()

print(variance_value)

#higher variance means more variability in the data
#lower variance means less variability in the data(closer to the mean)


#Standard deviation : square root of variance

std_deviation_value = df['Scores'].std()
print(std_deviation_value)