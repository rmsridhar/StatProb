from pandas import DataFrame
import matplotlib.pyplot as plt
from sklearn import linear_model
import statsmodels.api as sm
from mpl_toolkits import mplot3d
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import seaborn as sns
import numpy as np
import pandas as pd
from scipy import stats

data={'x':[1100,1400,1425,1550,1600,1700,1700,1875,2350,2450],
'y':[199000,245000,319000,240000,312000,279000,310000,308000,405000,324000]}
df=pd.DataFrame(data)
print(df)
#linear regression equation
m,b=np.polyfit(df['x'],df['y'],1)
print("m={0},b={1}".format(m,b))
plt.scatter(df['x'],df['y'], color='red')
plt.title('Houses in Sq.Ft Vs Price', fontsize=14)
plt.xlabel('Houses in Sq.Ft', fontsize=14)
plt.ylabel('Price', fontsize=14)
plt.grid(True)
plt.plot(df['x'],m*df['x']+b)
plt.show()

X=df[['x']]
Y=df[['y']]
# with sklearn
regr = linear_model.LinearRegression()
regr.fit(X,Y)

print('Intercept: \n', regr.intercept_)
print('Coefficients: \n', regr.coef_)
print('Y={0}+{1}X1'.format(regr.intercept_,regr.coef_[0]))
plt.scatter(X,Y)
plt.plot(X,regr.intercept_+regr.coef_[0]*X)
plt.show()

#print("Linear regression of SKLearn",regr.predict(1600))
# with statsmodels
X = sm.add_constant(X) # adding a constant
 
model = sm.OLS(Y,X).fit()
predictions = model.predict(X)
 
print_model = model.summary()
print(print_model)
#Gradient Descent
# transform data suiting to <1 for processing purpose
maxX=max(df['x'])
minxX=min(df['x'])
maxY=max(df['y'])
minY=min(df['y'])
X=df['x']
Y=df['y']
print()
print("X={0},Y={1}".format(df['x'],df['y']))
df_x=[]
df_y=[]
for i in range(len(X)):
    t1=(X[i]-minxX)/(maxX-minxX)
    t2=(Y[i]-minY)/(maxY-minY)
    df_x.append(t1)
    df_y.append(t2)
#transformed data in df_x,df_y
df_join={'x':df_x,'y':df_y}
df1=pd.DataFrame(df_join,columns=['x','y'])
print(df1)

a=0.45
b=0.75
print(df_y)

for k in range(25):
    yp=[]
    sse=[]
    dsse_da=[]
    dsse_db=[]
    for i in range(len(X)):
        yp.append(i)
        yp[i]=a+b*df_x[i]
        sse.append(i)
        sse[i]=pow(df_y[i]-yp[i],2) * 0.5
        dsse_da.append(i)
        dsse_db.append(i)
        dsse_da[i]=-1*(df_y[i]-yp[i])
        dsse_db[i]=-1*(df_y[i]-yp[i])*df_x[i]
    df_join={'x':df_x,'y':df_y,'yp':yp,'sse':sse,'dsse_da':dsse_da,'dsse_db':dsse_db}
    df1=pd.DataFrame(df_join,columns=['x','y','yp','sse','dsse_da','dsse_db'])
    print(df1)
    print("Converge={0}:".format(df1['sse'].sum()))
    r=0.01
    a=a-r*df1['dsse_da'].sum()
    b=b-r*df1['dsse_db'].sum()
    print("a={0},b={1}".format(a,b))
# plot gradient descent
plt.scatter(X,Y,color='red')
plt.plot(X,(a+b*(X-minxX)/(maxX-minxX))*(maxY-minY)+minY,label="Gradient Descent")
plt.plot(X,regr.intercept_+regr.coef_[0]*X,label="Linear")
plt.legend()
plt.show()

#finding the root mean square error
error = mean_squared_error(Y, regr.intercept_+regr.coef_[0]*X)
print("Root Mean Squared Error of SKLearn",np.sqrt(error))
error = mean_squared_error(Y, (a+b*(X-minxX)/(maxX-minxX))*(maxY-minY)+minY)
print("Root Mean Squared Error of Gradient descent",np.sqrt(error))

#R Squared
print("R Squared SKlearn",pow(np.corrcoef(Y, regr.intercept_+regr.coef_[0]*X),2))

print("R Squared Gradient Descent",pow(np.corrcoef(Y, (a+b*(X-minxX)/(maxX-minxX))*(maxY-minY)+minY),2))

#predict y value for x
print("Predict the value for 2350 Sq Ft")
x=2350
y=(a+b*(x-minxX)/(maxX-minxX))*(maxY-minY)+minY
print("Gradient Descent",y)
print("Linear regression of SKLearn",regr.predict([[x]]))
# linear regress equation using stats linregress slope,intercept, r-value,p-value are exhibited
print("intercept,slope,p-value.....")
slope, intercept, r_value, p_value, std_err = stats.linregress(X,Y)
print("Slope {0},Intercept {1},r_value {2}, p_value {3}, std_err {4}",slope,intercept,r_value,p_value,std_err)
# linear regression equation using gradient descent
slope, intercept, r_value, p_value, std_err = stats.linregress(df_x,df_y)
print("Slope {0},Intercept {1},r_value {2}, p_value {3}, std_err {4}",slope,intercept,r_value,p_value,std_err)

#polynomial of degree 2 regression equation
plt.xlabel('Sq.Feet')
plt.ylabel('Cost')
plt.title('Scatterplot of Sq.Feet vs Cost of degree 2')
p = np.poly1d(np.polyfit(X,Y,2))
plt.plot(X,p(X))
plt.scatter(X,Y)
plt.show()

#polynomial of degree 3 regression equation
plt.xlabel('Sq.Feet')
plt.ylabel('Cost')
plt.title('Scatterplot of Sq.Feet vs Cost of degree 3')
p = np.poly1d(np.polyfit(X,Y,3))
plt.plot(X,p(X))
plt.scatter(X,Y)
plt.show()

#polynomial of degree 2,3,4,5,6 curve
plt.xlabel('Sq.Feet')
plt.ylabel('Cost')
plt.title('Scatterplot of Sq.Feet vs Cost')
p1=np.poly1d(np.polyfit(X,Y,1))
plt.plot(X,p1(X),label="1st Degree")
p2 = np.poly1d(np.polyfit(X,Y,2))
plt.plot(X,p2(X),label="2nd Degree")
p3 = np.poly1d(np.polyfit(X,Y,3))
plt.plot(X,p3(X),label="3rd  Degree")
p4 = np.poly1d(np.polyfit(X,Y,4))
plt.plot(X,p4(X),label="4th  Degree")
p5 = np.poly1d(np.polyfit(X,Y,5))
plt.plot(X,p5(X),label="5th  Degree")
p6 = np.poly1d(np.polyfit(X,Y,6))
plt.plot(X,p6(X),label="6th  Degree")
plt.legend()
plt.scatter(X,Y)
plt.show()

#R2_score i.e., correlation between X and Y for 1,2,3,4,5,6
print("R2 Score - 1 Degree",r2_score(Y,p1(X)))
print("R2 Score - 2 Degree",r2_score(Y,p2(X)))
print("R2 Score - 3 Degree",r2_score(Y,p3(X)))
print("R2 Score - 4 Degree",r2_score(Y,p4(X)))
print("R2 Score - 5 Degree",r2_score(Y,p5(X)))
print("R2 Score - 6 Degree",r2_score(Y,p6(X)))

#4th degree equation is better
plt.xlabel('Sq.Feet')
plt.ylabel('Cost')
plt.title('Scatterplot of Sq.Feet vs Cost')
p4 = np.poly1d(np.polyfit(X,Y,4))
plt.plot(X,p4(X),label="4th  Degree")
plt.legend()
plt.scatter(X,Y)
plt.show()

#LassoCV

reg = LassoCV()
reg.fit(X, y)
print("Best alpha using built-in LassoCV: %f" % reg.alpha_)
print("Best score using built-in LassoCV: %f" %reg.score(X,y))
coef = pd.Series(reg.coef_, index = X.columns)

print("Lasso picked " + str(sum(coef != 0)) + " variables and eliminated the other " +  str(sum(coef == 0)) + " variables")



