import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
from statsmodels.stats import weightstats as stests
# 1000 simulations of die roll
n = 1000

# In each simulation, there is one trial more than the previous simulation
avg = []
for i in range(1,n):
    a = np.random.randint(1,7,i)
    avg.append(np.average(a))
# sample 10 expected value of die rolls

plt.title("10 samples")
avg[1:10]
plt.hist(avg[1:10])
plt.show()
plt.title("100 samples")
avg[1:100]
plt.hist(avg[1:100])
plt.show()
plt.title("200 samples")
avg[1:200]
plt.hist(avg[1:200])
plt.show()
plt.title("300 samples")
avg[1:300]
plt.hist(avg[1:300])
plt.show()
plt.title("400 samples")
avg[1:400]
plt.hist(avg[1:400])
plt.show()
x1=[]
x2=[]
for i in range(100):
    x1.append(avg[i])
for i in range(200):
    x2.append(avg[i])
print(x1)
print(x2)
ztest ,pval1 = stests.ztest(x1, x2)#, value=0,alternative='two-sided')
print("Test statistics",ztest)
print(float(pval1))
if pval1<0.05:
    print("reject null hypothesis")
else:
    print("accept null hypothesis")
