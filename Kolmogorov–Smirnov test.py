from scipy.stats import kstest 
import random 

# N = int(input("Enter number of random numbers: ")) 
N = 5
actual =[] 
print("Enter outcomes: ") 
for i in range(N): 
	# x = float(input("Outcomes of class "+str(i + 1)+": ")) 
	actual.append(random.random()) 
print(actual) 
x = kstest(actual, "uniform") 
print(x) 
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




