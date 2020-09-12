from keras.models import Sequential
from keras.layers import Dense

import numpy as np

x_train = np.array([x for x in range(1, 11)])
y_train = np.array([x for x in range(1, 11)])
x_test = np.array([x for x in range(11, 21)])
y_test = np.array([x for x in range(11, 21)])
# x_predict = np.array([x for x in range(21, 26)])

# Q. R2를 0.5 이하로 줄이시오
# 레이어는 인풋과 아웃풋 포함 5개 이상, 노드는 각 레이어당 5개 이상.
# batch_size=1
# epoch=100 이상

model = Sequential()
# model.add(Dense(100, input_dim=1, activation='relu'))
model.add(Dense(5, input_shape=(1, ), activation='relu'))
model.add(Dense(5000))
model.add(Dense(6))
model.add(Dense(3000))
model.add(Dense(6))
model.add(Dense(2000))
model.add(Dense(6))
model.add(Dense(4000))
model.add(Dense(6))
model.add(Dense(6000))
model.add(Dense(6))
model.add(Dense(2000))
model.add(Dense(6))
model.add(Dense(4000))
model.add(Dense(6))
model.add(Dense(3000))
model.add(Dense(6))
model.add(Dense(1))

model.summary()

model.compile(loss='mse', optimizer='adam', 
                # metrics=['accuracy']
                metrics=['mse'])
model.fit(x_train, y_train, epochs=120, batch_size=1) # default batch_size = 32

loss, mse = model.evaluate(x_test, y_test, batch_size=1) # mean squared error
print("mse :", mse)
print("loss :", loss)

# 선형 회귀 -> 회귀 + 분류

y_predict = model.predict(x_test)
print(y_predict)

# R2 ↑ RMSE ↓
# RMSE Calculate
from sklearn.metrics import mean_squared_error

def RMSE(y_test, y_predict):
    return np.sqrt(mean_squared_error(y_test, y_predict))

print("RMSE :", RMSE(y_test, y_predict))

# R2 Calcuate
from sklearn.metrics import r2_score

r2_y_predict = r2_score(y_test, y_predict)
print("R2 :", r2_y_predict)