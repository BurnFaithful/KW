#1. 데이터
import numpy as np

x = np.array(range(1, 101))
y = np.array(range(1, 101))
print(x)

# x_train = x[:60]
# x_val = x[60:80]
# x_test = x[80:]
# y_train = y[:60]
# y_val = y[60:80]
# y_test = y[80:]

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(
    x, y, random_state=66, train_size=0.8, test_size=0.2#, shuffle=False
)

x_test, x_val, y_test, y_val = train_test_split(
    x_test, y_test, random_state=66, test_size=0.5#, shuffle=False
)
# random으로 섞어도 데이터의 순서는 바뀌나 x-y 관계는 섞이지 않음.

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

model.save('./save/savetest01.h5')
print("Save Complete.")

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