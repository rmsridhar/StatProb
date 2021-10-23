import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.stats import normaltest
from scipy.stats import shapiro
import random
import math
v=[]
for i in range(1000000):
    rand1=random.randint(0,90)
    v.append(rand1)
   # v.append(i)
  #  v[i]=rand1
print("Population mean=",np.mean(v))
print("Population SD=",np.std(v))
#print("Population and sample SD=",np.std(v)/math.sqrt(1000))
v.sort()
print(v)
pdf_pop=stats.norm.pdf(v,np.mean(v),np.std(v))
plt.plot(v,pdf_pop,linewidth=3,color='b')
plt.show()
y=[]
#1000 sample
for i in range(1000):
    x=[]
    m=0
    for j in range(750):
        rand1=random.randint(0,90)
        x.append(m)
        x[m]=rand1
        m=m+1
    y.append(np.mean(x))
#print(y)
#df=pd.DataFrame(y)
#print(df)
#df.describe()
#print(df.describe())
#df.hist()
#plt.show()
y.sort()
pdf_pop1=stats.norm.pdf(y,np.mean(y),np.std(y))
plt.plot(y,pdf_pop1,linewidth=3,color='b')
plt.show()
print("sample mean1000",np.mean(y))
print("Sample Standard Deviation",np.std(y))
print("sample deviation is=",np.std(v)/math.sqrt(len(y)))
y=[]
#10000 sample
for i in range(10000):
    x=[]
    m=0
    for j in range(750):
        rand1=random.randint(0,90)
        x.append(m)
        x[m]=rand1
        m=m+1
    y.append(np.mean(x))
#print(y)
#df=pd.DataFrame(y)
#print(df)
#df.describe()
#print(df.describe())
#df.hist()
#plt.show()
y.sort()
pdf_pop1=stats.norm.pdf(y,np.mean(y),np.std(y))
plt.plot(y,pdf_pop1,linewidth=3,color='b')
plt.show()
print("sample mean 10000",np.mean(y))
print("Sample Standard Deviation",np.std(y))
print("sample deviation is=",np.std(v)/math.sqrt(len(y)))



# sample is not drawn from [0 90] but from population 
y=[]
for i in range(1000):
    x=[]
    m=0
    for j in range(750):
        rand1=random.randint(0,999999)
        x.append(m)
        x[m]=v[rand1]
        m=m+1
    y.append(np.mean(x))
#print(y)
#df=pd.DataFrame(y)
#print(df)
#df.describe()
#print(df.describe())
#df.hist()
#plt.show()
y.sort()
pdf_pop1=stats.norm.pdf(y,np.mean(y),np.std(y))
plt.plot(y,pdf_pop1,linewidth=3,color='b')
plt.show()
print("sample mean from population 999999",np.mean(y))
print("Sample Standard Deviation",np.std(y))
print("sample deviation is=",np.std(v)/math.sqrt(len(y)))


#stat, p = normaltest(v)
#print('Statistics=%.3f, p value of population=%.3f' % (stat, p))

#stat, p = normaltest(y)
#print('Statistics=%.3f, p value of sample=%.3f' % (stat, p))
#print(abs((np.mean(y)-np.mean(v))))
#n=1000-1
#tstatistic=abs((np.mean(y)-np.mean(v)))/(np.std(y)/math.sqrt(n))
#alpha=0.05
#if (tstatistic > 0.05):
#    print("There is no difference between population and sample mean",tstatistic)
#else:
#    print("There is difference between population and sample mean",tstatistic)
#stat, p = shapiro(y)
#print('Statistics=%.3f, p=%.3f' % (stat, p)) 


