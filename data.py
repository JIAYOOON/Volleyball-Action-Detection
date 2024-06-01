import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# 경로 설정
train_dir = 'C:/Users/yoonj/dataset/train'
validation_dir = 'C:/Users/yoonj/dataset/validation'

# 이미지 데이터 제너레이터 설정
train_datagen = ImageDataGenerator(
    rescale=1.0/255,
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

validation_datagen = ImageDataGenerator(rescale=1.0/255)

train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(150, 150), 
    batch_size=32,
    class_mode='categorical'
)

validation_generator = validation_datagen.flow_from_directory(
    validation_dir,
    target_size=(150, 150), 
    batch_size=32,
    class_mode='categorical'
)
