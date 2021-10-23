import numpy as np
import statistics
import scipy.stats as stats1
import math
import matplotlib.pyplot as plt
# importing statistics module
import statistics
h = [186, 176, 158, 180, 186, 168, 168, 164, 178, 170, 189, 195, 172,
     187, 180, 186, 185, 168, 179, 178, 183, 179, 170, 175, 186, 159,
     161, 178, 175, 185, 175, 162, 173, 172, 177, 175, 172, 177, 180]
h.sort()
hmean = np.mean(h)
print("Mean=:",hmean)
# list of elements to calculate mean
      
n = len(h) 
print("n=",n)
get_sum = sum(h) 
mean = get_sum / n 
  
print("Mean / Average is: " + str(mean))

#--------------------
hvar=np.var(h)
print("Variance=:",hvar)
print(hvar)

sum1=0
i=0
for i in range(n):
    sum1=sum1+(h[i]-mean)*(h[i]-mean)
variance=sum1/n-1

print("Variance is:",variance)
print("Standard Deviation is:",math.sqrt(variance))


hstd = np.std(h)
print("Standard Deviation",hstd)
#--------------------------------

print("Median of data-set is : % s "
        % (statistics.median(h)))

# list of elements to calculate median 

h.sort() 
  
if n % 2 == 0: 
    median1 = h[n//2] 
    median2 = h[n//2 - 1] 
    median = (median1 + median2)/2
else: 
    median = h[n//2] 
print("Median is: " + str(median))
#--------------------
#print(statistics.median(h.sort()))

 #Python code to demonstrate the  
# working of median() function.
  

  
# unsorted list of random integers
#data1 = [2, -2, 3, 6, 9, 4, 5, -1]
  
  
# Printing median of the
# random data-set
#print("Median of data-set is : % s "
        #% (statistics.median(data1)))


# Python program to print 
# mode of elements
print(stats1.mode(h))


from collections import Counter 
  
# list of elements to calculate mode 

data = Counter(h)
print("data:",data)
get_mode = dict(data)
print("get_mode",get_mode)
#print(list(data.values()))
mode =[k for k, v in get_mode.items() if v == max(list(data.values()))] 
print(mode)
#if len(mode) == n: 
#    get_mode = "No mode found"
#else: 
   # get_mode = "Mode is / are: " + ', '.join(map(str, mode)) 
      
#print(get_mode)
#print(data.most_common())   # Returns all unique items and their counts
#print(data.most_common(1))  # Returns the highest occurring item

#In statistics, skewness and kurtosis are two ways to measure the shape of a distribution.

#Skewness is a measure of the asymmetry of a distribution.
#This value can be positive or negative.

#A negative skew indicates that the tail is on the left side of
#the distribution, which extends towards more negative values.
#A positive skew indicates that the tail is on the right side
#of the distribution, which extends towards more positive values.
#A value of zero indicates that there is no skewness in the
#distribution at all, meaning the distribution is perfectly symmetrical.
#If skewness is less than -1 or greater than 1,
#the distribution is highly skewed.
#If skewness is between -1 and -0.5 or between 0.5 and 1,
#the distribution is moderately skewed.
#If skewness is between -0.5 and 0.5, the distribution is approximately symmetric.
   
#Kurtosis is a measure of whether or not a distribution is
#heavy-tailed or light-tailed relative to a normal distribution.

#The kurtosis of a normal distribution is 3.
#If a given distribution has a kurtosis less than 3,
#it is said to be playkurtic, which means it tends to produce
#fewer and less extreme outliers than the normal distribution.
#If a given distribution has a kurtosis greater than 3,
#it is said to be leptokurtic, which means it tends to produce
#more outliers than the normal distribution.
#Note: Some formulas (Fisher’s definition) subtract 3 from the kurtosis
#to make it easier to compare with the normal distribution.
#Using this definition, a distribution would have kurtosis greater
#than a normal distribution
#The values for asymmetry and kurtosis between -2 and +2
#are considered acceptable in order to prove normal univariate distribution
#data = [88, 85, 82, 97, 67, 77, 74, 86, 81, 95, 77, 88, 85, 76, 81]

#calculate sample skewness
#print(stats1.skew(h, bias=True))
skewness1=stats1.skew(h)
print("skewness=",skewness1)
#0.032697

#calculate sample kurtosis
#print(stats1.kurtosis(h, bias=True))
kurtosis1=stats1.kurtosis(h)
print("Kurtosis=",kurtosis1)

h.sort()
hmean = np.mean(h)
#print(hmean)
hstd = np.std(h)
#print(hstd)
pdf = stats1.norm.pdf(h, hmean, hstd)
plt.plot(h, pdf,linewidth=3, color='y') # including h here is crucial
plt.show()

#0.118157
#The skewness turns out to be 0.032697 and the kurtosis turns out to be 0.118157.

#This means the distribution is slightly positively skewed and
#the distribution has more values
#in the tails compared to a normal distribution.
#if it had a kurtosis value greater than 0.
