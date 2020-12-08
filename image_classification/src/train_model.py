import pandas as pd
import keras
import tensorflow as tf
from sklearn.model_selection import train_test_split

data = pd.read_csv('../data/image_features.csv', index_col=0, delimiter=',')
vectors = data[[str(i) for i in range(2048)]].to_numpy()
classes = data['class'].to_numpy()

model = keras.Sequential([
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(2, activation=tf.nn.softmax)
])

base_learning_rate=1e-4
model.compile(optimizer=tf.keras.optimizers.Adam(lr=base_learning_rate),
              loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
              metrics=['accuracy'])

epochs=10
train_dataset = tf.data.Dataset.from_tensor_slices((vectors, classes))
model.fit(train_dataset,
          epochs=epochs)

model.save_weights('../data/model_weights.ckpt')