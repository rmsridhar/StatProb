# Montecarlo procedure to find the area of y=x^2
import random
import matplotlib.pyplot as plt
n=int(input("Enter the values"))
x=[]
y=[]
sum1=0
for i in range(n):
    t=random.random()
    x.append(i)
    y.append(i)
    x[i]=t
    y[i]=t*t
    sum1=sum1+y[i]
plt.plot(x,y,linewidth=3,color='r')
plt.show()
print(sum1/n)


