import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
from statsmodels.stats import weightstats as stests

# 100 simulations of integer from 1 to 100
n = 1000

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

for i in range(400):
    a = np.random.randint(1,100)
    x1.append(i)
    x1[i]=pop[a]
x1_mean=np.mean(x1)
x1_std=np.std(x1)
plt.title("40 samples")
plt.hist(x1[1:400])
plt.show()

#x1=[53,56,57,70,70,70,75,53,56,57,70,70,70,75,53,56,57,70,70,70,75,53,56,57,70,70,70,75,69,76]

z=(x1_mean-pop_mean)/(pop_std/np.sqrt(n))
print("z value=",z)

ztest, pval = stests.ztest(x1)
print("Test Statistics",ztest)
print("p-values",pval)
if pval < 0.05:    # alpha value is 0.05 or 5%
   print(" we are rejecting null hypothesis")
else:
  print("we are accepting null hypothesis")

