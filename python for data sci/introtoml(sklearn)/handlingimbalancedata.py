from collections import Counter

import numpy as np
import pandas as pd
from imblearn.over_sampling import RandomOverSampler

#ovrersampling

X = np.array([[1, 2], [2, 3], [3, 4], [4,5], [5, 6]])


y = np.array([0, 0, 0, 0, 1])  # Imbalanced target variable


ros = RandomOverSampler(random_state=42)
X_resampled, y_resampled = ros.fit_resample(X, y)
print(f"Resampled Y: {Counter(y_resampled)}")