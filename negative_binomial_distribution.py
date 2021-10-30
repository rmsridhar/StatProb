import math
def fact(n):
    if (n==0):
        return 1
      
    if (n==1):
        return 1
    else:
        return (n*fact(n-1))

#print(recursion(3))

n=int(input("enter the value of n"))
i=int(input("enter the value of success position"))
p=float(input("enter the value of probability"))
q=round(1-p,3)
print(q)
x=fact(n-1)/(fact(i-1)* fact(n-i))* round(pow(p,i),10)*round(pow(q,n-i),10)
print(pow(p,i))
print(pow(q,n-i))
   # print(i)
print(x)
print("Expectation of Negative Binomial Distribution")
print(i/p)
print("Variance of Negative Binomial Distribution")
t=(i*(1-p)/(p*p))
print(t)
print("Standard Deviation")
print(math.sqrt(t))



    
