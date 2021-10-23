# Write a program to carry out the following experiment.
# A coin is tossed 100 times and the number of heads that turn up is recorded.
# This experiment is then repeated 1000 times.
# Have your program plot a bar graph for the proportion of the
# 1000 experiments in which the number of heads is n,
# for each n in the interval [35,65].
# Does the bar graph look as though it can be ﬁt with a normal curve?
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
from scipy.stats import normaltest
from scipy.stats import shapiro
import random
head=0
tail=0
h=[]
for j in range(1000):
    head=0;tail=0
    for i in range(100):
         t=random.choice([0,1])
         if t==0:
              head=head+1
         else:
              tail=tail+1
    print("Number of heads for 1000",head)
    h.append(j)
  #  if (head>=35) and (head<=65):
  #      h[j]=head
h.sort()
print("number of heads of 100 for 1000 times",h)
hmean = np.mean(h)
print(hmean)
hstd = np.std(h)
print(hstd)
pdf = stats.norm.pdf(h, hmean, hstd)
plt.plot(h, pdf,linewidth=3, color='y') # including h here is crucial
plt.show()

# Create the bins and histogram
count, bins, ignored = plt.hist(h, 100, density=True)
# Plot the distribution curve
plt.plot(bins, 1/(hstd * np.sqrt(2 * np.pi)) *
   np.exp( - (bins - hmean)**2 / (2 * hstd**2)),linewidth=3, color='y')
plt.show()
m=0
h1=[]
for i in range(len(h)):
    if (h[i]>35) and (h[i]<=65):
        h1.append(m)
        h1[m]=h[i]
        m=m+1
print("h1=",h1)
print("m=",m)
count, bins, ignored = plt.hist(h1, m, density=True)
h1mean = np.mean(h1)
print(h1mean)
h1std = np.std(h1)
print(h1std)




# Plot the distribution curve
plt.plot(bins, 1/(h1std * np.sqrt(2 * np.pi)) *
   np.exp( - (bins - h1mean)**2 / (2 * h1std**2)),linewidth=3, color='y')
plt.show()
#plt.plot(h, 1/(hstd * np.sqrt(2 * np.pi)) *
#   np.exp( - (h - hmean)**2 / (2 * hstd**2)),linewidth=3, color='y')
#plt.show()

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


