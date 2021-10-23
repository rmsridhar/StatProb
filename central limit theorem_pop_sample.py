import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import math
h = [186, 176, 158, 180, 186, 168, 168, 164, 178, 170, 189, 195, 172,
     187, 180, 186, 185, 168, 179, 178, 183, 179, 170, 175, 186, 159,
     161, 178, 175, 185, 175, 162, 173, 172, 177, 175, 172, 177, 180,
     186, 176, 158, 180, 186, 168, 168, 164, 178, 170, 189, 195, 172,
     187, 180, 186, 185, 168, 179, 178, 183, 179, 170, 175, 186, 159,
     161, 178, 175, 185, 175, 162, 173, 172, 177, 175, 172, 177, 180]


print(np.mean(h))
print(np.std(h))
sum1=0
for j in range(40):
    pop=[]
    for i in range(30):
        t=random.choice([0,77])
        pop.append(i)
        pop[i]=h[t]
   # print(pop)
   # print('The mean of the population =',j,',',np.mean(pop))
   # print(np.std(pop)/math.sqrt(30))
    sum1=sum1+np.mean(pop)
    
mean1=sum1/40
print('The average of mean sample is =',mean1)



