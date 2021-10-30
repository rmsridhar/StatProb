import numpy as np
from keras.models import Sequential
from keras.layers import InputLayer, Dense
from keras.optimizers import SGD
X = np.matrix('1,2;3,2')
y = np.matrix('0;1')
sgd = SGD(lr=0.1)
model = Sequential()
model.add(InputLayer(input_shape=(2,)))
model.add(Dense(units=2, kernel_initializer='random_uniform', activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer=sgd, metrics=['accuracy'])
model.fit(X,y, epochs=20)

