import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
from scipy.stats import ttest_ind
n = 100
# In each simulation, there are 100 times from 1 to 100 are generated
pop= []
for i in range(n):
    a = np.random.randint(1,100)
    pop.append(i)
    pop[i]=a
# sample 10
print(pop)
x1=[]
pop_mean=np.mean(pop)
pop_std=np.std(pop)
for i in range(10):
    a = np.random.randint(1,10)
    x1.append(i)
    #x1[i]=a
    x1[i]=pop[a]
#x1_mean=np.mean(x1)
#x1_std=np.std(x1)
#sample 15
print(x1)
y1=[]
#pop_mean=np.mean(pop)
#pop_std=np.std(pop)
for i in range(15):
    a = np.random.randint(1,100)
    y1.append(i)
    #y1[i]=a
    y1[i]=pop[a]
#y1_mean=np.mean(y1)
#y1_std=np.std(y1)
print(y1)
tset, pval = ttest_ind(x1,y1)
print("Test Statistics",tset)
print("p-values",pval)
if pval < 0.05:    # alpha value is 0.05 or 5%
   print(" we are rejecting null hypothesis")
else:
  print("we are accepting null hypothesis")

