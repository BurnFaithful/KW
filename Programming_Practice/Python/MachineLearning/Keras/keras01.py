from keras.models import Sequential
from keras.layers import Dense

import numpy as np

# Data Value
x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 2, 3, 4, 5])

#model node, layer
model = Sequential()
model.add(Dense(5, input_dim=1, activation='relu'))
model.add(Dense(3))
model.add(Dense(1))

model.compile(loss='mse', optimizer='adam')
model.fit(x, y, epochs=100, batch_size=1)

mse = model.evaluate(x, y, batch_size=1) # mean squared error
print("mse :", mse)
