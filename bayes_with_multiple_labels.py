#Loading Data
#Let's first load the required wine dataset from scikit-learn datasets.

#Import scikit-learn dataset library
from sklearn import datasets

#Load dataset
wine = datasets.load_wine()

#Exploring Data
#You can print the target and feature names, to make sure you have the
#right dataset, as such:

# print the names of the 13 features
print ("Features: ", wine.feature_names)

# print the label type of wine(class_0, class_1, class_2)
print ("Labels: ", wine.target_names)

# print data(feature)shape
print(wine.data.shape)



# print the wine labels (0:Class_0, 1:class_2, 2:class_2)
print (wine.target)

#Splitting Data
#First, you separate the columns into dependent and
#independent variables(or features and label).
#Then you split those variables into train and test set.

# Import train_test_split function
#from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split
# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(wine.data, wine.target,
                                                    test_size=0.3,random_state=178) # 70% training and 30% test


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

