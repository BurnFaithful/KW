#1. 데이터
import numpy as np

x_train = np.array([x for x in range(1, 11)])
y_train = np.array([y for y in range(1, 11)])
x_test = np.array([x for x in range(11, 21)])
y_test = np.array([y for y in range(11, 21)])
x_val = np.array([x for x in range(101, 106)])
y_val = np.array([629, 1070, 852, 205, 556])

#2. 모델 구성
from keras.models import Sequential
from keras.layers import Dense

model = Sequential()
# model.add(Dense(100, input_dim=1, activation='relu'))
model.add(Dense(5, input_shape=(1, ), activation='relu'))
model.add(Dense(6))
model.add(Dense(3))
model.add(Dense(7))
model.add(Dense(5))
model.add(Dense(1))

# model.summary()

# x_train, y_train -> fit
# x_val, y_val -> fit
# x_test, y_test -> evaluate, predict

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