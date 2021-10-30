from scipy.stats import kstest 
import random
from scipy.stats import stats
  
# N = int(input("Enter number of random numbers: ")) 
N = 10
  
actual =[] 
print("Enter outcomes: ") 
  
for i in range(N): 
    # x = float(input("Outcomes of class "+str(i + 1)+": ")) 
    actual.append(random.random()) 
      
print(actual)

x = kstest(actual, "norm")    
print(x) 

# Two sample KStest
rvs1=[11,23,42,15,23,34]
rvs2=[12,34,36,26,37,54]
t=stats.ks_2samp(rvs1, rvs2)
print(t)


