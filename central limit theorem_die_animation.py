import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import kstest
import scipy.stats as stats

# 1000 simulations of die roll
n = 10000

# In each simulation, there is one trial more than the previous simulation
avg = []
for i in range(2,n):
    a = np.random.randint(1,7,i)
    avg.append(np.average(a))
# sample 10 expected value of die rolls
plt.title("10 samples")
avg[1:10]
plt.hist(avg[1:10])
avg.sort()
pdf_pop=stats.norm.pdf(avg,np.mean(avg),np.std(avg))
plt.plot(avg,pdf_pop,linewidth=3,color='b')
plt.show()

x = kstest(avg[1:10], "norm")
print(x)
plt.title("100 samples")
avg[1:100]
plt.hist(avg[1:100])
avg.sort()
pdf_pop=stats.norm.pdf(avg,np.mean(avg),np.std(avg))
plt.plot(avg,pdf_pop,linewidth=3,color='b')
plt.show()

x = kstest(avg[1:100], "norm")
print(x)
plt.title("200 samples")
avg[1:200]
plt.hist(avg[1:200])
avg.sort()
pdf_pop=stats.norm.pdf(avg,np.mean(avg),np.std(avg))
plt.plot(avg,pdf_pop,linewidth=3,color='b')
plt.show()

x = kstest(avg[1:200], "norm")
print(x)
plt.title("300 samples")
avg[1:300]
plt.hist(avg[1:300])
avg.sort()
pdf_pop=stats.norm.pdf(avg,np.mean(avg),np.std(avg))
plt.plot(avg,pdf_pop,linewidth=3,color='b')
plt.show()

x = kstest(avg[1:300], "norm")
print(x)
plt.title("400 samples")
avg[1:400]
plt.hist(avg[1:400])
avg.sort()
pdf_pop=stats.norm.pdf(avg,np.mean(avg),np.std(avg))
plt.plot(avg,pdf_pop,linewidth=3,color='b')
plt.show()

x = kstest(avg[1:400], "norm")
print(x)
plt.title("1000 samples")
avg[1:1000]
plt.hist(avg[1:1000])
avg.sort()
pdf_pop=stats.norm.pdf(avg,np.mean(avg),np.std(avg))
plt.plot(avg,pdf_pop,linewidth=3,color='b')
plt.show()

x = kstest(avg[1:1000], "norm")
print(x)
