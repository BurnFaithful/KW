# LSTM(Long Short Term Memory) : 연속적인 data. 시(Time)계열.

from numpy import array
from keras.models import Sequential
from keras.layers import Dense, LSTM

#1. 데이터
x = array([[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7],
            [6, 7, 8], [7, 8, 9], [8, 9, 10], [9, 10, 11], [10, 11, 12],
            [20, 30, 40], [30, 40, 50], [40, 50, 60]])
y = array([4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 50, 60, 70])

print(x)
print("x.shape :", x.shape)
print("y.shape :", y.shape)

x = x.reshape((x.shape[0], x.shape[1], 1))
print(x)
print("x.shape :", x.shape)

#2. 모델 구성
model = Sequential()
model.add(LSTM(100, activation='relu', input_shape=(3, 1))) # (column, split)
model.add(Dense(50))
model.add(Dense(60))
model.add(Dense(70))
model.add(Dense(40))
model.add(Dense(60))
model.add(Dense(90))
model.add(Dense(30))
model.add(Dense(60))
model.add(Dense(1))

# model.summary()

#3. 실행
model.compile(optimizer='adam', loss='mse')

from keras.callbacks import EarlyStopping
early_stopping = EarlyStopping(monitor='loss', patience=100, mode='auto')

# model.fit(x, y, epochs=200, batch_size=1, verbose=2) # verbose = 1 default
model.fit(x, y, epochs=10000, batch_size=1, verbose=2, callbacks=[early_stopping])
# verbose = 0 : 결과만 보여줌
# verbose = 1 : 훈련과정 상세히
# verbose = 2 : 훈련과정 간략히

x_input = array([25, 35, 45])
x_input = x_input.reshape((1, 3, 1))

yhat = model.predict(x_input)
print(yhat)