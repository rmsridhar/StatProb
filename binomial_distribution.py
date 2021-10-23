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

n=int(input("enter the value of n"))
p=float(input("enter the value of success"))
q=round(1-p,3)
print(q)
x=[]
t=range(0,n+1)
for i in range(0,n+1):
    x.append(i)
   # print(fact(n))
   # print(fact(i))
   # print(fact(n-i))
    print(i)
    x[i]=fact(n)/(fact(i)* fact(n-i))* round(pow(p,i),10)*round(pow(q,n-i),10)
    #print(pow(p,i))
    #print(pow(q,n-i))
   # print(i)
    print(x[i])
print("Expectation of Binomial Distribution")
print(n*p)
print("Variance of Binomial Distribution")
print(n*p*q)
print("Standard Deviation")
print(math.sqrt(n*p*q))
plt.plot(t,x)
plt.show()






    
