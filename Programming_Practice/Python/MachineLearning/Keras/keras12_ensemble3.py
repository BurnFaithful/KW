# 2 input, 1 output ensemble model

#1. 데이터
import numpy as np

x1 = np.array([range(100), range(311, 411), range(100)])
x2 = np.array([range(100, 200), range(311, 411), range(100, 200)])

y1 = np.array([range(501, 601), range(711, 811), range(100)])

x1 = np.transpose(x1)
x2 = np.transpose(x2)
y1 = np.transpose(y1)

print(x1.shape)
print(x2.shape)
print(y1.shape)

from sklearn.model_selection import train_test_split

x1_train, x1_test, x2_train, x2_test, y1_train, y1_test = train_test_split(
    x1, x2, y1, random_state=66, test_size=0.4, shuffle=False
)

x1_val, x1_test, x2_val, x2_test, y1_val, y1_test = train_test_split(
    x1_test, x2_test, y1_test, random_state=66, test_size=0.5, shuffle=False
)

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

model = Model(inputs=[input1, input2], outputs=[output1])
model.summary()

#3. 훈련
model.compile(loss='mse', optimizer='adam', 
                # metrics=['accuracy']
                metrics=['mse'])
# model.fit(x_train, y_train, epochs=120, batch_size=1) # default batch_size = 32
model.fit([x1_train, x2_train], y1_train, 
            epochs=120, 
            batch_size=1,
            validation_data=([x1_val, x2_val], y1_val)) # 검증

# fit을 여러 번 해도 각각은 독립시행임.

#4. 평가 예측
loss = model.evaluate([x1_test, x2_test], y1_test, batch_size=1) # mean squared error
# print("mse :", mse)
print("loss :", loss)

# 선형 회귀 -> 회귀 + 분류

y_predict = model.predict([x1_test, x2_test])
print(y_predict)

# R2 ↑ RMSE ↓
# RMSE Calculate
from sklearn.metrics import mean_squared_error

def RMSE(y_test, y_predict):
    return np.sqrt(mean_squared_error(y_test, y_predict))

RMSE = RMSE(y1_test, y_predict)
print("RMSE :", RMSE)

# R2 Calcuate
from sklearn.metrics import r2_score

r2_y_predict = r2_score(y1_test, y_predict)
print("R2 :", r2_y_predict)