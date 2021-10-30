# Moving Averages
import matplotlib.pyplot as plt
year=[2003,2004,2005,2006,2007,2008,2009,2010,2011]
sales=[4,5,6,5,6,8,9,11,10]
plt.scatter(year,sales,color='red')
plt.plot(year,sales)
plt.show()
movavg=[2,3,4]
#movavg=[3]
for k in range(len(movavg)):
    t=0
    c=len(year)-movavg[k]+1
    year1=[]
    sales1=[]
    for i in range(c):
        t=0
        v=i
        for l in range(movavg[k]):
            t=t+sales[v]
            v=v+1
        year1.append(i)
        year1[i]=year[i+1]
        sales1.append(i)
        sales1[i]=t/movavg[k]
        #t=(sales[i]+sales[i+1]+sales[i+2])/3
        print(" moving average {0} year {1}, value {2} ".format(movavg[k],i,t/movavg[k]))
    plt.scatter(year,sales,color='red')
    plt.plot(year,sales)
   # plt.title("moving average for " + k + "years")
    plt.scatter(year1,sales1,color='green')
    plt.plot(year1,sales1)
    plt.show()
