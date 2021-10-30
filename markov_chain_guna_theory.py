import numpy as np
 #Guna Theory
T=[[0.09,0.29,0.62],[0.29,0.6,0.11],[0.62,0.11,0.17]]
A=[0.6,0.3,0.1]#(258 iterations convergence for sattvic,478 for 500)
#A=[0.3,0.6,0.1]#(259 iterations convergence for rajasic,479 for 500 iterations)
#A=[0.1,0.3,0.6]#(257 iterations convergence for tamasic for 300 iterations, 475 for 500)
#A=[0.2,0.8,0]
#T=[[0.125,0.25,0.125],[0.04,0.25,0.21],[0,0,0]]

v=np.dot(A,T)
#print(v)
for i in range(10):
    v=np.dot(A,T)
    print("Iteration{0},v={1}".format(i,v))
    A=v   
