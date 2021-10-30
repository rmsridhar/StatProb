import random
#--------------------------------
# Horse races pg 6
print("Acron->0.3,Balky->0.4,chestnet->0.2,Dolby->0.1")
val=0
val=int(input("enter the value"))
a=0
b=0
c=0
d=0
for i in range(1,val):
    r=random.random()
    print(r)
    if (r<0.3):
        a=a+1
    if (r>=0.3) and (r<0.7):
        b=b+1
    if (r>0.7) and (r<0.9):
        c=c+1
    if (r>0.9):
        d=d+1
print(a)
print(b)
print(c)
print(d)
