
from __future__ import print_function
import numpy as np
np.random.seed(1337)  # for reproducibility

from keras.preprocessing import sequence
from keras.models import Model
from keras.layers import Dense, Activation, Embedding, Flatten, Input, Dropout, merge, Convolution1D, GlobalMaxPooling1D, LSTM
from keras.datasets import imdb

max_features = 200 #20000
maxlen = 80  # cut texts after this number of words (among top max_features most common words)
batch_size = 32

print('Loading data...')
(X_train, y_train), (X_test, y_test) = imdb.load_data(nb_words=max_features)
print(len(X_train), 'train sequences')
print(len(X_test), 'test sequences')

print (X_train[0])

print('Pad sequences (samples x time)')
X_train = sequence.pad_sequences(X_train, maxlen=maxlen)
X_test = sequence.pad_sequences(X_test, maxlen=maxlen)
print('X_train shape:', X_train.shape)
print('X_test shape:', X_test.shape)

print('Build model...')


inputs = Input(shape=(maxlen,))
x = inputs
x = Embedding(max_features, 128, dropout=0.2)(x)
#x = Dense(64)(x)
#x = Activation(("relu"))(x)  # Non-linearity
#x = Dense(64)(x)
#x = Dropout(0.5)(x)

xA = Convolution1D(32,3, border_mode='same', input_shape = X_train.shape[1:])(x)
xA = Activation(("relu"))(xA)
xA = GlobalMaxPooling1D()(xA)

xB = LSTM(128,dropout_W=0.2,dropout_U=0.2)(x)



#x = Flatten()(x)
xA = Dense(1)(xA)
predictionsA = Activation("sigmoid")(xA)

xB = Dense(1)(xB)
predictionsB = Activation("sigmoid")(xB)

predictions = merge([predictionsA,predictionsB],mode='sum')

model = Model(input=inputs, output=predictions)
model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

print('Train...')
model.fit(X_train, y_train, batch_size=batch_size, nb_epoch=15,
          validation_data=(X_test, y_test))
score, acc = model.evaluate(X_test, y_test,
                            batch_size=batch_size)
print('Test score:', score)
print('Test accuracy:', acc)