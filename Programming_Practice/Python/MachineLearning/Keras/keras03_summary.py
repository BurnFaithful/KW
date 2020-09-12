from keras.models import Sequential
from keras.layers import Dense

import numpy as np

x = np.array([x for x in range(1, 11)])
y = np.array([x for x in range(1, 11)])
x2 = np.array([11, 12, 13, 14, 15])


model = Sequential()
model.add(Dense(100, input_dim=1, activation='relu'))
model.add(Dense(230))
model.add(Dense(170))
model.add(Dense(320))
model.add(Dense(1))

model.summary()

'''
model.compile(loss='mse', optimizer='adam', metrics=['accuracy'])
model.fit(x, y, epochs=100) # default batch_size = 32

loss, acc = model.evaluate(x, y) # mean squared error
print("acc :", acc)
print("loss :", loss)

y_predict = model.predict(x2)
print(y_predict)
'''
