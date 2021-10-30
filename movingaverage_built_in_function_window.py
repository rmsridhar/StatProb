# Import pandas
import pandas as pd
import matplotlib.pyplot as plt
# Create data
#data = {'score': [1,1,1,2,2,2,3,3,3]}
df = pd.read_csv('EDS_Day_to_Day_Sales.csv')
# Create dataframe
#df = pd.DataFrame(data)
sales=df['Value']
# View dataframe
#print(sales)
df1=pd.DataFrame(sales)
df2=pd.DataFrame(sales)
df3=pd.DataFrame(sales)
df4=pd.DataFrame(sales)
df5=pd.DataFrame(sales)
df6=pd.DataFrame(sales)
df7=pd.DataFrame(sales)
# Calculate the moving average. That is, take
# the first two values, average them, 
# then drop the first and add the third, etc.
#for i in range(0,90,10):
#    print("Moving average for = ",i)
#    print(df1.rolling(window=i).mean())
df1['5days']=df1.rolling(5).mean()
df2['10days']=df2.rolling(10).mean()
df3['15days']=df3.rolling(15).mean()
df4['20days']=df4.rolling(20).mean()
df5['25days']=df5.rolling(25).mean()
df6['30days']=df6.rolling(30).mean()
df7['40days']=df7.rolling(40).mean()

print(" sales average= {0}, 5 Days moving average={1}, difference={2}".format(sales.mean,df1['5days'].mean(),sales.mean()-df1['5days'].mean()))
print("10 Days Average",sales.mean()-df2['10days'].mean())
print("15 Days Average",sales.mean()-df3['15days'].mean())
print("20 Days Average",sales.mean()-df4['20days'].mean())
print("25 Days Average",sales.mean()-df5['25days'].mean())
print("30 Days Average",sales.mean()-df6['30days'].mean())
print("40 Days Average",sales.mean()-df7['40days'].mean())


plt.plot(df['BillDate'],df['Value'],label='Actual')

plt.plot(df['BillDate'],df1['5days'],label='5 days')

plt.plot(df['BillDate'],df2['10days'],label='10 days')
plt.plot(df['BillDate'],df3['15days'],label='15 days')
plt.plot(df['BillDate'],df4['20days'],label='20 days')
plt.plot(df['BillDate'],df5['25days'],label='25 days')
plt.plot(df['BillDate'],df6['30days'],label='30 days')
plt.plot(df['BillDate'],df7['40days'],label='40 days')
plt.legend()
plt.show()


