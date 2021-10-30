#Context
#Bob has started his own mobile company. He wants to give tough fight to big companies like Apple,
#Samsung etc.

#He does not know how to estimate price of mobiles his company creates.
#In this competitive mobile phone market you cannot simply assume things.
#To solve this problem he collects sales data of mobile phones of various companies.

#Bob wants to find out some relation between features of a mobile phone
#(eg:- RAM,Internal Memory etc) and its selling price. But he is not so good
#at Machine Learning. So he needs your help to solve this problem.

#In this problem you do not have to predict actual price but a price range
#indicating how high the price is
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

# fEATURE SELECTION
data = pd.read_csv("mobile_train.csv")
#data=pd.read_csv("winequality-red.csv")
#data=pd.read_csv("diabetes.csv")
#data=pd.read_csv("pima-indians-diabetes_data.csv")
X = data.iloc[:,0:20]  #independent columns
y = data.iloc[:,-1]    #target column i.e price range
#X = data.iloc[:,0:6]  #independent columns of diabetes
#y = data.iloc[:,7]    #target column of diabetes
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

#FEATURE IMPORTANCE
import pandas as pd
import numpy as np
#data = pd.read_csv("D://Blogs//train.csv")
X = data.iloc[:,0:20]  #independent columns
y = data.iloc[:,-1]    #target column i.e price range
from sklearn.ensemble import ExtraTreesClassifier
import matplotlib.pyplot as plt
model = ExtraTreesClassifier()
model.fit(X,y)
print(model.feature_importances_) #use inbuilt class feature_importances of tree based classifiers
#plot graph of feature importances for better visualization
feat_importances = pd.Series(model.feature_importances_, index=X.columns)
#feat_importances.to_excel("feature_mobile_train.xlsx",sheet_name="features_important")
feat_importances.nlargest(10).plot(kind='barh')
plt.show()


#Correlation
import pandas as pd
import numpy as np
import seaborn as sns
X = data.iloc[:,0:20]  #independent columns
y = data.iloc[:,-1]    #target column i.e price range
#get correlations of each features in dataset
corrmat = data.corr()
top_corr_features = corrmat.index
plt.figure(figsize=(20,20))
#plot heat map
g=sns.heatmap(data[top_corr_features].corr(),annot=True,cmap="RdYlGn")
plt.show()

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('pandas_multiple.xlsx', engine='xlsxwriter')

# Write each dataframe to a different worksheet.
featureScores.to_excel(writer, sheet_name='Feature Selection')
feat_importances.to_excel(writer, sheet_name='Feature Importance')
corrmat.to_excel(writer, sheet_name='Correlation')

# Close the Pandas Excel writer and output the Excel file.
writer.save()
