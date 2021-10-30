from scipy.stats import poisson

# importing numpy as np
import numpy as np
 
# importing matplotlib as plt
import matplotlib.pyplot as plt
# creating a numpy array for x-axis
x=np.arange(0,7,1)
#print(r_values)
#mu=3000*0.001
mu=3000*0.001

# poisson distribution data for y-axis
y = poisson.pmf(x, mu, loc=0)

print("X:",x,"Y:",y)
 
# plotting the graph
plt.plot(x, y)
 
# showing the graph
plt.show()
mean, var, skew, kurt = poisson.stats(mu, moments='mvsk')
print(mean)
print(var)
print(skew)
print(kurt)
