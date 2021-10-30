import math
import matplotlib.pyplot as plt
def fact(n):
    if (n==0):
        return 1
      
    if (n==1):
        return 1
    else:
        return (n*fact(n-1))

#print(recursion(3))
s=int(input("press 1 for n,p,r value or 2 for lambda value"))
if (s==1):
    n=int(input("enter the value of n"))
    p=float(input("enter the value of success"))
    r=int(input("enter the value of r"))
    lambda1=n*p
else:
    lambda1=float(input("enter the value of lambda"))
    r=int(input("enter the value of r"))
x=[]
t=[] 
for i in range(0,r+1):
    t.append(i)
    x.append(i)
    print(i)
    x[i]=math.exp(-lambda1)* pow(lambda1,i)/fact(i)
    print(x[i])
print("Expectation of poisson  Distribution")
print(lambda1)
print("Variance of poisson Distribution")
print(lambda1)
plt.plot(t,x)
plt.show()

#print("Standard Deviation")
#print(math.sqrt(n*p*q))



    
