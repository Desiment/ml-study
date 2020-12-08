import tensorflow as tf
import keras
from keras.preprocessing import image

model = keras.Sequential([
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(2, activation=tf.nn.softmax)
])
base_learning_rate=1e-4
model.compile(optimizer=tf.keras.optimizers.Adam(lr=base_learning_rate),
              loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
              metrics=['accuracy'])
model.load_weights('../data/model_weights.ckpt')

img = image.load_img('../data/cats/cat.10.jpg',
                     target_size=(100, 100),
                     interpolation='bilinear')

print(model.predict([image.img_to_array(img)]))