# LSTM(Long Short Term Memory) : 연속적인 data. 시(Time)계열.
# MinMaxScaler = X - Xmin / Xmax - Xmin

from numpy import array
from keras.models import Sequential
from keras.layers import Dense, LSTM

#1. 데이터
x = array([[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7],
            [6, 7, 8], [7, 8, 9], [8, 9, 10], [9, 10, 11], [10, 11, 12],
            [20000, 30000, 40000], [30000, 40000, 50000], 
            [40000, 50000, 60000], [100, 200, 300]])
y = array([4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 50000, 60000, 70000, 400])

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaler.fit(x)
x = scaler.transform(x) # eveluate, predict
print(x)

# train과 predict로 나눌 것
# train = 1번째부터 13번째
# predict = 14번째

x_train = x[:-1]
x_predict = x[-1]

y_train = y[:-1]

print("x.shape :", x.shape)
print("y.shape :", y.shape)

print("x_train.shape :", x_train.shape)
print("x_predict.shape :", x_predict.shape)

# x = x.reshape((x.shape[0], x.shape[1], 1))
# print(x)
# print("x.shape :", x.shape)

#2. 모델 구성
model = Sequential()
# model.add(LSTM(100, activation='relu', input_shape=(3, 1))) # (column, split)
model.add(Dense(60, activation='relu', input_shape=(3, ))) # activation default linear
model.add(Dense(50))
model.add(Dense(60))
model.add(Dense(70))
model.add(Dense(40))
model.add(Dense(60))
model.add(Dense(90))
model.add(Dense(30))
model.add(Dense(60))
model.add(Dense(1))

model.summary()

#3. 실행
model.compile(optimizer='adam', loss='mse')
# model.fit(x, y, epochs=200, batch_size=1, verbose=2) # verbose = 1 default
model.fit(x_train, y_train, epochs=200, batch_size=1, verbose=2)
# verbose = 0 : 결과만 보여줌
# verbose = 1 : 훈련과정 상세히
# verbose = 2 : 훈련과정 간략히

import numpy as np
# x_input = array([25, 35, 45])
# x_input = np.transpose(x_input)
# x_input = scaler.transform(x_input)
# x_input = x_input.reshape((1, 3, 1))

# yhat = model.predict(x_input)
# print(yhat)

x_predict = x_predict.reshape((1, 3))
y_predict = model.predict(x_predict)
print(y_predict)