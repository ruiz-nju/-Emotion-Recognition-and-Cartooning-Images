import warnings
import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
warnings.filterwarnings(action='ignore')
from keras.callbacks import CSVLogger, ModelCheckpoint, EarlyStopping
from keras.callbacks import ReduceLROnPlateau
from keras.preprocessing.image import ImageDataGenerator
from load_and_process import load_fer2013
from load_and_process import preprocess_input
from models.cnn import mini_XCEPTION
from sklearn.model_selection import train_test_split

# 参数
batch_size = 32
num_epochs = 10000
input_shape = (48, 48, 1)
validation_split = .2
verbose = 1
num_classes = 7
patience = 50
base_path = 'models/'

# 构建模型
# 构建、配置和显示一个使用了 mini_XCEPTION 架构的神经网络模型
# 用于解决一个多分类问题。在训练过程中，模型将使用 Adam 优化器来最小化对数损失函数，同时监测准确度作为性能指标。
model = mini_XCEPTION(input_shape, num_classes)
model.compile(optimizer='adam',  # 优化器采用adam
              loss='categorical_crossentropy',  # 多分类的对数损失函数
              metrics=['accuracy'])
model.summary()

# 定义回调函数 Callbacks 用于训练过程，回调函数在训练过程中监控和调整模型
log_file_path = base_path + '_emotion_training.log'
# 创建一个日志文件的路径，用于记录训练过程中的信息
csv_logger = CSVLogger(log_file_path, append=False)
# 创建一个 CSVLogger 回调，用于将训练过程中的指标记录到一个 CSV 文件中
early_stop = EarlyStopping('val_loss', patience=patience)
# 创建一个 EarlyStopping 回调，用于在模型训练时监控验证集上的损失值，如果连续 patience 次验证集损失没有改善，则提前停止训练
reduce_lr = ReduceLROnPlateau('val_loss', factor=0.1,
                              patience=int(patience / 4),
                              verbose=1)
# 创建一个 ReduceLROnPlateau 回调，用于在验证集上监控损失值，如果损失值停止改善，则减小学习率

# 模型位置及命名
trained_models_path = base_path + '_mini_XCEPTION'
model_names = trained_models_path + '.{epoch:02d}-{val_acc:.2f}.hdf5'

# 定义模型权重位置、命名等
model_checkpoint = ModelCheckpoint(model_names,
                                   'val_loss', verbose=1,
                                   save_best_only=True)
callbacks = [model_checkpoint, csv_logger, early_stop, reduce_lr]

# 载入数据集
faces, emotions = load_fer2013()
faces = preprocess_input(faces)
num_samples, num_classes = emotions.shape

# 划分训练、测试集
xtrain, xtest, ytrain, ytest = train_test_split(faces, emotions, test_size=0.2, shuffle=True)

# 图片产生器，在批量中对数据进行增强，扩充数据集大小
data_generator = ImageDataGenerator(
     featurewise_center=False,
     featurewise_std_normalization=False,
     rotation_range=10,
     width_shift_range=0.1,
     height_shift_range=0.1,
     shear_range=0.2,
     zoom_range=0.1,
     horizontal_flip=True
)

# 利用数据增强进行训练
model.fit_generator(
                    data_generator.flow(xtrain, ytrain, batch_size),
                    steps_per_epoch=len(xtrain) / batch_size,
                    epochs=num_epochs,
                    verbose=1, callbacks=callbacks,
                    validation_data=(xtest, ytest))
