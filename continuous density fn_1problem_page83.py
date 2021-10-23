#Choose independently two numbers B and C at random from the interval [−1,1]
#with uniform distribution, and consider the quadratic equation x2 + Bx+C =0.
#Find the probability that the roots of this equation
#(a) are both real. (b) are both positive.
import random

n=int(input("Enter the n value"))
for i in range(n):
    b=random.randrange(-1,1,0.0001)
    c=random.randrange(-1,1,0.0001)    
    v=i**2+b*i+c
    if (v==0):
        print("root is ",i)
