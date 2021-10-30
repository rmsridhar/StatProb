import numpy as np
#pepsi coke
T=[[0.7,0.3],[0.1,0.9]]
A=[0.55,0.45]
v=np.dot(A,T)
#print(v)
for i in range(100):
    v=np.dot(A,T)
    print("Iteration{0},v={1}".format(i,v))
    A=v
print(v)
print("Iteration{0},v={1}".format(i,v))

#fundamental Limit Theorem
#T=[[0, 1, 0, 0],[1/3, 0, 1/3, 1/3],[0, 1/2, 0, 1/2],[0, 1/2, 1/2, 0]]
#T=[[1/2, 1/4, 1/4],[1/2, 0, 1/2],[1/4, 1/4, 1/2]]
#f=T
#for i in range(20):
#    v=np.dot(f,T)
#    print("i={0},v={1}".format(i,v))
#    f=v

 #Guna Theory
#T=[[0.09,0.29,0.62],[0.29,0.6,0.11],[0.62,0.21,0.17]]
#A=[0.6,0.1,0.3]
#v=np.dot(A,T)
#print(v)
#for i in range(100):
#    v=np.dot(A,T)
#    print("Iteration{0},v={1}".format(i,v))
#    A=v   
