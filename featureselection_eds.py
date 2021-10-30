#In this problem you do not have to predict actual price but a price range
#indicating how high the price is
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import mutual_info_regression

# fEATURE SELECTION
df_data=pd.read_csv("EDS Branch.csv")
from sklearn import preprocessing
#creating labelEncoder
le = preprocessing.LabelEncoder()
# Converting string labels into numbers.
df_data['Days']=le.fit_transform(df_data['Days'])
df_data['SubgroupName']=le.fit_transform(df_data['SubgroupName'])
df_data['DineGroupName']=le.fit_transform(df_data['DineGroupName'])
df_data['ShiftName']=le.fit_transform(df_data['ShiftName'])
df_x=df_data.drop(['Createddate','Hours','Value','BillDate','ItemName','BranchName','HallName'],axis=1)
df_y=df_data['Value']
#apply SelectKBest class to extract top 10 best features
bestfeatures = SelectKBest(score_func=chi2, k=10)
fit = bestfeatures.fit(df_x,df_y)
#dfscores = pd.DataFrame(fit.scores_)
#dfcolumns = pd.DataFrame(df_x.columns)
#concat two dataframes for better visualization 
#featureScores = pd.concat([dfcolumns,dfscores],axis=1)
#featureScores.columns = ['Specs','Score']  #naming the dataframe columns
#featureScores.to_excel("feature_mobile_train.xlsx",sheet_name="features")
#print(featureScores.nlargest(10,'Score'))  #print 10 best features


# Create a Pandas Excel writer using XlsxWriter as the engine.
#writer = pd.ExcelWriter('eds_feature_selection.xlsx', engine='xlsxwriter')

# Write each dataframe to a different worksheet.
#df_x.to_excel(writer, sheet_name='Feature Selection')
#print('Completed')


