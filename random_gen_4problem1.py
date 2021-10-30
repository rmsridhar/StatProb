import random
#----------------------
# Random number generator 0 to 9
#----------------------
val=0
h=0
t=0
val=int(input("enter the value"))
x=[]
for i in range(0,val):
    x.append(i)
    x[i]=0

for i in range(0,val):
    r=random.choice([0,1,2,3,4,5,6,7,8,9])
    print(r)
    if (r==0):
        x[r]=x[r]+1
    if (r==1):
        x[r]= x[r]+1
    if (r==2):
        x[r]= x[r]+1
    if (r==3):
        x[r]= x[r]+1
    if (r==4):
        x[r]= x[r]+1
    if (r==5):
        x[r]= x[r]+1
    if (r==6):
        x[r]= x[r]+1
    if (r==7):
        x[r]= x[r]+1
    if (r==8):
        x[r]= x[r]+1
    if (r==9):
        x[r]= x[r]+1
print("the value is")    
print(x[0])
print(x[1])
print(x[2])
print(x[3])
print(x[4])
print(x[5])
print(x[6])
print(x[7])
print(x[8])
print(x[9])

#for i in range(0,val):
#    print("the value ",i)
#    print(x[i])
    
