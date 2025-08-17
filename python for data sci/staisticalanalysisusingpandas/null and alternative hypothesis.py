# method used to draw a conclusion about a population based on a sample.

import numpy as np
import pandas as pd
from scipy import stats
from scipy.stats import chi2_contingency

# Null Hypothesis: The observed frequencies are equal to the expected frequencies.
# Alternative Hypothesis: The observed frequencies are not equal to the expected frequencies.


group1  = [20,34,45,23,12]
group2  = [30,25,40,20,15]

t_stat, p_value = stats.ttest_ind(group1, group2)

print("T-statistic:", t_stat)
print("P-value:", p_value)

print("----------------------------------------------")


data = pd.DataFrame({
    'Group1': [20,30],
    'Group2': [25,35]
}, index=['Category1', 'Category2'])


chi2_stat,p_value, _, _, = chi2_contingency(data) # to determine if therer is  a significant relationship between two categorical variables.

print("Chi-squared Statistic:", chi2_stat)
print("P-value:", p_value)