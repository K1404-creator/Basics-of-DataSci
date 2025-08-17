import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom, poisson

lamda_pram = 5

x = np.arange(0, 20)
probabilities = poisson.pmf(x, lamda_pram)
plt.bar(x, probabilities, color='blue') 
plt.title('Poisson Distribution')
plt.xlabel('Number of events')
plt.ylabel('Probability')
plt.show()