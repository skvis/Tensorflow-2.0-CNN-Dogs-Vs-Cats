import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array

import config


def predict(model):

    for fname in os.listdir(config.TEST_DIR):
        img = load_img(os.path.join(config.TEST_DIR, fname), target_size=config.TARGET_SIZE)
        x = img_to_array(img)
        x = np.expand_dims(x, axis=0)
        images = np.vstack([x])
        classes = model.predict(images, batch_size=4)
        if classes[0] > 0:
            print(fname+' is a dog')
        else:
            print(fname+' is a cat')


if __name__ == '__main__':
    model = tf.keras.models.load_model(f"{config.MODEL_PATH}my_model.h5")
    predict(model)
