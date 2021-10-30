# A Python program to print all  
# permutations using library function 
from itertools import permutations 
from itertools import combinations  
# Get all permutations of [1, 2, 3] 
#perm = permutations([1, 2, 3,4]) 
#perm = permutations(['A', 'B', 'C','D']) 
#perm=permutations(['A','B','C','D','E'])
#perm=permutations([1,2,3,4,5,6,7,8,9,10,11])
# Print the obtained permutations 
#for i in list(perm): 
#    print (i)
count1=0
comb=combinations([1,2,3,4,5,6,7,8,9,10,11],4)
for i in list(comb):
    print(i)
    count1=count1+1
print(count1)
