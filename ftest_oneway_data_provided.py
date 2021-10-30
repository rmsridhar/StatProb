import pandas as pd
from scipy import stats
from statsmodels.stats import weightstats as stests
import numpy as np

#x=[8,10,7,14,11,0]
#y=[7,5,10,9,9]
#z=[12,9,13,12,14]

x=[86,65,90,75]
y=[96,80,70,80,91]
z=[85,90,95,70,70]
count_x=np.count_nonzero(x)
count_y=np.count_nonzero(y)
count_z=np.count_nonzero(z)
sum_x=sum(x)
sum_y=sum(y)
sum_z=sum(z)
sum_x2=0
sum_y2=0
sum_z2=0
total_sum_of_all_observations=sum_x+sum_y+sum_z

for i in range(len(x)):
      sum_x2=sum_x2+x[i]*x[i]
for i in range(len(y)):
      sum_y2=sum_y2+y[i]*y[i]
for i in range(len(z)):
      sum_z2=sum_z2+z[i]*z[i]

number_of_elements=count_x+count_y+count_z
print("number of elements",number_of_elements)
print("sum of x= {0}, y={1},z={2}".format(sum_x,sum_y,sum_z))
print("sum of x^2= {0}, y^2={1},z^2={2}".format(sum_x2,sum_y2,sum_z2))
correction_factor=total_sum_of_all_observations**2/number_of_elements
print("Correction Factor=",correction_factor)

sum_of_squares_between_samples=(sum_x*sum_x/count_x+sum_y*sum_y/count_y+sum_z*sum_z/count_z)-correction_factor
print("Between",sum_of_squares_between_samples)

Total_sum_of_squares=sum_x2+sum_y2+sum_z2-correction_factor
print("Total",Total_sum_of_squares)
sum_of_squares_within_samples=Total_sum_of_squares-sum_of_squares_between_samples
print("Within",sum_of_squares_within_samples)

Mean_square_between=sum_of_squares_between_samples/2
Mean_square_within=sum_of_squares_within_samples/(number_of_elements-3)
f_test=Mean_square_between/Mean_square_within
print("f_test=",f_test)

#sum_x2=(x[i]*x[i] for(i in range(np.count_nonzero(x))))

F, p = stats.f_oneway(x,y,z)

#F, p = stats.f_oneway(overcast,rainy,sunny)
print("F statistics",F)
print("p-value for significance is: ", p)
if p<0.05:
    print("reject null hypothesis")
else:
    print("accept null hypothesis")
