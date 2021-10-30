import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random


# logistic function 1/(1+pow(e,beta*t+alpha))
func=lambda x:1/(1+ np.exp(-beta*x-alpha))

#logistic distribution
x1=np.linspace(0,1,1000)
y1=[]
y2=[]
alpha=1
beta=2
for i in range(len(x1)):
    y1.append(i)
    y1[i]=func(x1[i])
    #plt.plot(x1[i],y1[i])
    #alpha=1
    #beta=-1
    #y2.append(i)
    #y2[i]=func(x1[i])
    #plt.plot(x1[i],y2[i])
#print("x1=",x1,"y1=",y1)

#logistic distribution MCMC
# Lets define our Beta Function to generate s for any particular state. We don't care for the normalizing constant here.
def beta_s(x,alpha,beta):
    return 1/(1+ np.exp(-beta*x-alpha))

# This Function returns True if the coin with probability P of heads comes heads when flipped.
def random_coin(p):
    unif = random.uniform(0,1)
    if unif>=p:
        return False
    else:
        return True

states = []
cur = random.uniform(0,1)
for i in range(len(x1)):
    states.append(cur)
    next = random.uniform(0,1)
    ap = min(beta_s(next,alpha,beta)/beta_s(cur,alpha,beta),1) # Calculate the acceptance probability
    if random_coin(ap):
        cur = next

plt.hist(states,normed=True,bins =100, histtype='step',label="Simulated_MCMC: alpha="+str(alpha)+", beta="+str(beta))
plt.plot(x1,y1,label="alpha="+str(alpha)+",beta="+str(beta))
#plt.plot(x1,y2,label="alpha=1,beta=-1")
plt.legend()
plt.show()


