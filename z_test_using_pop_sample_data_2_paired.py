import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
from statsmodels.stats import weightstats as stests

# 100 simulations of die roll
n = 1000

# In each simulation, there are 1000 data produced  from 1 to 100
pop= []
for i in range(n):
    a = np.random.randint(1,100)
    pop.append(i)
    pop[i]=a
# sample 1 of 100 from population of 1000
x1=[]
pop_mean=np.mean(pop)
pop_std=np.std(pop)
for i in range(200):
    a = np.random.randint(1,100)
    x1.append(i)
    x1[i]=pop[a]
x1_mean=np.mean(x1)
x1_std=np.std(x1)
# sample 2 of 100 from population of 1000
y1=[]
pop_mean=np.mean(pop)
pop_std=np.std(pop)
for i in range(300):
    a = np.random.randint(1,100)
    y1.append(i)
    y1[i]=pop[a]
y1_mean=np.mean(y1)
y1_std=np.std(y1)
ztest ,pval = stests.ztest(x1, y1)#, value=0,alternative='two-sided')
print("Test statistics",ztest)
print("p-values",pval)
if pval < 0.05:    # alpha value is 0.05 or 5%
   print(" we are rejecting null hypothesis")
else:
  print("we are accepting null hypothesis")

