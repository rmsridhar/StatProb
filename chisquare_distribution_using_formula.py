import numpy as np
import scipy.stats as stats
from scipy.stats import gamma
import matplotlib.pyplot as plt
import math
# Plot the theoretical density of f
x = np.arange(0, 300, .05)
df=3
y=[]
for i in range(len(x)):
    y.append(i)
    y[i]=(math.exp(-x[i]/2)*(pow(x[i],(df/2)-1)))/(pow(2,df/2)*math.gamma(df/2))
plt.plot(x,y,color='b',lw=3)
plt.show()

plt.plot(x, stats.chi2.pdf(x, df=1), color='g', lw=2)
plt.show()
plt.plot(x, stats.chi2.pdf(x, df=2), color='b', lw=2)
plt.show()
plt.plot(x, stats.chi2.pdf(x, df=3), color='r', lw=2)
plt.show()
plt.plot(x, stats.chi2.pdf(x, df=4), color='k', lw=2)
plt.show()
plt.plot(x, stats.chi2.pdf(x, df=5), color='m', lw=2)
plt.show()
plt.plot(x, stats.chi2.pdf(x, df=150), color='m', lw=2)
plt.show()
