from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie
from real_time_video_me import Emotion_Rec
from os import getcwd
import numpy as np
import cv2
import time
from base64 import b64decode
from os import remove
from slice_png import img as bgImg
from EmotionRecongnition_UI import Ui_MainWindow
from cartoonize import cartoonize
import image1_rc


class Emotion_MainWindow(Ui_MainWindow):
    def __init__(self, MainWindow):
        self.path = getcwd()
        self.timer_camera = QtCore.QTimer()  # 定时器
        self.timer_video = QtCore.QTimer()  # 定时器

        self.setupUi(MainWindow)  # 设置 GUI 窗口的外观和组件
        self.retranslateUi(MainWindow)  # 设置界面的文本翻译
        self.slot_init()  # 槽函数设置

        # 设置界面动画
        gif = QMovie(":/newPrefix/icons/new_scan.gif")
        gif1 = QMovie(":/newPrefix/icons/cartoonize.gif")
        self.label_face.setMovie(gif)
        self.cartoon.setMovie(gif1)
        gif.start()
        gif1.start()

        self.cap = cv2.VideoCapture()  # 屏幕画面对象
        self.cap2 = cv2.VideoCapture()
        self.CAM_NUM = 0  # 摄像头标号
        self.model_path = None  # 模型路径

    def slot_init(self):  # 定义槽函数
        self.toolButton_file.clicked.connect(self.choose_pic)

    def choose_pic(self):
        # 界面处理
        self.cap.release()
        self.cap2.release()
        self.label_face.clear()
        self.cartoon.clear()
        self.label_result.setText("None")
        self.label_time.setText("0 s")
        self.label_outputResult.clear()
        self.label_outputResult.setStyleSheet(
            "border-image: url(:/newPrefix/icons/ini.png);"
        )

        # 使用文件选择对话框选择图片
        fileName_choose, filetype = QFileDialog.getOpenFileName(
            self.centralwidget, "选取图片文件", self.path, "图片(*.jpg;*.jpeg;*.png)"  # 起始路径
        )  # 文件类型
        self.path = fileName_choose  # 保存路径
        if fileName_choose != "":
            self.textEdit_pic.setText(
                fileName_choose + "文件已选中"
            )  # 将选中文件的路径显示在 GUI 中的 textEdit_pic 文本框中
            self.label_face.setText("正在启动识别系统...\n\nleading")
            self.cartoon.setText("正在启动识别系统...\n\nleading")
            QtWidgets.QApplication.processEvents()  # 强制刷新 GUI，确保界面的及时更新
            # 生成模型对象
            self.emotion_model = Emotion_Rec(self.model_path)
            # 读取背景图
            tmp = open("slice.png", "wb")  # 创建一个临时文件 slice.png 以存储背景图
            tmp.write(b64decode(bgImg))  # 将通过 base64 编码的背景图数据写入临时文件
            tmp.close()  # 关闭临时文件
            canvas = cv2.imread("slice.png")  # 使用 OpenCV 读取背景图，存储在变量 canvas 中
            remove("slice.png")  # 删除临时文件

            image = self.cv_imread(fileName_choose)  # 读取选择的图片
            # 计时并开始模型预测
            QtWidgets.QApplication.processEvents()
            time_start = time.time()  # 记录开始时间
            result = self.emotion_model.run(
                image, canvas, self.label_face, self.label_outputResult
            )  # 调用情感模型的 run 方法进行情感识别
            time_end = time.time()  # 记录结束时间
            # 显示结果
            cartoonize(self.path, self.cartoon)
            self.label_result.setText(result)
            self.label_time.setText(str(round((time_end - time_start), 3)) + " s")

        else:
            # 选择取消，恢复界面状态
            self.textEdit_pic.setText("文件未选中")
            gif = QMovie(":/newPrefix/icons/new_scan.gif")
            gif1 = QMovie(":/newPrefix/icons/cartoonize.gif")
            self.label_face.setMovie(gif)
            self.cartoon.setMovie(gif1)
            gif.start()
            gif1.start()
            self.label_outputResult.clear()  # 清除画面
            self.label_outputResult.setStyleSheet(
                "border-image: url(:/newPrefix/icons/ini.png);"
            )
            self.label_result.setText("None")
            self.label_time.setText("0 s")

    def cv_imread(self, filePath):
        # 读取图片
        cv_img = cv2.imdecode(np.fromfile(filePath, dtype=np.uint8), -1)
        return cv_img

        # 恢复界面
        gif = QMovie(":/newPrefix/icons/new_scan.gif")
        gif1 = QMovie(":/newPrefix/icons/cartoonize.gif")
        self.label_face.setMovie(gif)
        self.cartoon.setMovie(gif1)
        gif.start()
        gif1.start()
