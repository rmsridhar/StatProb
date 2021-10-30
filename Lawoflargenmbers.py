import numpy as np
import random
import matplotlib.pyplot as plt
import math
import scipy.stats as stats
## weak law of large number
# Step 1
# create population with a gamma distribution
shape, scale = 2., 2.  # mean=4, std=2*sqrt(2)
s = np.random.gamma(shape, scale, 1000000)
s.sort()
pdf_pop1=stats.norm.pdf(s,np.mean(s),np.std(s))
plt.plot(s,pdf_pop1,linewidth=3,color='b')
plt.show()
# Step 2
samplemeanlist = [] # list of sample mean
l = [] # list of smaple size, for x-axis of box plots
numberofsample = 50 # number of sample in each sample size
    
# set sample size (i) between 100 to 8100, step by 500
for i in range(100,9101,500):
    # set x-axis
    l.append(i)
    # list of mean of each sample
    ml = []
    # sample 50 time.
    for n in range(0,numberofsample):
        # random pick from population with sample size = i
        rs = random.choices(s, k=i)
        # calculate the mean of each sample and save it in list of mean
        ml.append(sum(rs)/i)
        #ml.append(mean(rs))
    
    # save the 50 sample mean in samplemeanlist for box plots
    samplemeanlist.append(ml)
   
# Step 3
# set figure size
boxplots = plt.figure(figsize=(20,10))
# plot box plots of each sample mean
plt.boxplot(samplemeanlist,labels = l)
# show plot.
boxplots.show()

print("population S," + \
      "mean:" + str(np.mean(s)) + \
      ", standard deviation: "+ str(np.std(s)/math.sqrt(9100)))

print("sample with 100 sample size," + \
      "mean:" + str(np.mean(samplemeanlist[0])) + \
      ", standard deviation: "+ str(np.std(samplemeanlist[0])))

print("sample with 7600 sample size," + \
      "mean:" + str(np.mean(samplemeanlist[15])) + \
      ", standard deviation: "+ str(np.std(samplemeanlist[15])))
print("sample with 8100 sample size," + \
      "mean:" + str(np.mean(samplemeanlist[16])) + \
      ", standard deviation: "+ str(np.std(samplemeanlist[16])))

print("sample with 8600 sample size," + \
      "mean:" + str(np.mean(samplemeanlist[17])) + \
      ", standard deviation: "+ str(np.std(samplemeanlist[16])))

print("sample with 9100 sample size," + \
      "mean:" + str(np.mean(samplemeanlist[18])) + \
      ", standard deviation: "+ str(np.std(samplemeanlist[18])))

samplemeanlist.sort()
pdf_pop1=stats.norm.pdf(samplemeanlist,np.mean(samplemeanlist),np.std(samplemeanlist))
plt.plot(samplemeanlist,pdf_pop1,linewidth=3,color='b')
plt.show()

#import scipy.stats as stats
#pdf_pop=stats.norm.pdf(s,np.mean(s),np.std(s))
#plt.plot(s,pdf_pop,linewidth=3,color='b')
#plt.show()
# last hist plot
#histplot = plt.figure(figsize=(20,10))
#plt.hist(samplemeanlist[0], 10, density=True)
#plt.hist(samplemeanlist[16], 10, density=True)
#histplot.show()
