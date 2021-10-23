import math
#p=[0.3,0.5,0.2]
#p=[0.1,0.6,0.3]
#p=[0.5,0.25,0.25]
p=[0.2,0.4,0.2,0.2]
d=[]
d.append(0)
d[0]=0
for i in range(200):
    d.append(i)
    #d[i]=p[0]+p[1]*d[i-1]+p[2]*d[i-1]*d[i-1]
    d[i]=p[0]+p[1]*d[i-1]+p[2]*d[i-1]*d[i-1]+p[3]*d[i-1]*d[i-1]*d[i-1]
    print("i={0},d={1}".format(i,d[i]))

