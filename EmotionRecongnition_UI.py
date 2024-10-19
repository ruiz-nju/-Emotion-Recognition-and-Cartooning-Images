
from PyQt5 import QtCore, QtGui, QtWidgets
#导入模块：核心功能、图形用户界面（GUI）、创建标准GUI应用程序

class Ui_MainWindow(object):#定义了名为Ui_MainWindow的继承于object的python类
    def setupUi(self, MainWindow):#用于设置主窗口UI的方法
        MainWindow.setObjectName("MainWindow")#设置主窗口对象名称
        MainWindow.setWindowModality(QtCore.Qt.NonModal)#设置窗口模态性为非模态，方便与应用程序的其他部分进行交互
        MainWindow.resize(820, 625)#设置窗口的初始大小
        MainWindow.setMinimumSize(QtCore.QSize(820, 625))#设置窗口的最小大小
        MainWindow.setMaximumSize(QtCore.QSize(820, 625))#设置窗口的最大大小
        icon = QtGui.QIcon()#创建一个QT的图标对象
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/icons/pai.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # 从指定的文件路径加载图像
        MainWindow.setWindowIcon(icon)#将前面创建的图标设置为主窗口的图标
        MainWindow.setToolTip("")#设置主窗口的工具提示为空字符串。工具提示通常是在用户将鼠标悬停在控件上时显示的一段文本。
        MainWindow.setAutoFillBackground(False)#设置为不自动填充窗口的背景
        MainWindow.setStyleSheet(
                "\n"
                "#QInputDialog{border-image: url(:/newPrefix/images_test/light.png);}\n"
                "\n"
                "QMenuBar{border-color:transparent;}\n"#设置了菜单栏的边框颜色为透明。
                "QToolButton[objectName=pushButton_doIt]{\n"
                "    border:5px;}\n"#定义了一个名为 pushButton_doIt 的工具按钮的边框大小为5像素
                "\n"
                "QToolButton[objectName=pushButton_doIt]:hover {\n"
                "    image:url(:/newPrefix/images_test/run_hover.png);}\n"
                "\n"#当鼠标悬停在 pushButton_doIt 按钮上时，应用以下样式
                "QToolButton[objectName=pushButton_doIt]:pressed {\n"
                "    image:url(:/newPrefix/images_test/run_pressed.png);}\n"
                "\n"#当按钮被按下时，应用以下样式
                "QScrollBar:vertical{\n"
                "    background:transparent;\n"
                "    padding:2px;\n"
                "    border-radius:8px;\n"
                "    max-width:14px;}\n"
                "\n"#定义了垂直滚动条的样式。在这里，设置了滚动条的背景为透明，内边距为2像素，边框半径为8像素，最大宽度为14像素。这些属性可以调整滚动条的外观。
                "QScrollBar::handle:vertical{\n"
                "    background:#9acd32;\n"
                "    min-height:50px;\n"
                "    border-radius:8px;\n"
                "}\n"
                "\n"#垂直滚动条的滑块（handle）的样式。设置了滑块的背景颜色为 #9acd32，最小高度为50像素，边框半径为8像素。这是滑块正常状态的样式。
                "QScrollBar::handle:vertical:hover{\n"
                "    background:#9eb764;}\n"
                "\n"#当滑块被悬停时应用的样式。在这里，设置了滑块的背景颜色为 #9eb764
                "QScrollBar::handle:vertical:pressed{\n"
                "    background:#9eb764;\n"
                "}\n"#当滑块被按下时应用的样式。同样，设置了滑块的背景颜色为 #9eb764
                "QScrollBar::add-page:vertical{\n"
                "    background:none;\n"
                "}\n"#定义了垂直滚动条的增加页面（即滑块右侧的区域）的样式，将其背景设置为透明
                "                               \n"
                "QScrollBar::sub-page:vertical{\n"
                "    background:none;\n"
                "}\n"#定义了垂直滚动条的减少页面（即滑块左侧的区域）的样式，同样将其背景设置为透明
                "\n"
                "QScrollBar::add-line:vertical{\n"
                "    background:none;}\n"#定义了垂直滚动条的增加线的样式，同样将它们的背景设置为透明
                "                                 \n"
                "QScrollBar::sub-line:vertical{\n"
                "    background:none;\n"#定义了垂直滚动条的减少线的样式，同样将它们的背景设置为透明
                "}\n"
                "QScrollArea{\n"
                "    border:0px;\n"#设置了滚动区域的边框宽度为0像素，即没有边框
                "}\n"
                "\n"
                "QScrollBar:horizontal{\n"
                "    background:transparent;\n"
                "    padding:0px;\n"
                "    border-radius:6px;\n"
                "    max-height:12px;\n"
                "}\n"#定义了水平滚动条的样式。在这里，设置了水平滚动条的背景为透明，内边距为0像素，边框半径为6像素，最大高度为12像素
                "\n"
                "QScrollBar::handle:horizontal{\n"
                "    background:#9acd32;\n"
                "    min-width:50px;\n"
                "    border-radius:6px;\n"
                "}\n"#设置了滑块的背景颜色为 #9acd32，最小宽度为50像素，边框半径为6像素
                "\n"
                "QScrollBar::handle:horizontal:hover{\n"
                "    background:#9eb764;\n"
                "}\n"#当滑块被悬停时应用的样式。在这里，设置了滑块的背景颜色为 #9eb764
                "\n"
                "QScrollBar::handle:horizontal:pressed{\n"
                "    background:#9eb764;\n"
                "}\n"#当滑块被按下时应用的样式。同样，设置了滑块的背景颜色为 #9eb764
                "\n"
                "QScrollBar::add-page:horizontal{\n"
                "    background:none;\n"
                "}\n"#定义了水平滚动条的增加页面（即滑块右侧的区域）的样式，将其背景设置为透明
                "\n"
                "QScrollBar::sub-page:horizontal{\n"
                "    background:none;\n"
                "}\n"#定义了水平滚动条的减少页面（即滑块左侧的区域）的样式，同样将其背景设置为透明
                "QScrollBar::add-line:horizontal{\n"
                "    background:none;\n"
                "}\n"#定义了水平滚动条的增加线的样式，将它们的背景设置为透明
                "\n"
                "QScrollBar::sub-line:horizontal{\n"
                "    background:none;\n"
                "}\n"# 定义了水平滚动条的减少线的样式，将它们的背景设置为透明
                "QToolButton::hover{\n"
                "    border:0px;\n"
                "} "#当工具按钮被悬停时，设置边框为0像素，即没有边框
        )

        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)#设置标签页的形状为圆角形状
        self.centralwidget = QtWidgets.QWidget(MainWindow)#创建了一个中心部件(central widget)，并将其设置为 MainWindow 的中心部件。在 PyQt 应用中，中心部件通常是主要的用户界面区域
        self.centralwidget.setObjectName("centralwidget")#为中心部件设置了对象名称
        # 设置左上角标题标签
        self.label_title = QtWidgets.QLabel(self.centralwidget)#创建了一个标签控件(QLabel)，并将其设置为中心部件的子控件
        self.label_title.setGeometry(QtCore.QRect(-30, 20, 425, 47))#设置了标签控件的几何位置。在这里，标签的左上角坐标为(8, 30)，宽度为 425，高度为 47
        self.label_title.setMinimumSize(QtCore.QSize(0, 30))#设置了标签控件的最小尺寸。这里设置了高度的最小值为 30，而宽度的最小值默认为 0
        font = QtGui.QFont()#创建了一个字体对象
        font.setFamily("楷体")
        font.setPointSize(22)
        self.label_title.setFont(font)#将上述设置的字体应用到标签(label_title) 上
        self.label_title.setStyleSheet("color: rgb(0, 128, 0);")#设置了标签文本颜色为白色
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)#设置标签文本的对齐方式为居中对齐
        self.label_title.setObjectName("label_title")# 为标签设置对象名称为 "label_title"
        # 设置用时文本标签
        self.label_useTime = QtWidgets.QLabel(self.centralwidget)
        self.label_useTime.setGeometry(QtCore.QRect(58, 94, 103, 51))
        font = QtGui.QFont()
        font.setFamily("华文仿宋")
        font.setPointSize(16)
        self.label_useTime.setFont(font)
        self.label_useTime.setObjectName("label_useTime")
        # 设置用时图标
        self.label_picTime = QtWidgets.QLabel(self.centralwidget)
        self.label_picTime.setGeometry(QtCore.QRect(20, 100, 29, 31))
        self.label_picTime.setStyleSheet("border-image: url(:/newPrefix/icons/net_speed.png);")
        self.label_picTime.setText("")
        self.label_picTime.setObjectName("label_picTime")
        # 设置结果图标
        self.label_picResult = QtWidgets.QLabel(self.centralwidget)
        self.label_picResult.setGeometry(QtCore.QRect(18, 175, 31, 35))
        self.label_picResult.setStyleSheet("border-image: url(:/newPrefix/icons/g1.png);")
        self.label_picResult.setText("")
        self.label_picResult.setObjectName("label_picResult")
        # 设置右上角人脸标签
        self.label_face = QtWidgets.QLabel(self.centralwidget)
        self.label_face.setGeometry(QtCore.QRect(370, 20, 420, 280))
        self.label_face.setMinimumSize(QtCore.QSize(420, 280))
        self.label_face.setMaximumSize(QtCore.QSize(420, 280))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        self.label_face.setFont(font)
        self.label_face.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_face.setStyleSheet("border-image: url(:/newPrefix/icons/new_scan.gif);")
        self.label_face.setAlignment(QtCore.Qt.AlignCenter)
        self.label_face.setObjectName("label_face")
        #设置右下角卡通画图片标签
        self.cartoon = QtWidgets.QLabel(self.centralwidget)
        self.cartoon.setGeometry(QtCore.QRect(370, 320, 420, 280))
        self.cartoon.setMinimumSize(QtCore.QSize(420, 280))
        self.cartoon.setMaximumSize(QtCore.QSize(420, 280))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        self.cartoon.setFont(font)
        self.cartoon.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cartoon.setStyleSheet("border-image: url(:/newPrefix/icons/cartoonize.gif);")
        self.cartoon.setAlignment(QtCore.Qt.AlignCenter)
        self.cartoon.setObjectName("cartoon")
        # 设置选择图片一栏的按钮标签
        self.toolButton_file = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_file.setGeometry(QtCore.QRect(8, 242, 50, 40))
        self.toolButton_file.setMinimumSize(QtCore.QSize(50, 39))
        self.toolButton_file.setMaximumSize(QtCore.QSize(50, 40))
        self.toolButton_file.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_file.setAutoFillBackground(False)
        self.toolButton_file.setStyleSheet("background-color: transparent;")
        self.toolButton_file.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/icons/recovery.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_file.setIcon(icon1)
        self.toolButton_file.setIconSize(QtCore.QSize(40, 40))
        self.toolButton_file.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.toolButton_file.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_file.setAutoRaise(False)
        self.toolButton_file.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_file.setObjectName("toolButton_file")
        # 设置选择图片一栏的文本标签
        self.textEdit_pic = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_pic.setGeometry(QtCore.QRect(58, 248, 260, 30))
        self.textEdit_pic.setMinimumSize(QtCore.QSize(260, 30))
        self.textEdit_pic.setMaximumSize(QtCore.QSize(260, 30))
        font = QtGui.QFont()
        font.setFamily("华文仿宋")
        font.setPointSize(12)
        self.textEdit_pic.setFont(font)
        self.textEdit_pic.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textEdit_pic.setStyleSheet("background-color: transparent;\n"
"border-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);")
        self.textEdit_pic.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_pic.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_pic.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textEdit_pic.setReadOnly(True)
        self.textEdit_pic.setObjectName("textEdit_pic")
        # 设置结果用时数值的标签
        self.label_time = QtWidgets.QLabel(self.centralwidget)
        self.label_time.setGeometry(QtCore.QRect(122, 100, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_time.setFont(font)
        self.label_time.setAlignment(QtCore.Qt.AlignCenter)
        self.label_time.setObjectName("label_time")
        # 设置结果表情的文本标签
        self.label_result = QtWidgets.QLabel(self.centralwidget)
        self.label_result.setGeometry(QtCore.QRect(122, 175, 223, 43))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_result.setFont(font)
        self.label_result.setStyleSheet("color: rgb(0, 189, 189);")
        self.label_result.setAlignment(QtCore.Qt.AlignCenter)
        self.label_result.setObjectName("label_result")
        # 设置左下角各表情元素标签
        self.label_outputResult = QtWidgets.QLabel(self.centralwidget)
        self.label_outputResult.setGeometry(QtCore.QRect(18, 340, 300, 250))
        self.label_outputResult.setMinimumSize(QtCore.QSize(300, 250))
        self.label_outputResult.setMaximumSize(QtCore.QSize(300, 250))
        self.label_outputResult.setStyleSheet("border-image: url(:/newPrefix/icons/ini.png);")
        self.label_outputResult.setText("")
        self.label_outputResult.setObjectName("label_outputResult")
        # 设置左侧深色背景的标签
        self.label_back1 = QtWidgets.QLabel(self.centralwidget)
        self.label_back1.setGeometry(QtCore.QRect(0, -2, 337, 661))
        self.label_back1.setStyleSheet("border-image: url(:/newPrefix/icons/new_background1.jpg);")
        self.label_back1.setText("")
        self.label_back1.setObjectName("label_back1")
        # 设置右侧浅色背景的标签
        self.label_back1_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_back1_2.setGeometry(QtCore.QRect(195, -34, 660, 707))
        self.label_back1_2.setStyleSheet("border-image: url(:/newPrefix/icons/new_background2.png);")
        self.label_back1_2.setText("")
        self.label_back1_2.setObjectName("label_back1_2")
        # 设置结果文本标签
        self.label_scanResult = QtWidgets.QLabel(self.centralwidget)
        self.label_scanResult.setGeometry(QtCore.QRect(58, 170, 97, 51))
        font = QtGui.QFont()
        font.setFamily("华文仿宋")
        font.setPointSize(16)
        self.label_scanResult.setFont(font)
        self.label_scanResult.setObjectName("label_scanResult")
        # 开始调整叠加顺序
        self.label_back1_2.raise_()  # 右侧浅色背景
        self.label_back1.raise_()  # 左侧深色背景
        self.label_title.raise_()  # 左上角标题
        self.label_useTime.raise_()  # 用时文本
        self.label_picTime.raise_()  # 用时图标
        self.label_picResult.raise_()  # 结果图标
        self.label_face.raise_()  # 右上角人脸
        self.cartoon.raise_()  # 右下角卡通人脸
        self.toolButton_file.raise_()  # 选择图片的按钮
        self.textEdit_pic.raise_()  # 选择图片的文本
        self.label_time.raise_()  # 用时的数值
        self.label_result.raise_()  # 结果表情
        self.label_outputResult.raise_()  # 右下角各表情元素
        self.label_scanResult.raise_()  # 结果文本
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionGoogle_Translate = QtWidgets.QAction(MainWindow)#创建了一个动作(QAction) 对象，该对象关联到主窗口(MainWindow)
        self.actionGoogle_Translate.setObjectName("actionGoogle_Translate")#设置动作的对象名称
        self.actionHTML_type = QtWidgets.QAction(MainWindow)#以下四行同上两行
        self.actionHTML_type.setObjectName("actionHTML_type")
        self.actionsoftware_version = QtWidgets.QAction(MainWindow)
        self.actionsoftware_version.setObjectName("actionsoftware_version")
        self.retranslateUi(MainWindow)#设置用户界面的文本翻译，确保在不同语言环境下显示适当的文本
        QtCore.QMetaObject.connectSlotsByName(MainWindow)#将信号与槽连接起来

    def retranslateUi(self, MainWindow):#重新设置用户界面中各个元素的文本内容
        _translate = QtCore.QCoreApplication.translate#将文本翻译成不同的语言
        MainWindow.setWindowTitle(_translate("MainWindow", "Emotion recongnition"))
        self.label_title.setToolTip(_translate("MainWindow", "Test Result Helper 3.3.10 author：WuXian （2019.3.13）"))
        self.label_title.setText(_translate("MainWindow", "卡通化识别"))
        self.label_useTime.setText(_translate("MainWindow", "<html><head/><body><p>用时：</p></body></html>"))
        self.label_face.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.textEdit_pic.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'华文仿宋\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Adobe Devanagari\';\">选择图片</span></p></body></html>"))
        self.label_time.setText(_translate("MainWindow", "0 s"))
        self.label_result.setText(_translate("MainWindow", "None"))
        self.label_scanResult.setText(_translate("MainWindow", "<html><head/><body><p>结果：</p></body></html>"))
        self.actionGoogle_Translate.setText(_translate("MainWindow", "Google Translate"))
        self.actionHTML_type.setText(_translate("MainWindow", "HTML type"))
        self.actionsoftware_version.setText(_translate("MainWindow", "software version"))
import image1_rc
