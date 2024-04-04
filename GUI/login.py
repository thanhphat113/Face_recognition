# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/login.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit


class Ui_login_form(object):
        def setupUi(self, login_form):
                login_form.setObjectName("login_form")
                login_form.resize(417, 468)
                login_form.setMinimumSize(QtCore.QSize(417, 462))
                login_form.setMaximumSize(QtCore.QSize(417, 462))
                login_form.setStyleSheet("\n"
                "background-repeat: no-repeat;")
                self.gridLayout = QtWidgets.QGridLayout(login_form)
                self.gridLayout.setContentsMargins(0, 0, 0, 0)
                self.gridLayout.setObjectName("gridLayout")
                self.widget = QtWidgets.QWidget(login_form)
                self.widget.setMinimumSize(QtCore.QSize(417, 462))
                self.widget.setStyleSheet("")
                self.widget.setObjectName("widget")
                self.widget.setStyleSheet("QWidget{\n"
                "    background-image: url(img/login.png);\n"
                "}\n"
                "")
                self.label = QtWidgets.QLabel(self.widget)
                self.label.setGeometry(QtCore.QRect(0, 40, 417, 61))
                self.label.setMinimumSize(QtCore.QSize(0, 0))
                self.label.setStyleSheet("font: 75 40pt \"Futura\";\n"
        "color: rgb(255, 246, 244);")
                self.label.setAlignment(QtCore.Qt.AlignCenter)
                self.label.setObjectName("label")
                self.label_2 = QtWidgets.QLabel(self.widget)
                self.label_2.setGeometry(QtCore.QRect(60, 340, 91, 16))
                self.label_2.setStyleSheet("background-image: url(:/newPrefix/login-back.png);\n"
        "")
                self.label_2.setObjectName("label_2")
                self.label_3 = QtWidgets.QLabel(self.widget)
                self.label_3.setGeometry(QtCore.QRect(60, 370, 91, 16))
                self.label_3.setStyleSheet("background-image: url(:/newPrefix/login-back.png);\n"
        "")
                self.label_3.setObjectName("label_3")
                self.txtUser = QtWidgets.QLineEdit(self.widget)
                self.txtUser.setGeometry(QtCore.QRect(170, 340, 181, 21))
                self.txtUser.setStyleSheet("background-image: url(:/newPrefix/white.png);")
                self.txtUser.setText("")
                self.txtUser.setObjectName("lineEdit")
                self.txtPass = QtWidgets.QLineEdit(self.widget)
                self.txtPass.setGeometry(QtCore.QRect(170, 370, 181, 21))
                self.txtPass.setStyleSheet("\n"
        "background-image: url(:/newPrefix/white.png);")
                self.txtPass.setText("")
                self.txtPass.setObjectName("lineEdit_2")
                self.txtPass.setEchoMode(QLineEdit.Password)
                self.btnLogin = QtWidgets.QPushButton(self.widget)
                self.btnLogin.setGeometry(QtCore.QRect(80, 410, 113, 32))
                self.btnLogin.setStyleSheet("background-image: url(:/newPrefix/login-back.png);\n"
        "border: 1px solid black;\n"
        "border-radius:10px;\n"
        "")
                self.btnLogin.setCheckable(True)
                self.btnLogin.setDefault(True)
                self.btnLogin.setFlat(False)
                self.btnLogin.setObjectName("btnLogin")
                self.btnCancel = QtWidgets.QPushButton(self.widget)
                self.btnCancel.setGeometry(QtCore.QRect(220, 410, 113, 32))
                self.btnCancel.setStyleSheet("background-image: url(:/newPrefix/login-back.png);\n"
        "border: 1px solid black;\n"
        "border-radius:10px;")
                self.btnCancel.setCheckable(True)
                self.btnCancel.toggled['bool'].connect(login_form.close)
                self.btnCancel.setObjectName("btnCancel")
                self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

                self.retranslateUi(login_form)
                QtCore.QMetaObject.connectSlotsByName(login_form)

        def retranslateUi(self, login_form):
                _translate = QtCore.QCoreApplication.translate
                login_form.setWindowTitle(_translate("login_form", "Form"))
                self.label.setText(_translate("login_form", "Phòng khám"))
                self.label_2.setText(_translate("login_form", "Tên đăng nhập"))
                self.label_3.setText(_translate("login_form", "Mật khẩu"))
                self.btnLogin.setText(_translate("login_form", "Đăng nhập"))
                self.btnLogin.enterEvent = self.enter_accept_event
                self.btnLogin.leaveEvent = self.leave_accept_event
                self.btnCancel.setText(_translate("login_form", "Huỷ"))
                self.btnCancel.enterEvent = self.enter_cancel_event
                self.btnCancel.leaveEvent = self.leave_cancel_event
                
        def enter_accept_event(self, event):
                self.btnLogin.setStyleSheet("font-weight:bold;background-image: url(img/login-back.png);\nborder: 2px solid black;\nborder-radius:10px;\n")
                event.accept()

        def leave_accept_event(self, event):
                self.btnLogin.setStyleSheet("background-image: url(img/login-back.png);\nborder: 1px solid black;\nborder-radius:10px;")  # Xóa bất kỳ styleSheet nào được thiết lập
                event.accept()

        def enter_cancel_event(self, event):
                self.btnCancel.setStyleSheet("font-weight:bold;background-image: url(img/login-back.png);\nborder: 2px solid black;\nborder-radius:10px;\n")
                event.accept()

        def leave_cancel_event(self, event):
                self.btnCancel.setStyleSheet("background-image: url(img/login-back.png);\nborder: 1px solid black;\nborder-radius:10px;")  # Xóa bất kỳ styleSheet nào được thiết lập
                event.accept()
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login_form = QtWidgets.QWidget()
    ui = Ui_login_form()
    ui.setupUi(login_form)
    login_form.show()
    sys.exit(app.exec_())
