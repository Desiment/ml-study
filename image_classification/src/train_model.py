import pandas as pd
import keras
import tensorflow as tf
import numpy as np
from sklearn.model_selection import train_test_split

data = pd.read_csv('data/image_features.csv', index_col=0, delimiter=',')
vectors = data[[str(i) for i in range(2048)]].to_numpy()
classes = data['class'].to_numpy()

model = keras.Sequential([
    keras.layers.Flatten(),
    keras.layers.Dense(128, activation=tf.nn.tan),
    keras.layers.Dense(20, activation=tf.nn.relu),
    keras.layers.Dense(2, activation=tf.nn.softmax)
])

base_learning_rate = 1e-3
model.compile(optimizer=tf.keras.optimizers.Adam(lr=base_learning_rate),
              loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
              metrics=['accuracy'])

epochs = 10
batch_size = 32
classes = tf.keras.utils.to_categorical(classes, num_classes=2, dtype='float32')
classes = np.asarray(classes).astype('float32').reshape((-1, 1, 2))
vectors = np.asarray(vectors).astype('float32').reshape((-1, 1, 2048))

train_dataset = tf.data.Dataset.from_tensor_slices((vectors, classes))
model.fit(train_dataset,
          batch_size=batch_size,
          epochs=epochs)

model.save_weights('data/model_weights.ckpt')
