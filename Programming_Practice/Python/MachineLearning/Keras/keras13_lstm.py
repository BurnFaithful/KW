# LSTM(Long Short Term Memory) : 연속적인 data. 시(Time)계열.

from numpy import array
from keras.models import Sequential
from keras.layers import Dense, LSTM

#1. 데이터
x = array([[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]])
y = array([4, 5, 6, 7])

print(x)
print("x.shape :", x.shape)
print("y.shape :", y.shape)

'''
 x  y
123 4
234 5
345 6
456 7
'''

x = x.reshape((x.shape[0], x.shape[1], 1))
print(x)
print("x.shape :", x.shape)

'''
    x     y
[1][2][3] 4
[2][3][4] 5
[3][4][5] 6
[4][5][6] 7
'''

#2. 모델 구성
model = Sequential()
model.add(LSTM(300, activation='relu', input_shape=(3, 1))) # (column, split)
model.add(Dense(600))
model.add(Dense(300))
model.add(Dense(450))
model.add(Dense(500))
model.add(Dense(650))
model.add(Dense(1))

# model.summary()

#3. 실행
model.compile(optimizer='adam', loss='mse')
model.fit(x, y, epochs=600, batch_size=1)

x_input = array([6, 7, 8])
x_input = x_input.reshape((1, 3, 1))

yhat = model.predict(x_input)
print(yhat)