import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
#mean=0
#h = [-186, 196, -168, 170, -186, 186, 168, -164, 194,-210]
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

# Create the bins and histogram
count, bins, ignored = plt.hist(h, 9, density=True)

# Plot the distribution curve
plt.plot(bins, 1/(hstd * np.sqrt(2 * np.pi)) *
    np.exp( - (bins - hmean)**2 / (2 * hstd**2)),linewidth=3, color='y')
plt.show()

