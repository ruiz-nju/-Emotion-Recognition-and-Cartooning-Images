import pandas as pd
import cv2
import numpy as np


dataset_path = 'fer2013/fer2013/fer2013.csv'
image_size=(48,48)

def load_fer2013():
        data = pd.read_csv(dataset_path)
        # 使用 Pandas 库的 read_csv 函数读取 FER2013 数据集的CSV文件
        pixels = data['pixels'].tolist()
        # 从CSV文件中提取 'pixels' 列，该列包含了图像的像素值，并将其转换为列表
        width, height = 48, 48
        # 设定图像的宽度和高度
        faces = []
        # 创建一个空列表，用于存储处理后的图像数据
        for pixel_sequence in pixels:
            # 遍历每张图像的像素序列
            face = [int(pixel) for pixel in pixel_sequence.split(' ')]
            # 将像素序列分割并转换为整数列表
            face = np.asarray(face).reshape(width, height)
            # 将整数列表转换为 NumPy 数组，并重新形状为图像的二维数组
            face = cv2.resize(face.astype('uint8'),image_size)
            # 使用 OpenCV 的 resize 函数将图像大小调整为指定的 image_size
            faces.append(face.astype('float32'))
            # 将处理后的图像添加到 faces 列表中
        faces = np.asarray(faces)
        # 将处理后的图像列表转换为 NumPy 数组
        faces = np.expand_dims(faces, -1)
        # 在数组的最后一个维度上添加一个维度，以适应深度学习模型的输入要求
        emotions = pd.get_dummies(data['emotion']).as_matrix()
        # 使用 Pandas 的 get_dummies 函数对 'emotion' 列进行独热编码，表示图像的情感标签,将结果转换为 NumPy 数组
        return faces, emotions
        # 返回处理后的图像数据和相应的情感标签数组

def preprocess_input(x, v2=True):
    x = x.astype('float32')
    # 将输入数据的数据类型转换为浮点数类型（float32）
    x = x / 255.0
    # 对输入数据进行归一化，将像素值缩放到 [0, 1] 的范围内
    if v2:
        x = x - 0.5
        # 对数据进行平移
        x = x * 2.0
        # 对数据进行缩放
    return x
    # 返回预处理后的数据