import math
def fact(n):
    if (n==0):
        return 1
      
    if (n==1):
        return 1
    else:
        return (n*fact(n-1))

#print(recursion(3))

k=int(input("enter the population size of k"))
n=[] 
p=[]
s=0
prob=1
v=1
for i in range(0,k+1):
    n.append(i)
    n[i]=float(input("enter the population size of n1,n2,n3"))
    p.append(i)
    p[i]=float(input("enter the population size of p1,p2,p3"))
    s=s+n[i]
    prob=prob*pow(p[i],n[i])
    v=v*fact(n[i])
    print(n[i])
#print(prob)
#print(v)
multinomial=fact(s) * prob /v
print(multinomial)


from scipy.stats import multinomial
rv = multinomial(8, [0.3, 0.2, 0.5])
multi_value=rv.pmf([1, 3, 4])
print(multi_value)

from scipy.stats import multinomial
rv = multinomial(5, [0.25, 0.25, 0.25,0.25])
multi_value=rv.pmf([1, 1, 1,2])
print(multi_value)



    
