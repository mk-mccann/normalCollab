import numpy as np
import matplotlib.pyplot as plt

mean = 0
std = 3
samples = 100
dist = np.random.normal(mean, std, samples)

plt.hist(dist)
plt.savefig('norm_plot', format = '.pdf')
plt.show()