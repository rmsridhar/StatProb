import numpy as np
from scipy.stats import beta
from matplotlib import pyplot as plt
import random


# Define the distribution parameters to be plotted
#alpha_values = [3.0, 7.0]
#beta_values = [8.0, 4]
alpha_values = [1,5,100.0, 1000.0,10000.0]
beta_values = [1,5,100.0, 1000.0,10000]
linestyles = ['-', '--','-','--','-','-']
color=['r','b','g','m','k','r']
#x = np.linspace(0, 1, 1002)
xx=[]
for k in range(200):
    x=[]
    for i in range(100):
        t=random.choices([0,1])
        x.append(i)
        x[i]=t
    xx.append(k)
    xx[k]=x.count([1])/100
print(xx)
#------------------------------------------------------------
# plot the distributions
#fig, ax = plt.subplots(figsize=(5, 3.75))
xx.sort()
plt.figure(figsize=(10,10))
for a, b, ls,c in zip(alpha_values, beta_values, linestyles,color):
    dist = beta(a, b)
    plt.plot(xx, dist.pdf(xx), ls=ls, c=c,label=r'$\alpha=%.1f,\ \beta=%.1f$' % (a, b))
   #plt.plot(xx.mean(),dist.pdf(xx),linewidth=1,color='r')
plt.xlim(0, 1)
plt.ylim(0, 50)
plt.xlabel('$x$')
plt.ylabel(r'$p(x|\alpha,\beta)$')
plt.title('Beta Distribution')
plt.legend(loc=0)
plt.show()

dist=beta(100000,100000)
plt.plot(xx,dist.pdf(xx),linewidth=2,color='y')
plt.show()
print("Mean is ",np.mean(xx))


