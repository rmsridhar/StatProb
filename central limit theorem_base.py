#generate random choice out of (0,1) 200 times
#(0 is Tail and 1 is Head, count how many times
#we got head. I will do this process 1000 time and
#try to plot histogram of the data. And as below this data is
#normally distributed and follow 68–95–99 rule.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import kstest 
import random
heads=[]
for j in range(2000):
    ht200=[]
    for i in range(200):
        ht200.append(random.choice([0,1]))
       #  ht200.append(random.random())
    heads.append(np.sum(ht200))
for j in range(len(heads)):
    print("heads",j,"=value",heads[j])

dfh=pd.DataFrame(heads)
dfh.head()
dfh.hist(bins=30)
print(dfh.describe())
plt.show()
x = kstest(dfh, "norm")
print(x)


