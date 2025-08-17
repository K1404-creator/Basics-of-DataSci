import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom, poisson

mean = 0


std_dev = 1


data = np.random.normal(mean,std_dev, 1000)


plt.hist(data,bins = 30, density = True, alpha= 0.6)


plt.title('Normal Distribution')
plt.xlabel('value')

plt.ylabel("Frequency")

plt.show()




