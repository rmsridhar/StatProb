import numpy as np
import math
from statsmodels.stats import weightstats as stests
#ages = np.genfromtxt("body_fat.csv")
#x=[53,56,57,70,70,70,75]										
#y=[63,66,67,67,67,68,69,70,72,73,75,76,76,78,79,80,81]
x=[53,56,57,70,70,70,75,53,56,57,70,70,70,75,53,56,57,70,70,70,75,53,56,57,70,70,70,75,69,76]										
y=[63,66,67,67,67,68,69,70,72,73,75,76,76,78,79,80,81,67,68,69,70,72,73,75,76,76,78,79,80,81]
N1=np.count_nonzero(x)
N2=np.count_nonzero(y)
print("N1=",N1)
print("N2=",N2)
x_mean = np.mean(x)
y_mean = np.mean(y)
print("x mean value:",x_mean)
print("y mean value:",y_mean)
x_var = np.var(x)
y_var = np.var(y)
x_var1=0
y_var1=0
for i in range(len(x)):
  x_var1=x_var1 + (x[i]-x_mean)*(x[i]-x_mean)
for i in range(len(y)):
  y_var1=y_var1 + (y[i]-y_mean)*(y[i]-y_mean)
x_var1=x_var1/(N1-1)
y_var1=y_var1/(N2-1)
print("x_var1=",x_var1)
print("y_var1=",y_var1)
#print("x_var {0},y_var {1}".format(x_var,y_var))
S2=((x_var1/N1+y_var1/N2))
print("S2=",S2)
z=(x_mean-y_mean)/(np.sqrt(S2))
print("z value:",z)
ztest ,pval = stests.ztest(x,y)
print("ztest:",ztest)
print("p-value",pval)
if pval <0.05:
  print("we reject null hypothesis")
else:
  print("we accept null hypothesis")
