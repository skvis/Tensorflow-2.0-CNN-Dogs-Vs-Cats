import os


DATA_PATH = '../input/dogs-vs-cats/'
MODEL_PATH = '../models/'

TRAIN_DIR = os.path.join(DATA_PATH, 'train')
TEST_DIR = os.path.join(DATA_PATH, 'test')

VALID_DIR = os.path.join(DATA_PATH, 'valid')

CAT_TRAIN_DIR = os.path.join(TRAIN_DIR, 'cats')
CAT_VALID_DIR = os.path.join(VALID_DIR, 'cats')
DOG_TRAIN_DIR = os.path.join(TRAIN_DIR, 'dogs')
DOG_VALID_DIR = os.path.join(VALID_DIR, 'dogs')

SPLIT_SIZE = .9

IMAGE_WIDTH = 150
IMAGE_HEIGHT = 150
IMAGE_CHANNELS = 3
TARGET_SIZE = (IMAGE_WIDTH, IMAGE_HEIGHT)
BATCH_SIZE = 32
CLASS_MODE = 'binary'
LEARNING_RATE = 1e-3
NUM_EPOCHS = 2
