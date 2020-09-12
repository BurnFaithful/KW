#1. 데이터
import numpy as np

x = np.array(range(1, 101))
y = np.array(range(1, 101))
print(x)

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(
    x, y, random_state=66, test_size=0.4#, shuffle=False
)

x_test, x_val, y_test, y_val = train_test_split(
    x_test, y_test, random_state=66, test_size=0.5#, shuffle=False
)
# random으로 섞어도 데이터의 순서는 바뀌나 x-y 관계는 섞이지 않음.

#2. 모델 구성
# 모델은 순차적 모델, 함수형 모델이 있다.
from keras.models import Sequential, Model
from keras.layers import Dense, Input

# model = Sequential()

# 레이어를 10개 이상 늘리시오.
# input1 = Input(shape=(1, ))
# dense1 = Dense(5, activation='relu')(input1)
# dense2 = Dense(3)(dense1)
# dense3 = Dense(4)(dense2)
# dense4 = Dense(8)(dense3)
# dense5 = Dense(5)(dense4)
# dense6 = Dense(9)(dense5)
# dense7 = Dense(10)(dense6)
# dense8 = Dense(4)(dense7)
# dense9 = Dense(6)(dense8)
# dense10 = Dense(7)(dense9)
# output1 = Dense(1)(dense3)

input1 = Input(shape=(1, ))
xx = Dense(5, activation='relu')(input1)
xx = Dense(3)(xx)
xx = Dense(4)(xx)
xx = Dense(8)(xx)
xx = Dense(5)(xx)
xx = Dense(9)(xx)
xx = Dense(10)(xx)
xx = Dense(4)(xx)
xx = Dense(6)(xx)
xx = Dense(7)(xx)
output1 = Dense(1)(xx)

model = Model(inputs=input1, outputs=output1)
model.summary()

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