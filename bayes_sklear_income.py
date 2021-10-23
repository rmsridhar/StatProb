 #Assigning features and label variables
Refund=['yes','no','no','yes','no','no','yes','no','no','no']
Martial=['Single','Married','Single','Married','Divorced','Married','Divorced','Single','Married','Single']
Income=[125,100,70,120,95,60,220,85,75,90]
Evade=['No','No','No','No','Yes','No','No','Yes','No','Yes']
#play=[0,0,1,1,1,0,1,0,1,1,1,1,1,0]
from sklearn import preprocessing
#creating labelEncoder
le = preprocessing.LabelEncoder()
# Converting string labels into numbers.
Refund_encoded=le.fit_transform(Refund)
print (Refund_encoded)

Martial_encoded=le.fit_transform(Martial)
#Tax_encoded=le.fit(Tax)
Evade_encoded=le.fit_transform(Evade)
print(Martial_encoded)
print(Income)
#Combinig weather and temp into single listof tuples
features=list(zip(Refund_encoded,Martial_encoded,Income))
print(features)

#Generate a model using naive bayes classifier in the following steps:

#Create naive bayes classifier
#Fit the dataset on classifier
#Perform prediction

#Import Gaussian Naive Bayes model
from sklearn.naive_bayes import GaussianNB

#Create a Gaussian Classifier
model = GaussianNB()

# Train the model using the training sets
model.fit(features,Evade_encoded)

#Predict Output
predicted= model.predict([[0,1,120]]) # Refund:No, Martial:Married,Tax=120
print ("Predicted Value:", predicted)

if (predicted==1):
    print("Evade Tax")
else:
    print("Not Evade Tax")
