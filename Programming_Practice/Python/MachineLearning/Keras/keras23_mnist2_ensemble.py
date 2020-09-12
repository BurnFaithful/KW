# x_train 60000, 28, 28 -> x1, x2 각 30000

from keras.datasets import mnist

(X_train, Y_train), (X_test, Y_test) = mnist.load_data()

print("X_train[0] :", X_train[0])
print("Y_test[0] :", Y_test[0])
print("X_train shape :", X_train.shape)
print("X_test shape :", X_test.shape)
print("Y_train shape :", Y_train.shape)
print("Y_test shape :", Y_test.shape)

from keras.utils import np_utils
from keras.models import Sequential, Model
from keras.layers import Dense, Input, Dropout, Flatten, LSTM, Conv2D, MaxPooling2D
from keras.callbacks import ModelCheckpoint, EarlyStopping
import numpy as np
import os
import tensorflow as tf

# Min Max 전처리
X_train = X_train.reshape((X_train.shape[0], 28, 28, 1)).astype('float32') / 255
X_test = X_test.reshape((X_test.shape[0], 28, 28, 1)).astype('float32') / 255

Y_train = np_utils.to_categorical(Y_train)
Y_test = np_utils.to_categorical(Y_test)
# print(Y_train[0])
# print(Y_train.shape)
# print(Y_test.shape)

x1_train = X_train[:30000, :, :, :]
x2_train = X_train[30000:, :, :, :]
# y1_train = Y_train[:30000, :, :, :]
# y2_train = Y_train[30000:, :, :, :]

x1_test = X_test[:5000, :, :, :]
x2_test = X_test[5000:, :, :, :]
# y1_test = Y_test[:5000, :, :, :]
# y2_test = Y_test[5000:, :, :, :]

# x1_train = x1_train.reshape((x1_train.shape[0], 28, 28, 1)).astype('float32') / 255
# x2_train = x2_train.reshape((x2_train.shape[0], 28, 28, 1)).astype('float32') / 255
# y1_train = y1_train.reshape((y1_train.shape[0], 28, 28, 1)).astype('float32') / 255
# y2_train = y2_train.reshape((y2_train.shape[0], 28, 28, 1)).astype('float32') / 255


# One Hot Encoding : 표현하고 싶은 토큰 인덱스를 1, 나머지를 0으로 표현.
# MaxPooling : 가장 큰 수치로 이미지를 간략화.

# CNN 설정
# model = Sequential()
# model.add(Conv2D(32, kernel_size=(3, 3), input_shape=(28, 28, 1), activation='relu'))
# model.add(Conv2D(64, (3, 3), activation='relu'))
# model.add(Dense(32, activation='relu', input_shape=(784, )))
# model.add(LSTM(32, input_shape=(784, 1), activation='relu'))
# model.add(MaxPooling2D(pool_size=2))
# model.add(Dropout(0.25))
# model.add(Flatten())
# model.add(Dense(128, activation='relu'))
# model.add(Dropout(0.5))
# model.add(Dense(10, activation='softmax'))
input1 = Input(shape=(28, 28, 1))
hidden1 = Conv2D(32, (3, 3), activation='relu')(input1)
hidden1 = Flatten()(hidden1)
middle1 = Dense(16)(hidden1)

input2 = Input(shape=(28, 28, 1))
hidden2 = Conv2D(32, (3, 3), activation='relu')(input2)
hidden2 = Flatten()(hidden2)
middle2 = Dense(16)(hidden2)

from keras.layers.merge import concatenate
merge = concatenate([middle1, middle2])

output1 = Dense(16)(merge)
output1 = Dense(10, activation='softmax')(output1)

output2 = Dense(16)(merge)
output2 = Dense(10, activation='softmax')(output2)

model = Model(inputs=[input1, input2], outputs=[output1, output2])

# model.summary()

model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
# model.compile(loss='mse', optimizer='adam', metrics=['accuracy'])


early_stopping_callback = EarlyStopping(monitor='val_loss', patience=10)

# 모델의 실행
history = model.fit([x1_train, x2_train], 
                    # [y1_train, y2_train],
                    Y_train,
                    validation_data=(X_test, Y_test),
                    epochs=1, batch_size=200, verbose=1,
                    callbacks=[early_stopping_callback])

print("\n Test Accuracy: %.4f" % (model.evaluate([x1_test, x2_test], Y_test)[1]))