import tensorflow as tf
import sys
import keras
import numpy as np
from keras.applications import ResNet50
from keras.preprocessing import image

model = keras.Sequential([
    keras.layers.Flatten(),
    keras.layers.Dense(128, activation=tf.nn.tanh),
    keras.layers.Dense(20, activation=tf.nn.relu),
    keras.layers.Dense(2, activation=tf.nn.softmax)
])
base_learning_rate = 1e-5
model.compile(optimizer=tf.keras.optimizers.Adam(lr=base_learning_rate),
              loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
              metrics=['accuracy'])
model.load_weights('model_weights_128tanh_20relu.ckpt')

resnet_settings = {
    'include_top': False,
    'weights': 'imagenet',
    'input_shape': (100, 100, 3),
    'pooling': 'max'}
resnet = ResNet50(**resnet_settings)

img = image.load_img(sys.argv[1],
                     target_size=(100, 100),
                     interpolation='bilinear')
features = resnet.predict(np.expand_dims(image.img_to_array(img), axis=0))

res = np.asarray(model.predict(features))
print(res)
print("cat" if res[0][0] > 0.5 else "not-cat")
