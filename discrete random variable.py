import math
x=[0,1,2,3,4]
p=[0.37,0.39,0.19,0.04,0.01]
e=[0,0,0,0,0]
x2=[0,0,0,0,0]
sumx=0
sumx2=0
for i in range(0,5):
    e[i]=x[i]*p[i]
    sumx=sumx + e[i]
    x2[i]=x[i]*x[i]
    sumx2=sumx2+x2[i]*p[i]
print("Expectation of x")
print(sumx)
print("Expectation of X^2")
print(sumx2)
print("Variance of X")
variance=sumx2-sumx*sumx
print(variance)
print("Standard Deviation of X")
std=math.sqrt(variance)
print(std)

