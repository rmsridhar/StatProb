# A Python program to print all  
# permutations using library function 
from itertools import permutations 
  
# Get all permutations of [1, 2, 3] 
#perm = permutations([1, 2, 3]) 
val=int(input("enter the value"))
l = list(permutations(range(1, val))) 
print(l)
# Print the obtained permutations 
#for i in list(perm): 
#    print(i) 
