import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
# Compare the likelihood of the random samples to the two 
# distributions
def compare_data_to_dist(x, mu_1=5, mu_2=7,mu_3=6, sd_1=3, sd_2=3,sd_3=3):
    ll_1 = 0
    ll_2 = 0
    ll_3=0
    for i in x:
        print(i)
        ll_1 += np.log(stats.norm.pdf(i, mu_1, sd_1))
        ll_2 += np.log(stats.norm.pdf(i, mu_2, sd_2))
        ll_3 += np.log(stats.norm.pdf(i, mu_3, sd_3))
    
    print( "The LL of of x for mu: = {0} and sd = {1} is:{2}".format(mu_1, sd_1, ll_1))
    print( "The LL of of x for mu: = {0} and sd = {1} is: {2}" .format(mu_2, sd_2, ll_2))
    print( "The LL of of x for mu: = {0} and sd = {1} is: {2}" .format(mu_3, sd_3, ll_3))
    pdf=stats.norm.pdf(x,mu_1,sd_1)
    plt.plot(x, pdf,linewidth=3, color='r',label="mu1:"+ str(mu_1) + ",sd_1:" + str(sd_1)) # including h here is crucial
    pdf=stats.norm.pdf(x,mu_2,sd_2)
    plt.plot(x, pdf,linewidth=3, color='y',label="mu2:"+str(mu_2) +",sd_2:"+str(sd_2)) # including h here is crucial
    pdf=stats.norm.pdf(x,mu_3,sd_3)
    plt.plot(x, pdf,linewidth=3, color='g',label="mu3:"+str(mu_3) +",sd_3:"+str(sd_3))
    
    plt.legend()
    plt.show()



x=[2,3,4,5,6,7,8,9,10]
compare_data_to_dist(x)
