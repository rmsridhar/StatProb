import numpy as np
from scipy.stats import gamma
from matplotlib import pyplot as plt
x = np.linspace(1E-6, 10, 100)
print(x)
c=0.0
for k in range(1,10):
    c=c+0.1
    dist = gamma(c, 0, 1)
    plt.plot(x, dist.pdf(x),label="c", linewidth=3, color='y')
plt.xlim(0, 1)
plt.ylim(0, 0.45)
plt.show()
