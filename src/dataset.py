import os
import sys
from zipfile import ZipFile
from shutil import copyfile
from subprocess import check_output
from random import sample

import config

# Download the Kaggle Dataset
'''
Link: "https://www.kaggle.com/c/dogs-vs-cats/data"
'''


def download_dataset():

    link_list = ['https://storage.googleapis.com/kaggle-competitions-data/kaggle-v2/3362/31148/bundle/archive.zip?GoogleAccessId=web-data@kaggle-161607.iam.gserviceaccount.com&Expires=1591201828&Signature=RtdfERnscQp2pJO6Fxg5v1LgxuryJPdEQbuDXQ3g5LI9JpYoUTwmCjhvlyrzWskmrpk1FWbX6nXzS3lhNmbVqgCXiH%2BGRSAOnxlGWxEs11gObxITPCQV1AQQkYW7XDxU%2B8fUdEAgUUAo5PvSpsEA7yxToPXF4qe2eOZQLSwU5yp6HLiKmBg%2F3Pe9P7S%2B4l9ccWH2wt8S8eFl8RmlvS8V8yJsEePUrt8oHZ%2BYmr6ZVpxEC4xkGZfeLduH2Fie2%2FCdNuoNkpkThq2V%2BNG9Lve0k1TGoLcgXHNJHxT4FiqXguQr%2BMY3W7GlKBqB59bq9E3szQvaMSrg9dCjvQkJ1R%2FEYg%3D%3D&response-content-disposition=attachment%3B+filename%3Ddogs-vs-cats.zip']
    if not os.path.isdir('../input/'):
        os.makedirs('../input')
        for item in link_list:
            os.system(f"wget --no-check-certificate {item} -O ../input/dogs-vs-cats.zip")
    else:
        for item in link_list:
            if not os.path.exists(f"../input/dogs-vs-cats.zip"):
                os.system(f"wget --no-check-certificate {item} -O ../input/dogs-vs-cats.zip")
            else:
                print('File already exits')


def unzip_dataset(data_path, zip_filename):
    zip_ref = ZipFile(data_path+zip_filename, 'r')
    zip_ref.extractall(data_path+zip_filename.split('.')[0])
    zip_ref.close()
    os.remove(data_path+zip_filename)


def filter_data(source):
    cat_list, dog_list = [], []
    for fname in os.listdir(source):
        if fname[:3] == 'cat' and fname[-3:] == 'jpg':
            cat_list.append(fname)
        elif fname[:3] == 'dog' and fname[-3:] == 'jpg':
            dog_list.append(fname)
        else:
            pass
    for file in cat_list:
        copyfile(os.path.join(source, file), os.path.join(source, 'cats', file))
        os.remove(os.path.join(source, file))
    for file in dog_list:
        copyfile(os.path.join(source, file), os.path.join(source, 'dogs', file))
        os.remove(os.path.join(source, file))


def create_valid_directory():
    try:
        bashCommand = 'mkdir -p ../input/dogs-vs-cats/valid/{cats,dogs}'
        _ = check_output(['bash', '-c', bashCommand])
    except OSError as err:
        print('OS error" {0}'.format(err))
    except:
        print("unexpected error:", sys.exc_info()[0])
        raise Exception('Validation Directory not created')


def split_data(source, validation, split_size):
    file_list = [fname for fname in os.listdir(source)]
    training_size = int(len(file_list) * split_size)
    validation_size = len(file_list) - training_size
    shuffled_list = sample(file_list, len(file_list))
    training_set = shuffled_list[:training_size]
    validation_set = shuffled_list[-validation_size:]

    for file in validation_set:
        copyfile(os.path.join(source, file), os.path.join(validation, file))
        os.remove(os.path.join(source, file))

    if len(training_set) == len(os.listdir(source)):
        print('validation set created successfully')
    else:
        raise Exception('Error in creating validation set')


def show_len_data():
    print(len(os.listdir(os.path.join(config.TRAIN_DIR, 'cats'))))
    print(len(os.listdir(os.path.join(config.TRAIN_DIR, 'dogs'))))
    print(len(os.listdir(os.path.join(config.VALID_DIR, 'cats'))))
    print(len(os.listdir(os.path.join(config.VALID_DIR, 'dogs'))))


if __name__ == '__main__':

    download_dataset()

    zip_data_path = '../input/'
    zip_filename = 'dogs-vs-cats.zip'
    unzip_dataset(zip_data_path, zip_filename)

    zip_data_path = zip_data_path+zip_filename.split('.')[0]+'/'
    zip_filename = 'train.zip'
    unzip_dataset(zip_data_path, zip_filename)

    zip_filename = 'test1.zip'
    unzip_dataset(zip_data_path, zip_filename)

    # move the folder in train and in test using basic linux command(see resources)
    # create a data hierarchy as ImageDataGenerator

    filter_data(config.TRAIN_DIR)

    create_valid_directory()

    split_data(config.CAT_TRAIN_DIR, config.CAT_VALID_DIR, config.SPLIT_SIZE)
    split_data(config.DOG_TRAIN_DIR, config.DOG_VALID_DIR, config.SPLIT_SIZE)

    show_len_data()
