# Import libraries
import matplotlib.pyplot as plt
import numpy as np


# Creating dataset
np.random.seed(10)
#data = np.random.normal(100, 20, 200)
#data=[186, 176, 158, 180, 186, 168, 168, 164, 178, 170, 189, 195, 172,
#     187, 180, 186, 185, 168, 179, 178, 183, 179, 170, 175, 186, 159,
#     161, 178, 175, 185, 175, 162, 173, 172, 177, 175, 172, 177, 180,30,500]
data=[186, 176, 158, 180, 186, 168, 168, 164, 178, 170, 189, 195, 172,
     187, 180, 186, 185, 168, 179, 178, 183, 179, 170, 175, 186, 159,
     161, 178, 175, 185, 175, 162, 173, 172, 177, 175, 172, 177, 180,30,500,425,450]
print(data)
fig = plt.figure(figsize =(10, 7))

# Creating plot
plt.boxplot(data)

# show plot
plt.show()
