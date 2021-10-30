from pandas import DataFrame
import matplotlib.pyplot as plt
from sklearn import linear_model
import statsmodels.api as sm
from mpl_toolkits import mplot3d
import seaborn as sns
import numpy as np
Stock_Market = {'Year': [2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016],
                'Month': [12, 11,10,9,8,7,6,5,4,3,2,1,12,11,10,9,8,7,6,5,4,3,2,1],
                'Interest_Rate': [2.75,2.5,2.5,2.5,2.5,2.5,2.5,2.25,2.25,2.25,2,2,2,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75],
                'Unemployment_Rate': [5.3,5.3,5.3,5.3,5.4,5.6,5.5,5.5,5.5,5.6,5.7,5.9,6,5.9,5.8,6.1,6.2,6.1,6.1,6.1,5.9,6.2,6.2,6.1],
                'Stock_Index_Price': [1464,1394,1357,1293,1256,1254,1234,1195,1159,1167,1130,1075,1047,965,943,958,971,949,884,866,876,822,704,719]        
                }

df = DataFrame(Stock_Market,columns=['Year','Month','Interest_Rate','Unemployment_Rate','Stock_Index_Price']) 

print (df)

#Before you execute a linear regression model, it is
#advisable to validate that certain assumptions are met.

#As noted earlier, you may want to check that a linear relationship exists between the
#dependent variable and the independent variable/s.

#In our example, you may want to check that a linear relationship exists between:

#The Stock_Index_Price (dependent variable) and the Interest_Rate (independent variable); and
#The Stock_Index_Price (dependent variable) and the Unemployment_Rate (independent variable)
#To perform a quick linearity check, you can use scatter diagrams (utilizing the matplotlib library):

x=df['Interest_Rate']
y=df['Stock_Index_Price']
m,b=np.polyfit(x,y,1)
plt.scatter(df['Interest_Rate'], df['Stock_Index_Price'], color='red')
plt.title('Stock Index Price Vs Interest Rate', fontsize=14)
plt.xlabel('Interest Rate', fontsize=14)
plt.ylabel('Stock Index Price', fontsize=14)
plt.grid(True)
plt.plot(x,m*x+b)
plt.show()

x=df['Unemployment_Rate']
y=df['Stock_Index_Price']
m,b=np.polyfit(x,y,1)
plt.scatter(df['Unemployment_Rate'], df['Stock_Index_Price'], color='green')
plt.title('Stock Index Price  Vs Unemployment Rate', fontsize=14)
plt.xlabel('Unemployment Rate', fontsize=14)
plt.ylabel('Stock Index Price', fontsize=14)
plt.grid(True)
plt.plot(x,m*x+b)
plt.show()

plt.scatter(df['Interest_Rate'], df['Stock_Index_Price'], color='red')
plt.scatter(df['Unemployment_Rate'], df['Stock_Index_Price'], color='green')
plt.title('Stock Index Price Vs Interest Rate Vs Unemployment Rate', fontsize=14)
plt.xlabel('Interest Rate and Unemployment Rate', fontsize=14)
plt.ylabel('Stock Index Price', fontsize=14)
plt.grid(True)
plt.show()


X = df[['Interest_Rate','Unemployment_Rate']] # here we have 2 variables for multiple regression. If you just want to use one variable for simple linear regression, then use X = df['Interest_Rate'] for example.Alternatively, you may add additional variables within the brackets
Y = df['Stock_Index_Price']

# with sklearn
regr = linear_model.LinearRegression()
regr.fit(X, Y)

print('Intercept: \n', regr.intercept_)
print('Coefficients: \n', regr.coef_)
print('Y={0}+{1}X1+{2}X2'.format(regr.intercept_,regr.coef_[0],regr.coef_[1]))
fig = plt.figure()
#ax = plt.axes(projection='3d')
ax=plt.axes(projection='3d')
plt.show()
x1 = df['Interest_Rate']
x2=df['Unemployment_Rate']
y=df['Stock_Index_Price']
#ax.plot3D(x1,x2,y,'blue')
#ax.scatter3D(x1,x2,y,c=y,cmap='Greens')
plt.show()
# prediction with sklearn
New_Interest_Rate =2.75
New_Unemployment_Rate = 5.3
print ('Predicted Stock Index Price: \n', regr.predict([[New_Interest_Rate ,New_Unemployment_Rate]]))

# with statsmodels
X = sm.add_constant(X) # adding a constant
 
model = sm.OLS(Y, X).fit()
predictions = model.predict(X) 
 
print_model = model.summary()
print(print_model)

