#The following iterative sequence is defined for the set of positive integers:

#n → n/2 (n is even)
#n → 3n + 1 (n is odd)

#Using the rule above and starting with 13, we generate the following sequence:


#13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
#Although it has not been proved yet (Collatz Problem), it is thought that all starting
#numbers finish at 1.

#Which starting number, under one million, produces the longest chain?

#NOTE: Once the chain starts the terms are allowed to go above one million.

import pandas  as pd
import random
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("EDS_Day_to_Day_Sales.csv")
#x=df['Sales']
x=df['Value']
#counting number of elements for converging sales to 1 
counter_elements=[]
#sales element
sales_element=[]
for i in range(len(x)):
    n=int(x[i])
    m=n
    counter=0
    while (m!=1):
        if (m%2==0):
            m=m/2
        else:
            m=(3*m+1)*0.5
        counter=counter+1
    counter_elements.append(i)
    sales_element.append(i)
    counter_elements[i]=counter
    sales_element[i]=n
print(sales_element,counter_elements)    
x=sales_element
y=counter_elements
#correlation coefficient data
print(np.corrcoef(x,y))
print(np.mean(x),np.std(x))
print(np.mean(y),np.std(y))
plt.xlabel('Sales Data')
plt.ylabel('Counting')
plt.title('Collatz Sequence')
plt.scatter(x,y)
plt.show()
print("Mean of sales",np.mean(x))
print("Standard Deviation of sales",np.std(x))
# remove all sales > 200000 and counter >200
x_remove_sales=[]
y_remove_counter_elements=[]
for i in range(len(x)):
    if (x[i] <200000 and y[i]<200):
        x_remove_sales.append(x[i])
        y_remove_counter_elements.append(y[i])

#correlation coefficient data
#print(np.corrcoef(x_remove_sales,y_remove_counter_elements))
#print(np.mean(x),np.std(x))
#print(np.mean(y),np.std(y))
plt.xlabel('Sales Data')
plt.ylabel('Counting')
plt.title('Collatz Sequence')
plt.scatter(x_remove_sales,y_remove_counter_elements)
plt.show()

# mean and standard deviation of sales
print("Mean of sales",np.mean(x_remove_sales))
print("Standard Deviation of sales",np.std(x_remove_sales))
sales_value_low=np.mean(x_remove_sales)-np.std(x_remove_sales)
sales_value_max=np.mean(x_remove_sales)+np.std(x_remove_sales)
sales_value_true=0
for i in range(len(x)):
    if (x[i]>sales_value_low) and (x[i]<sales_value_max):
        sales_value_true=sales_value_true+1
print("Number of Sales Value lies between the interval",sales_value_true)
print("Possible Probability",sales_value_true/len(x))

