#1. 데이터
import numpy as np

x1 = np.array([range(100), range(311, 411), range(100)])
y1 = np.array([range(501, 601), range(711, 811), range(100)])

x2 = np.array([range(100, 200), range(311, 411), range(100, 200)])
y2 = np.array([range(501, 601), range(711, 811), range(100)])

x1 = np.transpose(x1)
y1 = np.transpose(y1)
x2 = np.transpose(x2)
y2 = np.transpose(y2)

print(x1.shape)
print(x2.shape)
print(y1.shape)
print(y2.shape)

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

print(x2_test.shape)
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

from keras.layers.merge import concatenate
merge1 = concatenate([middle1, middle2])

# 합쳤다가 분기되어야 함
output1 = Dense(30)(merge1)
output1 = Dense(3)(output1)

output2 = Dense(15)(merge1)
output2 = Dense(3)(output2)

model = Model(inputs=[input1, input2], outputs=[output1, output2])
model.summary()

#3. 훈련
model.compile(loss='mse', optimizer='adam', 
                # metrics=['accuracy']
                metrics=['mse'])
# model.fit(x_train, y_train, epochs=120, batch_size=1) # default batch_size = 32
model.fit([x1_train, x2_train], [y1_train, y2_train], epochs=120, batch_size=1,
            validation_data=([x1_val, x2_val], [y1_val, y2_val])) # 검증

# fit을 여러 번 해도 각각은 독립시행임.

#4. 평가 예측
loss = model.evaluate([x1_test, x2_test], [y1_test, y2_test], batch_size=1) # mean squared error
# print("mse :", mse)
print("loss :", loss)

# 선형 회귀 -> 회귀 + 분류

y1_predict, y2_predict = model.predict([x1_test, x2_test])
print(y1_predict, y2_predict)

# R2 ↑ RMSE ↓
# RMSE Calculate
from sklearn.metrics import mean_squared_error

def RMSE(y_test, y_predict):
    return np.sqrt(mean_squared_error(y_test, y_predict))

RMSE1 = RMSE(y1_test, y1_predict)
RMSE2 = RMSE(y2_test, y2_predict)

print("RMSE1 :", RMSE1)
print("RMSE2 :", RMSE2)
print("RMSE :", (RMSE1 + RMSE2) / 2)

# R2 Calcuate
from sklearn.metrics import r2_score

r2_y1_predict = r2_score(y1_test, y1_predict)
r2_y2_predict = r2_score(y2_test, y2_predict)
print("R2_y1 :", r2_y1_predict)
print("R2_y2 :", r2_y2_predict)
print("R2 :", (r2_y1_predict + r2_y2_predict) / 2)