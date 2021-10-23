
from sklearn import preprocessing
 #Assigning features and label variables
weather=['Sunny','Sunny','Overcast','Rainy','Rainy','Rainy','Overcast','Sunny','Sunny',
'Rainy','Sunny','Overcast','Overcast','Rainy']
temp=['Hot','Hot','Hot','Mild','Cool','Cool','Cool','Mild','Cool','Mild','Mild','Mild',
      'Hot','Mild']

#play=['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes','Yes','No']
play=[0,0,1,1,1,0,1,0,1,1,1,1,1,0]

#creating labelEncoder
le = preprocessing.LabelEncoder()
# Converting string labels into numbers.
wheather_encoded=le.fit_transform(weather)
print (wheather_encoded)

temp_encoded=le.fit_transform(temp)
label=le.fit_transform(play)
print ("temp:",temp_encoded)
print ("Play:",label)


#Combinig weather and temp into single listof tuples
features=list(zip(wheather_encoded,temp_encoded))
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
model.fit(features,label)

#Predict Output
predicted= model.predict([[0,2]]) # 0:Overcast, 2:Mild
print ("Predicted Value:", predicted)

if (predicted==1):
    print("Play")
else:
    print("Not Play")
