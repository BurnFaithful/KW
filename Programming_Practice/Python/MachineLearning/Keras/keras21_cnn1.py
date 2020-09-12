from keras.models import Sequential

filter_size = 32
kernal_size = (3, 3)

from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
model = Sequential()
model.add(Conv2D(7, # filter : output
                (2, 2), # kernel_size : 자르는 크기.
                padding='same', # default : valid. same이면 input과 동일하게.
                input_shape=(28, 28, 1)))
# (2, 2) -> 자르는 단위크기
# input_shape (width, height, feature)
# 1 : 흑백, 3 : 컬러

# padding valid일 때 (Edge의) 가중치 손실이 있을 수 있다. 이를 same으로 최소화한다.
model.add(Conv2D(4, (2, 2)))
model.add(Conv2D(16, (2, 2)))
model.add(Conv2D(8, (2, 2)))

# model.add(MaxPooling2D(3, 3))

model.add(Flatten())
model.add(Dense(10))
model.add(Dense(1))

model.summary()

# Flatten : 평평하게 만듦. Dense 레이어와 Conv 레이어를 연결하기 위해선 Flatten 수행이 필요
