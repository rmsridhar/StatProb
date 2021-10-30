import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import random
import math
np.random.seed(10)
population_ages1 = stats.poisson.rvs(loc=18, mu=35, size=150000)
population_ages2 = stats.poisson.rvs(loc=18, mu=10, size=100000)
population_ages = np.concatenate((population_ages1, population_ages2))

print("Population Ages Mean",population_ages.mean())

np.random.seed(6)
sample_ages = np.random.choice(a= population_ages,
                               size=500)            # Sample 500 values

print ("Sample mean", sample_ages.mean() )                         # Show sample mean

print("difference between means",population_ages.mean() - sample_ages.mean())   # Check difference between means


#The distribution has low skewness, but the plot reveals the data is clearly not normal:
#instead of one symmetric bell curve, it has as bimodal distribution
#with two high density peaks. 
plt.show(pd.DataFrame(population_ages).hist(bins=58,
                                  range=(17.5,75.5),
                                  figsize=(9,9)))

print( stats.skew(population_ages))
#The sample we drew from this population should have roughly the same shape and skew:
plt.show(pd.DataFrame(sample_ages).hist(bins=58,
                                  range=(17.5,75.5),
                                  figsize=(9,9)))
print( stats.skew(sample_ages) )

 #let's create a sampling distribution by taking 200 samples from our population and
 #then making 200 point estimates of the mean:
np.random.seed(10)

point_estimates = []         # Make empty list to hold point estimates

for x in range(200):         # Generate 200 samples
    sample = np.random.choice(a= population_ages, size=500)
    point_estimates.append( sample.mean() )
    
plt.show(pd.DataFrame(point_estimates).plot(kind="density",  # Plot sample mean density
                                   figsize=(9,9),
                                   xlim=(41,45)))   
print("Point Estimate Mean",np.array(point_estimates).mean())
print(population_ages.mean() - np.array(point_estimates).mean())

#Let's calculate a 95% confidence for our mean point estimate:

np.random.seed(10)

sample_size = 500
sample = np.random.choice(a= population_ages, size = sample_size)
sample_mean = sample.mean()

z_critical = stats.norm.ppf(q = 0.975)  # Get the z-critical value* ppf->percent point function

print("z-critical value:")              # Check the z-critical value
print(z_critical)                        

pop_stdev = population_ages.std()  # Get the population standard deviation

margin_of_error = z_critical * (pop_stdev/math.sqrt(sample_size))

confidence_interval = (sample_mean - margin_of_error,
                       sample_mean + margin_of_error)  

print("Confidence interval of mean1:")
print(confidence_interval)
# We use stats.norm.ppf(q = 0.975) to get the desired z-critical value instead of q = 0.95
#because the distribution has two tails.
#Notice that the confidence interval we calculated captures the true population mean
#of 43.0023.
#Let's create several confidence intervals and plot them to get a
#better sense of what it means to "capture" the true mean:

np.random.seed(12)

sample_size = 1000

intervals = []
sample_means = []

for sample in range(25):
    sample = np.random.choice(a= population_ages, size = sample_size)
    sample_mean = sample.mean()
    sample_means.append(sample_mean)

    z_critical = stats.norm.ppf(q = 0.975)  # Get the z-critical value*         

    pop_stdev = population_ages.std()  # Get the population standard deviation

    margin_of_error = z_critical * (pop_stdev/math.sqrt(sample_size))

    confidence_interval = (sample_mean - margin_of_error,
                           sample_mean + margin_of_error)  
    
    intervals.append(confidence_interval)

plt.figure(figsize=(9,9))

plt.errorbar(x=np.arange(0.1, 25, 1), 
             y=sample_means, 
             yerr=[(top-bot)/2 for top,bot in intervals],
             fmt='o')

plt.hlines(xmin=0, xmax=25,
           y=43.0023, 
           linewidth=2.0,
           color="red")
plt.show()
t=[]
for i in range(len(sample_means)):
    t.append((population_ages.mean()-sample_means[i])*(population_ages.mean()-sample_means[i]))
    
    
    print("i={0},Population Mean={1},sample mean={2}, difference={3}".format(i,population_ages.mean(),sample_means[i],t[i]))
    
print(t.sort())

#Notice that in the plot above, all but one of the 95% confidence intervals
#overlap the red line marking the true mean. This is to be expected:
#since a 95% confidence interval captures the true mean 95% of the time,
#we'd expect our interval to miss the true mean 5% of the time.
# t-distribution
np.random.seed(10)

sample_size = 25
sample = np.random.choice(a= population_ages, size = sample_size)
sample_mean = sample.mean()

t_critical = stats.t.ppf(q = 0.975, df=24)  # Get the t-critical value*

print("t-critical value:")                  # Check the t-critical value
print(t_critical)                        

#sample_stdev = sample.std(ddof=1)    # Get the sample standard deviation
sample_stdev = sample.std()

sigma = sample_stdev/math.sqrt(sample_size)  # Standard deviation estimate
margin_of_error = t_critical * sigma

confidence_interval = (sample_mean - margin_of_error,
                       sample_mean + margin_of_error)  

print("Confidence interval of mean2:")
print(confidence_interval)

random.seed(10)
population_races = (["white"]*100000) + (["black"]*50000) +\
                   (["hispanic"]*50000) + (["asian"]*25000) +\
                   (["other"]*25000)
    
demo_sample = random.sample(population_races, 1000)   # Sample 1000 values

for race in set(demo_sample):
    print( race + " proportion estimate:" )
    print( demo_sample.count(race)/1000 )


# Check the difference between critical values with a sample size of 1000
             
#print(stats.t.ppf(q=0.975, df= 999) - stats.norm.ppf(0.975))

#Instead of calculating a confidence interval for a mean point estimate by hand,
#you can calculate it using the Python function stats.t.interval():
#print(stats.t.interval(alpha = 0.95,              # Confidence level
#                 df= 24,                    # Degrees of freedom
#                 loc = sample_mean,         # Sample mean
#                 scale = sigma))             # Standard deviation estimate


#We can also make a confidence interval for a point estimate of a population proportion. 
z_critical = stats.norm.ppf(0.975)      # Record z-critical value

p = 0.192                               # Point estimate of proportion

n = 1000                                # Sample size

margin_of_error = z_critical * math.sqrt((p*(1-p))/n)

confidence_interval = (p - margin_of_error,  # Calculate the the interval
                       p + margin_of_error)
print("point estimate of a population proportion",confidence_interval)



#. In this case were working with z-critical values so we want to work with the normal distribution
#instead of the t distribution:

print(stats.norm.interval(alpha = 0.95,    # Confidence level             
                   loc =  0.192,     # Point estimate of proportion
                   scale = math.sqrt((p*(1-p))/n)))  # Scaling factor
