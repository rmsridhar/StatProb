 #Assigning features and label variables
outlook=['sunny','sunny','overcast','rain','rain','rain','overcast','sunny','sunny','rain','sunny','overcast','overcast','rain']
humidity=['high','high','high','high','normal','normal','normal','high','normal','normal','normal','high','normal','high']
wind=['weak','strong','weak','weak','weak','strong','strong','weak','weak','weak','strong','strong','weak','strong']
play=['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes','Yes','No']
#play=[0,0,1,1,1,0,1,0,1,1,1,1,1,0]
from sklearn import preprocessing
#creating labelEncoder
le = preprocessing.LabelEncoder()
# Converting string labels into numbers.
outlook_encoded=le.fit_transform(outlook)
print (outlook_encoded)

humidity_encoded=le.fit_transform(humidity)
wind_encoded=le.fit_transform(wind)
play_encoded=le.fit_transform(play)
#Combinig weather and temp into single listof tuples
features=list(zip(outlook_encoded,humidity_encoded,wind_encoded))
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
model.fit(features,play_encoded)

#Predict Output # Rain,High, Weak
predicted= model.predict([[0,0,1]]) 
print ("Predicted Value:", predicted)

if (predicted==1):
    print("play")
else:
    print("Not play")
