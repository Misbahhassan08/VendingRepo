# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'onescreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1921, 972)
        MainWindow.setMinimumSize(QtCore.QSize(800, 0))
        MainWindow.setStyleSheet("background-color:black")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMaximumSize(QtCore.QSize(1910, 965))
        self.widget.setStyleSheet("background-color:black")
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.tool_bar = QtWidgets.QFrame(self.widget)
        self.tool_bar.setMinimumSize(QtCore.QSize(250, 0))
        self.tool_bar.setMaximumSize(QtCore.QSize(200, 1000))
        self.tool_bar.setStyleSheet("background-color:black")
        self.tool_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tool_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tool_bar.setObjectName("tool_bar")
        self.comboBox = QtWidgets.QComboBox(self.tool_bar)
        self.comboBox.setGeometry(QtCore.QRect(10, 0, 245, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QtCore.QSize(245, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("background-color:white")
        self.comboBox.setMaxVisibleItems(8)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.tool_bar)
        self.pushButton.setGeometry(QtCore.QRect(10, 40, 245, 34))
        self.pushButton.setMinimumSize(QtCore.QSize(245, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color:white")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.tool_bar, 0, 1, 1, 1)
        self.screen_frame_1 = QtWidgets.QFrame(self.widget)
        self.screen_frame_1.setMinimumSize(QtCore.QSize(0, 0))
        self.screen_frame_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.screen_frame_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.screen_frame_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.screen_frame_1.setObjectName("screen_frame_1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.screen_frame_1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.screen_1 = QtWidgets.QLabel(self.screen_frame_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.screen_1.sizePolicy().hasHeightForWidth())
        self.screen_1.setSizePolicy(sizePolicy)
        self.screen_1.setMinimumSize(QtCore.QSize(0, 0))
        self.screen_1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.screen_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.screen_1.setStyleSheet("background-color:white")
        self.screen_1.setLineWidth(1)
        self.screen_1.setText("")
        self.screen_1.setScaledContents(True)
        self.screen_1.setAlignment(QtCore.Qt.AlignCenter)
        self.screen_1.setObjectName("screen_1")
        self.verticalLayout.addWidget(self.screen_1)
        self.label = QtWidgets.QLabel(self.screen_frame_1)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label.setStyleSheet("color:white")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout.addWidget(self.screen_frame_1, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setItemText(0, _translate("MainWindow", "You want to play video"))
        self.comboBox.setItemText(1, _translate("MainWindow", "You want to play camera"))
        self.pushButton.setText(_translate("MainWindow", "Set Screens"))
        self.label.setText(_translate("MainWindow", "Status:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())