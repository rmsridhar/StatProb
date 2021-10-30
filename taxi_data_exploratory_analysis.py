import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
#df=pd.read_csv('mobile_train.csv')
#df=pd.read_csv('winequality-red.csv')
#df=pd.read_csv("myc_taxi_distance_day_month_year_hr_min_sec.csv")
df= pd.read_csv("taxi_data.csv")
print(df.isnull().sum())
#Correlation
df4=df.corr()
print(df4)

#df5=df.groupby('quality').count()



from sklearn.model_selection import train_test_split
X=df.drop('trip_duration',axis=1)
y=df['trip_duration']
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




