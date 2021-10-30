# Montecarlo procedure to find the area of x^2+y^2=0.5^2
import random
import matplotlib.pyplot as plt
n=int(input("Enter the values"))
x=[]
y=[]
sum1=0
m=0
for i in range(n):
    t1=random.random()
    t2=random.random()
    if (t1*t1+t2*t2<=0.5*0.5):
        x.append(m)
        y.append(m)
        x[m]=t1
        y[m]=t2
        sum1=sum1+x[m]*x[m]+y[m]*y[m]
        m=m+1
plt.plot(x,y,linewidth=3,color='r')
plt.show()
print("m=",m)
print(sum1/m)


