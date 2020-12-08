import numpy as np
from keras.applications.resnet50 import ResNet50
from keras.preprocessing import image
from keras.preprocessing import image_dataset_from_directory
import os
import csv

resnet_settings = {
    'include_top': False,
    'weights': 'imagenet',
    'input_shape': (100, 100, 3),
    'pooling': 'max'}
resnet = ResNet50(**resnet_settings)

imgs = image_dataset_from_directory(os.path.dirname('../data/'),
                                    shuffle=True,
                                    labels='inferred',
                                    label_mode='categorical',
                                    batch_size=32,
                                    image_size=(100, 100))

with open('../data/image_features.csv', 'w') as out:
    csvwriter = csv.writer(out, delimiter=',', quotechar="\"", quoting=csv.QUOTE_ALL)
    row = ['', 'class'] + [str(i) for i in range(0, 2048)]
    csvwriter.writerow(row)

    k = 0
    for image_batch, label_batch in iter(imgs):
        features = resnet.predict(image_batch)
        labels = np.argmax(label_batch.numpy(), axis=-1)
        for i, el in enumerate(features):
            el = (el-el.min())/(el.max() - el.min())
            row = [str(k), str(labels[i])] + [str(scalar) for scalar in el]
            csvwriter.writerow(row)
            k += 1