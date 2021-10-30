import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
#df=pd.read_csv('mobile_train.csv')
#df=pd.read_csv('winequality-red.csv')
df = pd.read_csv('winequality-white1.csv')
#df = pd.read_csv('Salaries1.csv')
#diabetes
#df=pd.read_csv('diabetes.csv')
#df=pd.read_csv('blood_sugar.csv')
#df=pd.read_csv('Online_Retail.csv')
df.describe()
#Filtering numerical data
df_numerics_only = df.select_dtypes(include=[np.number])
df_numerics_only
print(df_numerics_only.head())
df3=df_numerics_only.columns.values
print(len(df3))
fig=plt.figure(figsize=(10,10))
rows=2
cols=np.absolute(len(df3)/rows)+1
#probability distribution plot
for i in range(len(df3)):
    plt.subplot(rows,cols,i+1)
    sns.distplot(df[df3[i]],kde=True)

plt.show()
#Correlation
df4=df.corr()
print(df4)
# linear regression
from statsmodels.graphics.gofplots import qqplot
for i in range(len(df3)):
    qqplot(df[df3[i]], line='s')
    plt.xlabel(df3[i])
    plt.show()

#df5=df.groupby('quality').count()


#print(df5)
from scipy.stats import normaltest
from scipy.stats import shapiro
# normality test
for i in range(len(df3)):
    stat, p = normaltest(df[df3[i]])
   # stat,p=shapiro(df[df3[i]])
    print('Statistics=%.3f, p=%.3f' % (stat, p))
    # interpret
    alpha = 0.05
    if p>alpha:
        print("Accepted :",df3[i])
    else:
        print("Rejected :",df3[i])
#----------------------
# Complete Exploratory Analysis
#----------------------

df_describe=df.describe()
print(df_describe)

# anderson test for skewness and kurtosis
from scipy.stats import anderson

for i in range(len(df3)):
    result = anderson(df[df3[i]])
print('Statistic: %.3f' % result.statistic)
p = 0
for i in range(len(result.critical_values)):
	sl, cv = result.significance_level[i], result.critical_values[i]
	if result.statistic < result.critical_values[i]:
		print('%.3f: %.3f, data looks normal (fail to reject H0)' % (sl, cv))
	else:
		print('%.3f: %.3f, data does not look normal (reject H0)' % (sl, cv))


#Kolomogrov smniov test
from scipy.stats import kstest 
for i in range(len(df3)):
    result = kstest(df[df3[i]], "norm")    
    print("KStest {0}, {1} ".format(df3[i],result))


#converting the categorical feature i.e bad or good into numerical feature 0 and 1
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
new_data=le.fit_transform(df['quality'])
#saving the new quality column in our orignal dataframe and checking its head
df['quality']=new_data
print(df.head())

from sklearn.model_selection import train_test_split
X=df.drop('quality',axis=1)
y=df['quality']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

#Import Gaussian Naive Bayes model
from sklearn.naive_bayes import GaussianNB

#Create a Gaussian Classifier
gnb = GaussianNB()

#Train the model using the training sets
gnb.fit(X_train, y_train)

#Predict the response for test dataset
y_pred = gnb.predict(X_test)
print(y_pred)
#Evaluating Model
#After model generation, check the accuracy using actual and predicted values.

#Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics

# Model Accuracy, how often is the classifier correct?
print("Accuracy of Bayesian:",metrics.accuracy_score(y_test, y_pred))


#training different models and comparing the results
# K-nearest Neighbour
from sklearn.neighbors import KNeighborsClassifier
knc=KNeighborsClassifier()
knc.fit(X_train,y_train)
knc_prediction=knc.predict(X_test)

from sklearn.metrics import classification_report,accuracy_score
print('\t\t\tK-Nearest Neighbours\n\n',classification_report(y_test,knc_prediction))

# Decision Tree and Random Forest
from sklearn.tree import DecisionTreeClassifier
dtc=DecisionTreeClassifier()
dtc.fit(X_train,y_train)

dtc_prediction=dtc.predict(X_test)
from sklearn.ensemble import RandomForestClassifier
rfc=RandomForestClassifier(n_estimators=200)
rfc.fit(X_train,y_train)

rfc_predictions=rfc.predict(X_test)
#Support Vector Machine
from sklearn.svm import SVC
svc=SVC()
svc.fit(X_train,y_train)

svc_predictions=svc.predict(X_test)
#from sklearn.grid_search import GridSearchCV
from sklearn.model_selection import GridSearchCV
#for getting the best parameters in out model
grid=GridSearchCV(SVC(),param_grid={'C':[0.1,1,10,100,1000],'gamma':[1,0.1,0.001,0.0001]},verbose=3)
grid.fit(X_train,y_train)

#checking the best parameters for our model
grid.best_params_
#Using the best parameters in our model
grid.best_estimator_

grid_predictions=grid.predict(X_test)
#Comparing the Predictions and Accuracy of our models
from sklearn.metrics import classification_report,accuracy_score
print('\t\t\tK-Nearest Neighbours\n\n',classification_report(y_test,knc_prediction))

print('\n\n\t\t\tDecision Tree\n\n',classification_report(y_test,dtc_prediction))

print('\n\n\t\t\tRandom Forest\n\n',classification_report(y_test,rfc_predictions))

print('\n\n\t\t\tSupport Vector Machine\n\n',classification_report(y_test,svc_predictions))

print('\n\n\t\t\tSVM With GridSearch\n\n',classification_report(y_test,grid_predictions))




