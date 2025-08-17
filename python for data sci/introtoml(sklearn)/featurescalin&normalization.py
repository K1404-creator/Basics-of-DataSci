# Use MinMaxScaler for neural networks or when you need a specific range.
# Use StandardScaler for most ML algorithms if your data is roughly normal.
# Use RobustScaler if your data has many outliers.

import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, RobustScaler, StandardScaler

data = np.array([[100,200], [150,300], [200,400]])


scaler = MinMaxScaler()
scaled_Data = scaler.fit_transform(data)

print(scaled_Data)

print("----------------------------------------------")
# standardization
scale = StandardScaler()
standardized_data = scale.fit_transform(data)
print(standardized_data)


# robust scaling
robust_scaler = RobustScaler()
robust_scaled_data = robust_scaler.fit_transform(data)
print(robust_scaled_data)






#Here’s a detailed, easy explanation of each scaling method in your code, with simple examples:

# ---

# ### 1. MinMaxScaler

# **What it does:**  
# Scales each feature (column) to a given range, usually [0, 1].  
# Formula:  
# ```
# X_scaled = (X - X_min) / (X_max - X_min)
# ```

# **Example:**  
# Suppose you have values: [10, 20, 30]  
# - Min = 10, Max = 30  
# - Scaled:  
#   - (10-10)/(30-10) = 0  
#   - (20-10)/(30-10) = 0.5  
#   - (30-10)/(30-10) = 1

# **In your code:**  
# Each column in `data` is scaled so the smallest value becomes 0 and the largest becomes 1.

# ---

# ### 2. StandardScaler

# **What it does:**  
# Standardizes features by removing the mean and scaling to unit variance.  
# Formula:  
# ```
# X_standardized = (X - mean) / std
# ```
# Result: Each column has mean 0 and standard deviation 1.

# **Example:**  
# Suppose you have values: [1, 2, 3]  
# - Mean = 2, Std = 1  
# - Standardized:  
#   - (1-2)/1 = -1  
#   - (2-2)/1 = 0  
#   - (3-2)/1 = 1

# **In your code:**  
# Each column in `data` is transformed so it has mean 0 and standard deviation 1.

# ---

# ### 3. RobustScaler

# **What it does:**  
# Scales features using statistics that are robust to outliers: the median and the interquartile range (IQR).  
# Formula:  
# ```
# X_robust = (X - median) / IQR
# ```
# - IQR = 75th percentile - 25th percentile

# **Example:**  
# Suppose you have values: [1, 2, 100]  
# - Median = 2, IQR = 100 - 1 = 99  
# - Robust scaled:  
#   - (1-2)/99 ≈ -0.01  
#   - (2-2)/99 = 0  
#   - (100-2)/99 ≈ 0.99

# **In your code:**  
# Each column in `data` is scaled using the median and IQR, making it less sensitive to extreme values.

# ---

# **Summary Table:**

# | Method           | Sensitive to Outliers? | Range/Mean/Std after scaling |
# |------------------|-----------------------|-----------------------------|
# | MinMaxScaler     | Yes                   | [0, 1]                      |
# | StandardScaler   | Yes                   | Mean 0, Std 1               |
# | RobustScaler     | No                    | Median 0, IQR 1             |

# Let me know if you want to see the output for your specific data or need more examples