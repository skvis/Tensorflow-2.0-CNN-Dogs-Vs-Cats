import os
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import tensorflow as tf

import config


def view_data():
    nrows, ncols = 4, 4
    pic_index = 0
    fig = plt.gcf()
    fig.set_size_inches(nrows * 4, ncols * 4)
    pic_index += 8
    next_cat_images = [os.path.join(config.CAT_TRAIN_DIR, fname) for fname in os.listdir(config.CAT_TRAIN_DIR)[pic_index-8:pic_index]]
    next_dog_images = [os.path.join(config.DOG_TRAIN_DIR, fname) for fname in os.listdir(config.DOG_TRAIN_DIR)[pic_index-8:pic_index]]

    for i, img_path in enumerate(next_cat_images+next_dog_images):
        sp = plt.subplot(nrows, ncols, i+1)
        sp.axis('off')
        img = mpimg.imread(img_path)
        plt.imshow(img)
    plt.show()


def plot_graphs(history, string):
    plt.plot(history[string])
    plt.plot(history['val_'+string])
    plt.xlabel('Epochs')
    plt.ylabel(string)
    plt.legend([string, 'val_'+string])
    plt.show()


def view_test_images():
    fig = plt.gcf()
    fig.set_size_inches(16, 16)
    for i, fname in enumerate(os.listdir(config.TEST_DIR)[:16]):
        sp = plt.subplot(4, 4, i+1)
        sp.axis('off')
        image = mpimg.imread(os.path.join(config.TEST_DIR, fname))
        plt.title(fname)
        plt.imshow(image)
    plt.show()


if __name__ == '__main__':
    view_data()

    # Run after training the model
    # log_data = pd.read_csv(f'{config.MODEL_PATH}training.log', sep=',')
    history = np.load(f'{config.MODEL_PATH}my_history.npy', allow_pickle=True).item()
    plot_graphs(history, 'accuracy')
    plot_graphs(history, 'loss')

    view_test_images()
