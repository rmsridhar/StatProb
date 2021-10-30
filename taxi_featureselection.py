#Context
#Bob has started his own mobile company. He wants to give tough fight to big companies like Apple,
#Samsung etc.

#He does not know how to estimate price of mobiles his company creates.
#In this competitive mobile phone market you cannot simply assume things.
#To solve this problem he collects sales data of mobile phones of various companies.

#Bob wants to find out some relation between features of a mobile phone
#(eg:- RAM,Internal Memory etc) and its selling price. But he is not so good
#at Machine Learning. So he needs your help to solve this problem.

#In this problem you do not have to predict actual price but a price range
#indicating how high the price is
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

# fEATURE SELECTION
#data = pd.read_csv("myc_taxi_distance_day_month_year_hr_min_sec.csv")
data = pd.read_csv("taxi_data.csv")
print(data.isnull().sum())
x=data['pickup_month']
y=data['trip_duration']
m,b=np.polyfit(x,y,1)
plt.scatter(data['pickup_month'], data['trip_duration'], color='red')
plt.title('Distance Vs Trip_duration', fontsize=14)
plt.xlabel('Pickup_month', fontsize=14)
plt.ylabel('Trip_duration', fontsize=14)
plt.grid(True)
plt.plot(x,m*x+b)
plt.show()


x=data['distance']
y=data['trip_duration']
m,b=np.polyfit(x,y,1)
plt.scatter(data['distance'], data['trip_duration'], color='red')
plt.title('Distance Vs Trip_duration', fontsize=14)
plt.xlabel('Distance', fontsize=14)
plt.ylabel('Trip_duration', fontsize=14)
plt.grid(True)
plt.plot(x,m*x+b)
plt.show()

x=data['Speed']
y=data['trip_duration']
m,b=np.polyfit(x,y,1)
plt.scatter(data['Speed'], data['trip_duration'], color='red')
plt.title('Speed Vs Trip_duration', fontsize=14)
plt.xlabel('Speed', fontsize=14)
plt.ylabel('Trip_duration', fontsize=14)
plt.grid(True)
plt.plot(x,m*x+b)
plt.show()


x=data['distance']
y=data['Speed']
m,b=np.polyfit(x,y,1)
plt.scatter(data['distance'], data['Speed'], color='red')
plt.title('Distance Vs Speed', fontsize=14)
plt.xlabel('Distance', fontsize=14)
plt.ylabel('Speed', fontsize=14)
plt.grid(True)
plt.plot(x,m*x+b)
plt.show()
