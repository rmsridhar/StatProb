import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
#from scipy.stats import normaltest
#from scipy.stats import shapiro
h = [186, 176, 158, 180, 186, 168, 168, 164, 178, 170, 189, 195, 172,
     187, 180, 186, 185, 168, 179, 178, 183, 179, 170, 175, 186, 159,
     161, 178, 175, 185, 175, 162, 173, 172, 177, 175, 172, 177, 180]
h.sort()
hmean = np.mean(h)
print(hmean)
hstd = np.std(h)
print(hstd)
pdf = stats.norm.pdf(h, hmean, hstd)
plt.plot(h, pdf,linewidth=3, color='y') # including h here is crucial
plt.show()

plt.plot(h, 1/(hstd * np.sqrt(2 * np.pi)) *
   np.exp( - (h - hmean)**2 / (2 * hstd**2)),linewidth=3, color='r')
plt.show()
# Create the bins and histogram
#count, bins, ignored = plt.hist(h, 39, density=True)

# Plot the distribution curve
#plt.plot(bins, 1/(hstd * np.sqrt(2 * np.pi)) *
#   np.exp( - (bins - hmean)**2 / (2 * hstd**2)),linewidth=3, color='y')
#plt.show()


#If skewness is less than -1 or greater than 1,
#the distribution is highly skewed.
#If skewness is between -1 and -0.5 or between 0.5 and 1,
#the distribution is moderately skewed.
#If skewness is between -0.5 and 0.5, the distribution is approximately symmetric.
skewness1=stats.skew(h)
print("skewness=",skewness1)
#The values for asymmetry and kurtosis between -2 and +2
#are considered acceptable in order to prove normal univariate distribution
kurtosis1=stats.kurtosis(h)
print("Kurtosis=",kurtosis1)
#Test whether a sample differs from a normal distribution.
#This function tests the null hypothesis that a sample comes from a normal distribution.
#It is based on D’Agostino and Pearson’s test that combines skew and kurtosis
#to produce an omnibus test of normality.
#stat, p = normaltest(h)
#print('Statistics=%.3f, p=%.3f' % (stat, p))
# interpret
#alpha = 0.05
#if p > alpha:
#    print('Sample looks Gaussian (fail to reject H0)')
#else:
#    print('Sample does not look Gaussian (reject H0)')
#
