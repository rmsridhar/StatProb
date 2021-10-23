import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import random
import math
np.random.seed(10)
population_ages1 = stats.poisson.rvs(loc=18, mu=35, size=150000)
population_ages2 = stats.poisson.rvs(loc=18, mu=10, size=100000)
population_ages = np.concatenate((population_ages1, population_ages2))

print("Population Ages Mean",population_ages.mean())

# We use stats.norm.ppf(q = 0.975) to get the desired z-critical value instead of q = 0.95
#because the distribution has two tails.
#Notice that the confidence interval we calculated captures the true population mean
#of 43.0023.
#Let's create several confidence intervals and plot them to get a
#better sense of what it means to "capture" the true mean:

np.random.seed(12)

sample_size = 1000
p=0.25
n=10
sumx=0
a=[]
b=[]
for i in range(20):
   # x=random.random()
    x = np.random.choice(a= population_ages, size=500)
    a.append(x)
    sumx=sumx+x
    y=pow(p,x)*pow(1-p,n-x)
    b.append(y)
print(np.mean(b))
plt.plot(x,y,'o')
mid=sumx/20

plt.hlines(xmin=0, xmax=25,
           y=mid, 
           linewidth=2.0,
           color="red")
plt.show()

  
