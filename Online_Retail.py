import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv('Online_Retail.csv')
#Check sample data
data.head()
type(data)
data.info
data.shape
data.dtypes
data['InvoiceDate'] =  pd.to_datetime(data.InvoiceDate)
#Introduce new column for total
tot=data.Quantity*data.UnitPrice
data['total']=tot
n=sum(data['total'])/500000
print("n=",n)
#For Sales of Monthly 
sales_month=data.groupby(data.InvoiceDate.dt.month).sum()

plt.plot(sales_month.index,sales_month.total)
plt.bar(sales_month.index,sales_month.total)

#For Customer wise sales
cus_sales=data.groupby(data.CustomerID).sum()

cus_sales=cus_sales.sort_values(by='total')
cus_sales.head(10)
cus_sales.tail(10)

sales_country=data.groupby('Country').sum()
print(sales_country)
plt.bar(sales_country.index,sales_country.total,figsize=(6,6))
