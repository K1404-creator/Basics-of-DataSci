# CALCULATING CENTRAL TENDNENCY :  MEAN, MEDIAN, MODE

import pandas as pd

data = {'Scores': [45,56,45,46,65,34,64]}

data_with_mode = {'Scores': [45, 56, 45, 46, 65, 34, 64, 45] }

df_with_mode = pd.DataFrame(data_with_mode)
df = pd.DataFrame(data)

mean_score = df['Scores'].mean()
mean_score = round(mean_score, 2)

median_score = df['Scores'].median()
mode_score = df_with_mode['Scores'].mode()

print(f"Mean Score: {mean_score}")

print(f"Median Score: {median_score}")

print(f"Mode: {mode_score[0]}")



