import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv("myc_taxi_distance_day_month_year_hr_min_sec.csv")
#Correlation
df4=df.corr()
print(df4)

#converting the categorical feature i.e bad or good into numerical feature 0 and 1
#from sklearn.preprocessing import LabelEncoder
#le=LabelEncoder()
#new_data=le.fit_transform(df['quality'])
#saving the new quality column in our orignal dataframe and checking its head
#df['quality']=new_data
#print(df.head())

from sklearn.model_selection import train_test_split
X=df.drop('trip_duration',axis=1)
y=df['trip_duration']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

#training different models and comparing the results
# K-nearest Neighbour
from sklearn.neighbors import KNeighborsClassifier
knc=KNeighborsClassifier()
knc.fit(X_train,y_train)
knc_prediction=knc.predict(X_test)

from sklearn.metrics import classification_report,accuracy_score
print('\t\t\tK-Nearest Neighbours\n\n',classification_report(y_test,knc_prediction))



