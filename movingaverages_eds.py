# Moving Averages
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('EDS_Day_to_Day_Sales.csv')
print(df.head())
plt.scatter(df['BillDate'],df['Value'],color='red')
plt.plot(df['BillDate'],df['Value'])
plt.show()
year=df['BillDate']
sales=df['Value']
movavg=[10,20,30,40,50,60,70,80,90]
df=pd.DataFrame()
# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('moving_Average_eds.xlsx', engine='xlsxwriter')
#movavg=[30]
for k in range(len(movavg)):
    t=0
    c=len(year)-movavg[k]+1
    year1=[]
    sales1=[]
    for i in range(c):
        t=0
        v=i
        for l in range(movavg[k]):   #Add sales based on movavg(10,20,....)
            t=t+sales[v]
            v=v+1
        year1.append(i)
        year1[i]=year[i+1]
        sales1.append(i)
        sales1[i]=t/movavg[k]
        #t=(sales[i]+sales[i+1]+sales[i+2])/3
        print(" moving average {0} year {1}, value {2} ".format(movavg[k],i,t/movavg[k]))
    str1='mov'+str(movavg[k])
  # Write each dataframe to a different worksheet.
  #Work around Solution (use with caution): convert the list/array to a pandas Series,
  #and then when you do assignment, missing index in the Series will be filled with NaN:
    df[str1]=pd.Series([sales1])
  #  df.to_csv("moving_average_10.csv")
    df.to_excel(writer,sheet_name=str1)
    plt.scatter(year,sales,color='red')
    plt.plot(year,sales)
    plt.title("moving average for  " + str(movavg[k]) + "days")
    plt.scatter(year1,sales1,color='green')
    plt.plot(year1,sales1)
    plt.show()
# Close the Pandas Excel writer and output the Excel file.
writer.save()




