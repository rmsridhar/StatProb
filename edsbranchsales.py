#Context
# Easy Design problem for data analysis to predict next day sales

import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

# fEATURE SELECTION
#data = pd.read_csv("mobile_train.csv")
#data=pd.read_csv("winequality-red.csv")
data=pd.read_csv("EDS Branch.csv")
df1=data['Value'].sum()
df_month_days=data.groupby(['Month','Days'])['Value'].sum()
df_month=data.groupby(['Month'])['Value'].sum()
df_year_month_days=data.groupby(['Year','Month','Days'])['Value'].sum()
df_year_month_date=data.groupby(['Year','Month','Date'])['Value'].sum()
print(df_month_days)
print(df_year_month_days.corr())

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('edsreport.xlsx', engine='xlsxwriter')

# Write each dataframe to a different worksheet.
df_month.to_excel(writer,sheet_name='Monthly Sales')
df_month_days.to_excel(writer, sheet_name='Monthly Day wise Sales')
df_year_month_days.to_excel(writer,sheet_name='Yearly_Monthly_Day wise sales')
df_year_month_date.to_excel(writer,sheet_name='Yearly_Monthly_Date wise sales')




# Close the Pandas Excel writer and output the Excel file.
writer.save()
