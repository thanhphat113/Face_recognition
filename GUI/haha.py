# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/thongtin.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(420, 300)
        Dialog.setMinimumSize(QtCore.QSize(420, 300))
        Dialog.setMaximumSize(QtCore.QSize(420, 300))
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(0, 0, 421, 71))
        self.widget.setStyleSheet("QWidget{\n"
"    background-color: rgb(65, 255, 245);\n"
"    border:1px solid black\n"
"}\n"
"QLabel{\n"
"         border:none\n"
"}")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(100, 20, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 110, 91, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(70, 150, 91, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(70, 190, 91, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(180, 110, 181, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 150, 181, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(180, 190, 181, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(90, 240, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 240, 113, 32))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "THÔNG TIN TÀI KHOẢN"))
        self.label_2.setText(_translate("Dialog", "Tên nhân viên"))
        self.label_3.setText(_translate("Dialog", "Số điện thoại"))
        self.label_4.setText(_translate("Dialog", "Email"))
        self.pushButton.setText(_translate("Dialog", "Đổi mật khẩu"))
        self.pushButton_2.setText(_translate("Dialog", "Huỷ"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
