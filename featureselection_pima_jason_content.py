#Context
#Bob has started his own mobile company. He wants to give tough fight to big companies like Apple,
#Samsung etc.

#Feature selection is a process where you automatically
#select those features in your data that contribute most to the prediction variable or
#output in which you are interested.

#Having irrelevant features in your data can decrease the accuracy of many models,
#especially linear algorithms like linear and logistic regression.

#Three benefits of performing feature selection before modeling your data are:

#Reduces Overfitting: Less redundant data means less opportunity to make decisions based on noise.
#Improves Accuracy: Less misleading data means modeling accuracy improves.
#Reduces Training Time: Less data means that algorithms train faster.

import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

# fEATURE SELECTION
data=pd.read_csv("diabetes.csv")
X = data.drop(["Outcome"],axis=1)  #independent columns
y = data["Outcome"]    #target column i.e price range
#apply SelectKBest class to extract top 10 best features
bestfeatures = SelectKBest(score_func=chi2, k='all')
fit = bestfeatures.fit(X,y)
dfscores = pd.DataFrame(fit.scores_)
dfcolumns = pd.DataFrame(X.columns)
#concat two dataframes for better visualization 
featureScores = pd.concat([dfcolumns,dfscores],axis=1)
featureScores.columns = ['Specs','Score']  #naming the dataframe columns
#featureScores.to_excel("feature_mobile_train.xlsx",sheet_name="features")
print(featureScores.nlargest(10,'Score'))  #print 10 best features

