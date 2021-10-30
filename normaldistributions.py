import matplotlib.pyplot as plt
import numpy as np
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

#mu, sigma = 0.5, 0.1
mu, sigma = -2, 2
#mu,sigma=2,0.5
s = np.random.normal(mu, sigma, 100)
print(s)
# Create the bins and histogram
count, bins, ignored = plt.hist(s, 20, density=True)

# Plot the distribution curve
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
    np.exp( - (bins - mu)**2 / (2 * sigma**2)),linewidth=3, color='y')
plt.show()
skewness1=stats.skew(bins)
print("skewness=",skewness1)
kurtosis1=stats.kurtosis(bins)
print("Kurtosis=",kurtosis1)

mu,sigma=2,0.5
s = np.random.normal(mu, sigma, 100)
print(s)
# Create the bins and histogram
count, bins, ignored = plt.hist(s, 20, density=True)

# Plot the distribution curve
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
    np.exp( - (bins - mu)**2 / (2 * sigma**2)),linewidth=3, color='y')
plt.show()
skewness1=stats.skew(bins)
print("skewness=",skewness1)
kurtosis1=stats.kurtosis(bins)
print("Kurtosis=",kurtosis1)
mu,sigma=0,1
s = np.random.normal(mu, sigma, 100)
print(s)
# Create the bins and histogram
count, bins, ignored = plt.hist(s, 20, density=True)

# Plot the distribution curve
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
    np.exp( - (bins - mu)**2 / (2 * sigma**2)),linewidth=3, color='y')
plt.show()
skewness1=stats.skew(bins)
print("skewness=",skewness1)
kurtosis1=stats.kurtosis(bins)
print("Kurtosis=",kurtosis1)
