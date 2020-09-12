#1. 데이터
import numpy as np
from keras.layers.merge import concatenate

x1 = np.array([range(100), range(311, 411), range(100)])
y1 = np.array([range(501, 601), range(711, 811), range(100)])

x2 = np.array([range(100, 200), range(311, 411), range(100, 200)])
y2 = np.array([range(501, 601), range(711, 811), range(100)])

# append, concatenate, hstack, vstack, ...
x3 = np.concatenate([x1, x2])
y3 = np.concatenate([y1, y2])

x1 = np.transpose(x1)
y1 = np.transpose(y1)
x2 = np.transpose(x2)
y2 = np.transpose(y2)

x3 = np.transpose(x3)
y3 = np.transpose(y3)

print(x1.shape)
print(x2.shape)
print(y1.shape)
print(y2.shape)

print(x3.shape)
print(y3.shape)
# print(x3)
# print(y3)

from sklearn.model_selection import train_test_split

x1_train, x1_test, y1_train, y1_test = train_test_split(
    x1, y1, random_state=66, test_size=0.4, shuffle=False
)

x1_val, x1_test, y1_val, y1_test = train_test_split(
    x1_test, y1_test, random_state=66, test_size=0.5, shuffle=False
)

x2_train, x2_test, y2_train, y2_test = train_test_split(
    x2, y2, random_state=66, test_size=0.4, shuffle=False
)

x2_val, x2_test, y2_val, y2_test = train_test_split(
    x2_test, y2_test, random_state=66, test_size=0.5, shuffle=False
)

x3_train, x3_test, y3_train, y3_test = train_test_split(
    x3, y3, random_state=66, test_size=0.4, shuffle=False
)

x3_val, x3_test, y3_val, y3_test = train_test_split(
    x3_test, y3_test, random_state=66, test_size=0.5, shuffle=False
)

print(x2_test.shape)
print(x3_test.shape)
# random으로 섞어도 데이터의 순서는 바뀌나 x-y 관계는 섞이지 않음.

#2. 모델 구성
# 모델은 순차적 모델, 함수형 모델이 있다.
from keras.models import Sequential, Model
from keras.layers import Dense, Input

# model = Sequential()

input1 = Input(shape=(3, ))
dense1 = Dense(5, activation='relu')(input1)
dense2 = Dense(3)(dense1)
dense3 = Dense(4)(dense2)
middle1 = Dense(3)(dense3)

input2 = Input(shape=(3, ))
xx = Dense(5, activation='relu')(input2)
xx = Dense(3)(xx)
xx = Dense(4)(xx)
middle2 = Dense(3)(xx)

merge1 = concatenate([middle1, middle2])

# 합쳤다가 분기되어야 함
output1 = Dense(30)(merge1)
output1 = Dense(3)(output1)

output2 = Dense(15)(merge1)
output2 = Dense(3)(output2)

model = Model(inputs=[input1, input2], outputs=[output1, output2])
model.summary()

'''
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
'''