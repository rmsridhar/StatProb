import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import normaltest
from scipy.stats import shapiro
#h = [6.84,6.04,7.77,6.77,7.85,8.2,9.12,7.79,10.7,10.1,13.3,5.44]
#data=pd.read_csv("EDS Branch.csv")
#h=data['Value']
data=pd.read_csv("winequality-red.csv")
h=data['pH']

print(h)
hmean = np.mean(h)
print(hmean)
hstd = np.std(h)
print(hstd)
pdf = stats.norm.pdf(h, hmean, hstd)
plt.plot(h, pdf,linewidth=3, color='y') # including h here is crucial
plt.show()

# Create the bins and histogram
count, bins, ignored = plt.hist(h, len(h), density=True)

# Plot the distribution curve
plt.plot(bins, 1/(hstd * np.sqrt(2 * np.pi)) *
   np.exp( - (bins - hmean)**2 / (2 * hstd**2)),linewidth=3, color='y')
plt.show()
plt.plot(h, 1/(hstd * np.sqrt(2 * np.pi)) *
   np.exp( - (h - hmean)**2 / (2 * hstd**2)),linewidth=3, color='y')
plt.show()
skewness1=stats.skew(h)
print("skewness=",skewness1)
kurtosis1=stats.kurtosis(h)
print("Kurtosis=",kurtosis1)
stat, p = normaltest(h)
print('Statistics=%.3f, p=%.3f' % (stat, p))
# interpret
alpha = 0.05
if p > alpha:
    print('Sample looks Gaussian (fail to reject H0)')
else:
    print('Sample does not look Gaussian (reject H0)')
