# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Admin_Detail.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from ast import Delete
from tkinter import dialog
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1079, 487)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 20, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(35, 91, 1001, 311))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(970, 30, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.statuslabel = QtWidgets.QLabel(Dialog)
        self.statuslabel.setGeometry(QtCore.QRect(35,420, 291, 51)) 
        font = QtGui.QFont()
        self.statuslabel.setFont(font)
        self.statuslabel.setObjectName("label_3")
        self.addbutton = QtWidgets.QPushButton(Dialog)
        self.addbutton.setGeometry(QtCore.QRect(600, 430, 112, 34))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.addbutton.setFont(font)
        self.addbutton.setObjectName("pushButton")
        self.deletebutton = QtWidgets.QPushButton(Dialog)
        self.deletebutton.setGeometry(QtCore.QRect(750, 430, 112, 34))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.deletebutton.setFont(font)
        self.deletebutton.setObjectName("pushButton")
        self.updatebutton = QtWidgets.QPushButton(Dialog)
        self.updatebutton.setGeometry(QtCore.QRect(900, 430, 112, 34))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.updatebutton.setFont(font)
        self.updatebutton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Admin Detail"))
        self.label.setText(_translate("Dialog", "Welcome Dear "))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Dialog", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Dialog", "4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("Dialog", "5"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("Dialog", "6"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "User ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "User Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Password"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "First Name"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Last Name"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "Subject ID"))
        self.label_2.setText(_translate("Dialog", "Admin"))
        self.statuslabel.setText(_translate("Dialog", "Status : "))
        self.addbutton.setText(_translate("Login", "Add"))
        self.deletebutton.setText(_translate("Login", "Delete"))
        self.updatebutton.setText(_translate("Login", "Update"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
