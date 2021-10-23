#Loading Data
#Let's first load the required wine dataset from scikit-learn datasets.

#Import scikit-learn dataset library

import csv
import pandas as pd
filename = 'wine_data1.csv'
wine1=pd.read_csv(filename)
print(wine1.head(10))

# print data(feature)shape
print(wine1.shape)

# print the wine data features
#print (wine[0:5])
Y=wine1.iloc[:,13] # target variable
X=wine1.iloc[:,0:13]# independent variables
print(Y)
print(X)
from sklearn.model_selection import train_test_split
# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, Y,
                                                    test_size=0.3,random_state=177) # 70% training and 30% test



#Model Generation
#After splitting, you will generate a random forest model on the training set
#and perform prediction on test set features.

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
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

#predicted= gnb.predict([[14.23,1.71,2.43,15.6,127,2.8,3.06,0.28,2.29,5.64,1.04,3.92,1065]]) # L1,L2,L3....L13
#print ("Predicted Value:", predicted)
