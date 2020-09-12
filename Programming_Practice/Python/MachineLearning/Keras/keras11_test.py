# 행 무시 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#1. 데이터
import numpy as np

x = np.array([range(1, 101), range(101, 201)])
y = np.array([range(201, 301)])
print(x)

print(x.shape)

x = np.transpose(x)
y = np.transpose(y)

print(x.shape)

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(
    x, y, random_state=66, test_size=0.4, shuffle=False
)

x_val, x_test, y_val, y_test = train_test_split(
    x_test, y_test, random_state=66, test_size=0.5, shuffle=False
)
# random으로 섞어도 데이터의 순서는 바뀌나 x-y 관계는 섞이지 않음.

#2. 모델 구성
from keras.models import Sequential
from keras.layers import Dense

model = Sequential()
# model.add(Dense(100, input_dim=1, activation='relu'))
model.add(Dense(10, input_shape=(2, ), activation='relu'))
model.add(Dense(5000))
model.add(Dense(10))
model.add(Dense(6000))
model.add(Dense(10))
model.add(Dense(7000))
model.add(Dense(10))
model.add(Dense(4000))
model.add(Dense(10))
model.add(Dense(3000))
model.add(Dense(10))
model.add(Dense(6000))
model.add(Dense(10))
model.add(Dense(8000))
model.add(Dense(10))
model.add(Dense(4000))
model.add(Dense(10))
model.add(Dense(6000))
model.add(Dense(10))
model.add(Dense(3000))
model.add(Dense(10))
model.add(Dense(1))

# model.summary()

#3. 훈련
model.compile(loss='mse', optimizer='adam', 
                # metrics=['accuracy']
                metrics=['mse'])
# model.fit(x_train, y_train, epochs=120, batch_size=1) # default batch_size = 32
model.fit(x_train, y_train, epochs=120, batch_size=1,
            validation_data=(x_val, y_val)) # 검증

#4. 평가 예측
loss, mse = model.evaluate(x_test, y_test, batch_size=1) # mean squared error
print("mse :", mse)
print("loss :", loss)

# 선형 회귀 -> 회귀 + 분류

a_test = np.array([[101, 102, 103], [201, 202, 203]])
a_test = np.transpose(a_test)
y_predict = model.predict(x_test)
# y_predict = model.predict(a_test)
print(y_predict)

# R2 ↑ RMSE ↓
# RMSE Calculate
from sklearn.metrics import mean_squared_error

def RMSE(y_test, y_predict):
    return np.sqrt(mean_squared_error(y_test, y_predict))

print("RMSE :", RMSE(y_test, y_predict))
# print("RMSE : ", RMSE(a_test, y_predict))

# R2 Calcuate
from sklearn.metrics import r2_score

r2_y_predict = r2_score(y_test, y_predict)
# r2_y_predict = r2_score(a_test, y_predict)
print("R2 :", r2_y_predict)