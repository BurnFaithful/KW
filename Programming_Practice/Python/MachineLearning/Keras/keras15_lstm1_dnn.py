import numpy as np
from keras.models import Sequential
from keras.layers import Dense, LSTM

#1. 데이터
a = np.array(range(1, 11))

def split_x(seq, size):
    split_list = []
    for i in range(len(seq) - size + 1):
        subset = seq[i:(i + size)]
        split_list.extend([subset])
    print(type(split_list))
    return np.array(split_list)

'''
size = 1 -> 10 x 1
size = 2 -> 9 x 2
size = 3 -> 8 x 3
size = 4 -> 7 x 4
size = 5 -> 6 x 5
size = 6 -> 5 x 6
size = 7 -> 4 x 7
size = 8 -> 3 x 8
size = 9 -> 2 x 9
size = 10 -> 1 x 10
'''

size = 5
dataset = split_x(a, size)
print("====================")
print(dataset)

x_train = dataset[:, :-1]
y_train = dataset[:, -1]

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(
    x_train, y_train, random_state=66, test_size=0.6, shuffle=False
)
x_test, x_val, y_test, y_val = train_test_split(
    x_test, y_test, random_state=66, test_size=0.5, shuffle=False
)

print(x_train.shape)
print(y_train.shape)

# DNN 구성
model = Sequential()
model.add(Dense(100, input_shape=(4, ), activation='relu'))
model.add(Dense(200))
model.add(Dense(300))
model.add(Dense(300))
model.add(Dense(400))
model.add(Dense(500))
model.add(Dense(400))
model.add(Dense(1))

model.summary()

from keras.callbacks import EarlyStopping
early_stopping = EarlyStopping(monitor='loss', patience=100, mode='auto')

model.compile(loss='mse', optimizer='adam', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=500, batch_size=1, verbose=2,
            validation_data=(x_val, y_val),
            callbacks=[early_stopping])

loss, acc = model.evaluate(x_test, y_test)
print("acc :", acc)
print("loss :", loss)

x2 = np.array([[7, 8, 9, 10]])
y_predict = model.predict(x2)
print(y_predict)