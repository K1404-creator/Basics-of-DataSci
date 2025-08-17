import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom, poisson

n = 10
p = 0.5

x = np.arange(0, n+1)
probabilities = binom.pmf(x, n, p)

plt.bar(x, probabilities, color = 'green')

plt.title('Binomial Distribution ')

plt.xlabel('Number of successes')
plt.ylabel('Probability')   
plt.show()