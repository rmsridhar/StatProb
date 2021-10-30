
# create a regression dataset with outliers
# Robust regression

from random import random
from random import randint
from random import seed
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedKFold
from matplotlib import pyplot
import numpy as np
 
# prepare the dataset
def get_dataset():
	X, y = make_regression(n_samples=100, n_features=1, tail_strength=0.9, effective_rank=1, n_informative=1, noise=3, bias=50, random_state=1)
	# add some artificial outliers
	seed(1)
	for i in range(10):
		factor = randint(2, 4)
		if random() > 0.5:
			X[i] += factor * X.std()
		else:
			X[i] -= factor * X.std()
	return X, y


# load dataset
X, y = get_dataset()
# summarize shape
print(X.shape, y.shape)
# scatter plot of input vs output
pyplot.scatter(X, y)
pyplot.show()
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size =  
                                                1/3, random_state = 0)

# define the linear regresssion model
model = LinearRegression()
# evaluate model
model.fit(X_train, y_train)

# Predicting the Test set results
y_pred = model.predict(X_test)

# Visualising the Training set results
pyplot.scatter(X_train, y_train, color = 'blue')
pyplot.plot(X_train, model.predict(X_train), color = 'red')
pyplot.show()

# Visualising the Test set results
#pyplot.scatter(X_test, y_test, color = 'blue')
#pyplot.plot(X_test, model.predict(X_test), color = 'red')
#pyplot.show()

from sklearn import metrics
print("Linear Regression")
print("MAE",metrics.mean_absolute_error(y_test,y_pred))
print("Mean Squared Error",metrics.mean_squared_error(y_test,y_pred))
print("Root Mean Squared Error",np.sqrt(metrics.mean_squared_error(y_test,y_pred)))

# define the Huber Regressor model
from sklearn.linear_model import HuberRegressor
model = HuberRegressor()
# evaluate model
model.fit(X_train, y_train)

# Predicting the Test set results
y_pred = model.predict(X_test)

# Visualising the Training set results
pyplot.scatter(X_train, y_train, color = 'blue')
pyplot.plot(X_train, model.predict(X_train), color = 'red')
pyplot.show()

# Visualising the Test set results
#pyplot.scatter(X_test, y_test, color = 'blue')
#pyplot.plot(X_test, model.predict(X_test), color = 'red')
#pyplot.show()

from sklearn import metrics
print("HuberRegression")
print("MAE",metrics.mean_absolute_error(y_test,y_pred))
print("Mean Squared Error",metrics.mean_squared_error(y_test,y_pred))
print("Root Mean Squared Error",np.sqrt(metrics.mean_squared_error(y_test,y_pred)))

# define the RANSAC Regressor model
from sklearn.linear_model import RANSACRegressor
model = RANSACRegressor()
# evaluate model
model.fit(X_train, y_train)

# evaluate model
model.fit(X_train, y_train)

# Predicting the Test set results
y_pred = model.predict(X_test)

# Visualising the Training set results
pyplot.scatter(X_train, y_train, color = 'blue')
pyplot.plot(X_train, model.predict(X_train), color = 'red')
pyplot.show()

# Visualising the Test set results
#pyplot.scatter(X_test, y_test, color = 'blue')
#pyplot.plot(X_test, model.predict(X_test), color = 'red')
#pyplot.show()

from sklearn import metrics
print("RANSAC Regression")
print("MAE",metrics.mean_absolute_error(y_test,y_pred))
print("Mean Squared Error",metrics.mean_squared_error(y_test,y_pred))
print("Root Mean Squared Error",np.sqrt(metrics.mean_squared_error(y_test,y_pred)))


# define the RANSAC Regressor model
from sklearn.linear_model import TheilSenRegressor
model = TheilSenRegressor()
# evaluate model
model.fit(X_train, y_train)

# evaluate model
model.fit(X_train, y_train)

# Predicting the Test set results
y_pred = model.predict(X_test)

# Visualising the Training set results
pyplot.scatter(X_train, y_train, color = 'blue')
pyplot.plot(X_train, model.predict(X_train), color = 'red')
pyplot.show()

# Visualising the Test set results
#pyplot.scatter(X_test, y_test, color = 'blue')
#pyplot.plot(X_test, model.predict(X_test), color = 'red')
#pyplot.show()

from sklearn import metrics
print("TheilSen Regression")
print("MAE",metrics.mean_absolute_error(y_test,y_pred))
print("Mean Squared Error",metrics.mean_squared_error(y_test,y_pred))
print("Root Mean Squared Error",np.sqrt(metrics.mean_squared_error(y_test,y_pred)))
