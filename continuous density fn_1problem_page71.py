# Suppose you choose at random a real number X from the interval [2,10].
#Find the density function f(x) and the probability of an event E
#for this experiment, where E is a subinterval [a,b] of [2 ,10]. (b)
#From (a), ﬁnd the probability that X>5, that 5 <X<7, and that X2 −12X +35>0.
import random
n=int(input("enter the value for n"))
x=0
y=0
z=0
for i in range(n):
    t=random.choice([2,3,4,5,6,7,8,9,10])
    if t>5:
        x=x+1
    if (t>5) and (t<7):
        y=y+1
    if (t**2-12*t+35)>0:
        z=z+1
print("Probability of x>5",x/n)
print("Probability of 5<x<7",y/n)
print("Probability of X2-12x+35>0",z/n)
