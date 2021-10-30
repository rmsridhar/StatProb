import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
from scipy.stats import ttest_1samp
# 100 simulations of integer from 1 to 100
n = 100

# In each simulation, there is one trial more than the previous simulation
pop= []
for i in range(n):
    a = np.random.randint(1,100)
    pop.append(i)
    pop[i]=a
# sample 10 expected value of die rolls
print(pop)

x1=[]
pop_mean=np.mean(pop)
pop_std=np.std(pop)

for i in range(25):
    a = np.random.randint(1,100)
    x1.append(pop[a])
x1_mean=np.mean(x1)
x1_std=np.std(x1)
plt.title("25 samples")
plt.hist(x1[1:25])
plt.show()
n=25
t=(x1_mean-pop_mean)/(pop_std/np.sqrt(n))
print("t value=",t)

tset, pval = ttest_1samp(x1,np.mean(pop))
print("Test Statistics",tset)
print("p-values",pval)
if pval < 0.05:    # alpha value is 0.05 or 5%
   print(" we are rejecting null hypothesis")
else:
  print("we are accepting null hypothesis")

