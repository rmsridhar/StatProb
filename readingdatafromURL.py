# the Pima Indians diabetes dataset from CSV URLPython
# Load the Pima Indians diabetes dataset from CSV URL
import numpy as np
import urllib.request as url
# URL for the Pima Indians Diabetes dataset (UCI Machine Learning Repository)
url1 = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
# download the file
#raw_data = url
#import urllib.request as ur
#s = ur.urlopen("http://www.google.com")
#s = ur.urlopen(url1)
#sl = s.read()
#print(sl)
# load the CSV file as a numpy matrix
dataset = np.loadtxt("diabetes.csv", delimiter=",")
print(dataset.shape)
# separate the data from the target attributes
X = dataset[:,0:7]
y = dataset[:,8]

