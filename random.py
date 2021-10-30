import random

# using choice() to generate a random number from a  
# given list of numbers. 
print ("A random number between 0 and 1 is : ", end="") 
print (random.random())


# using choice() to generate a random number from a  
# given list of numbers. 
print ("A random number from list is : ",end="") 
print (random.choice([1, 4, 8, 10, 3]))

# using seed() to seed a random number 
random.seed(5) 
  
    # printing mapped random number 
++print ("The mapped random number with 5 is : ", end="") 
print (random.random()) 
  
# using seed() to seed different random number 
random.seed(7) 
  
# printing mapped random number 
print ("The mapped random number with 7 is : ", end="") 
print (random.random()) 
  
# using seed() to seed to 5 again 
random.seed(5) 
  
# printing mapped random number 
print ("The mapped random number with 5 is : ",end="") 
print (random.random()) 
  
# using seed() to seed to 7 again  
random.seed(7) 
  
# printing mapped random number 
print ("The mapped random number with 7 is : ",end="") 
print (random.random()) 
#----------------------
# Dice rolling for 4 pg 4
#----------------------
val=0
h=0
t=0
val=int(input("enter the value"))
for i in range(1,val):
    r=random.choice([1,2,3,4,5,6])
    if (r==6):
        t=t+1
print(t)
#---------------------
# Dice rolling for 24 pg 4
#----------------------
val=0
h=0
t=0
val=int(input("enter the value"))
for i in range(1,val):
    r1=random.choice([1,2,3,4,5,6])
    r2=random.choice([1,2,3,4,5,6])
    
    if (r1==6) and (r2==6):
        t=t+1
print(t)


#--------------------------------
#coin Tossing pg 5
val=0
h=0
t=0
val=int(input("enter the value"))
for i in range(1,val):
    r=random.choice([0,1])
    if (r==0):
        t=t+1
    if (r==1):
        h=h+1
        
print(t)
print(h)
print("The probability of head approaching 0.5")
print(h/val)
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
#---------------
#Roulette wheel 38 slots  pg 13
#-----------------
val=0
win=0
val=int(input("enter the value"))
for i in range(1,val):
    r=random.choice([0,0.5,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,])
    if (r>=1) and (r<=18):
        win=win+1
print(win)



