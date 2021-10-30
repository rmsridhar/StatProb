import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import random
import math
np.random.seed(10)
population_ages1 = stats.poisson.rvs(loc=18, mu=35, size=150000)
plt.show(pd.DataFrame(population_ages1).hist(bins=58,
                                  range=(17.5,75.5),
                                  figsize=(9,9)))

population_ages2 = stats.poisson.rvs(loc=18, mu=10, size=100000)
plt.show(pd.DataFrame(population_ages2).hist(bins=58,
                                  range=(17.5,75.5),
                                  figsize=(9,9)))

population_ages = np.concatenate((population_ages1, population_ages2))
plt.show(pd.DataFrame(population_ages).hist(bins=58,
                                  range=(17.5,75.5),
                                  figsize=(9,9)))



np.random.seed(6)
sample_ages = np.random.choice(a= population_ages,
                               size=500)            # Sample 500 values
plt.show(pd.DataFrame(sample_ages).hist(bins=58,
                                  range=(17.5,75.5),
                                  figsize=(9,9)))

print("Population Ages Mean",population_ages.mean())
print ("Sample mean", sample_ages.mean() )                         # Show sample mean

print("difference between means",population_ages.mean() - sample_ages.mean())   # Check difference between means


#The distribution has low skewness, but the plot reveals the data is clearly not normal:
#instead of one symmetric bell curve, it has as bimodal distribution with two high density peaks. 
#plt.show(pd.DataFrame(population_ages).hist(bins=58,
#                                  range=(17.5,75.5),
#                                  figsize=(9,9)))

print( stats.skew(population_ages))
#The sample we drew from this population should have roughly the same shape and skew:
#plt.show(pd.DataFrame(sample_ages).hist(bins=58,
#                                  range=(17.5,75.5),
#                                  figsize=(9,9)))
print( stats.skew(sample_ages))

 #let's create a sampling distribution by taking 200 samples from our population and
 #then making 200 point estimates of the mean:
np.random.seed(10)

point_estimates = []         # Make empty list to hold point estimates

for x in range(200):         # Generate 200 samples
    sample = np.random.choice(a= population_ages, size=500)
    point_estimates.append( sample.mean())
    
plt.show(pd.DataFrame(point_estimates).plot(kind="density",  # Plot sample mean density
                                   figsize=(9,9),
                                   xlim=(41,45)))   
print("Point Estimate Mean",np.array(point_estimates).mean())
print(population_ages.mean() - np.array(point_estimates).mean())

t=[]
for i in range(len(point_estimates)):
    t.append((population_ages.mean()-point_estimates[i]))
        
    print("i={0},Population Mean={1},sample mean={2}, difference={3}".format(i,population_ages.mean(),point_estimates[i],t[i]))
    
print(t.sort())

point_estimates = []         # Make empty list to hold point estimates

for x in range(200):         # Generate 1000 samples
    sample = np.random.choice(a= population_ages, size=1000)
    point_estimates.append( sample.mean())
    
plt.show(pd.DataFrame(point_estimates).plot(kind="density",  # Plot sample mean density
                                   figsize=(9,9),
                                   xlim=(41,45)))   
print("Point Estimate Mean",np.array(point_estimates).mean())
print(population_ages.mean() - np.array(point_estimates).mean())

t=[]
for i in range(len(point_estimates)):
    t.append((population_ages.mean()-point_estimates[i]))
        
    print("i={0},Population Mean={1},sample mean={2}, difference={3}".format(i,population_ages.mean(),point_estimates[i],t[i]))
    
print(t.sort())



