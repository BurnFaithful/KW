# LSTM(Long Short Term Memory) : 연속적인 data. 시(Time)계열.

import numpy as np
from keras.models import Sequential, Model
from keras.layers import Dense, LSTM, Input

#1. 데이터
x = np.array([[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7],
            [6, 7, 8], [7, 8, 9], [8, 9, 10], [9, 10, 11], [10, 11, 12],
            [20, 30, 40], [30, 40, 50], [40, 50, 60]])
y = np.array([4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 50, 60, 70])

x1_train = x[:10]
x2_train = x[10:]
y1_train = y[:10]
y2_train = y[10:]

# print(x)
# print("x.shape :", x.shape)
# print("y.shape :", y.shape)

# x = x.reshape((x.shape[0], x.shape[1], 1))
# print(x)
# print("x.shape :", x.shape)

print(x1_train)
print(x2_train)
print("x1_train.shape :", x1_train.shape)
print("x2_train.shape :", x2_train.shape)

x1_train = x1_train.reshape((x1_train.shape[0], x1_train.shape[1], 1))
x2_train = x2_train.reshape((x2_train.shape[0], x2_train.shape[1], 1))

print("x1_train.shape :", x1_train.shape)
print("x2_train.shape :", x2_train.shape)

# y1_train = y1_train.reshape((y1_train.shape[0], 1))
# y2_train = y2_train.reshape((y2_train.shape[0], 1))

print("y1_train.shape :", y1_train.shape)
print("y2_train.shape :", y2_train.shape)

#2. 모델 구성
# model = Sequential()
# model.add(LSTM(100, activation='relu', input_shape=(3, 1))) # (column, split)
# model.add(Dense(50))
# model.add(Dense(60))
# model.add(Dense(70))
# model.add(Dense(40))
# model.add(Dense(60))
# model.add(Dense(90))
# model.add(Dense(30))
# model.add(Dense(60))
# model.add(Dense(1))

input1 = Input(shape=(3, 1))
input1_lstm = LSTM(40)(input1)
hidden1 = Dense(50, activation='relu')(input1_lstm)
hidden1 = Dense(60)(hidden1)
hidden1 = Dense(70)(hidden1)
hidden1 = Dense(40)(hidden1)
middle1 = Dense(60)(hidden1)

input2 = Input(shape=(3, 1))
input2_lstm = LSTM(50)(input2)
hidden2 = Dense(90, activation='relu')(input2_lstm)
hidden2 = Dense(40)(hidden2)
hidden2 = Dense(60)(hidden2)
hidden2 = Dense(70)(hidden2)
middle2 = Dense(60)(hidden2)

# model.summary()

# concatenate를 할 때 input, target arrays의 크기를 맞춰야 한다.
from keras.layers.merge import concatenate
merge = concatenate([middle1, middle2])

output1 = Dense(60)(merge)
output1 = Dense(1)(output1)

output2 = Dense(80)(merge)
output2 = Dense(1)(output2)

model = Model(inputs=[input1, input2], outputs=[output1, output2])

#3. 실행
model.compile(optimizer='adam', loss='mse', metrics=['mse'])

from keras.callbacks import EarlyStopping
early_stopping = EarlyStopping(monitor='loss', patience=100, mode='auto')

# x1_train = np.swapaxes(x1_train, 1, 0)
# x2_train = np.swapaxes(x2_train, 1, 0)

# model.fit(x, y, epochs=200, batch_size=1, verbose=2) # verbose = 1 default
# model.fit(x, y, epochs=10000, batch_size=1, verbose=2, callbacks=[early_stopping])
model.fit([x1_train, x1_train], [y1_train, y1_train], epochs=10000, batch_size=1,
            verbose=2,
            callbacks=[early_stopping])
# verbose = 0 : 결과만 보여줌
# verbose = 1 : 훈련과정 상세히
# verbose = 2 : 훈련과정 간략히

# x_input = np.array([25, 35, 45])
# x_input = x_input.reshape((1, 3, 1))

# yhat = model.predict(x_input)
# print(yhat)