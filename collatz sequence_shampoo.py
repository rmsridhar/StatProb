#The following iterative sequence is defined for the set of positive integers:

#n → n/2 (n is even)
#n → 3n + 1 (n is odd)

#Using the rule above and starting with 13, we generate the following sequence:


#13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

#Which starting number, under one million, produces the longest chain?

#NOTE: Once the chain starts the terms are allowed to go above one million.

import pandas  as pd
import random
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("EDS_Day_to_Day_Sales.csv")
#x=df['Sales']
x=df['Value']
counter_elements=[]
random_element=[]
for i in range(len(x)):
    n=int(x[i])
    m=n
    counter=0
    while (m!=1):
        if (m%2==0):
            m=m/2
        else:
            m=3*m+1
        counter=counter+1
    counter_elements.append(i)
    random_element.append(i)
    counter_elements[i]=counter
    random_element[i]=n
print(random_element,counter_elements)    
x=random_element
y=counter_elements
print(np.corrcoef(x,y))
print(np.mean(x),np.std(x))
print(np.mean(y),np.std(y))
plt.xlabel('Random Elements')
plt.ylabel('Counting')
plt.title('Collatz Sequence')
plt.scatter(x,y)
plt.show()

