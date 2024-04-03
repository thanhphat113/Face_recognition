from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from DAO.taikhoanDAO import taikhoanDAO
import GUI.thongbao as tb
import GUI.sidebar as sb


class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("Phòng khám thú y")
                MainWindow.resize(417, 462)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
                MainWindow.setSizePolicy(sizePolicy)
                MainWindow.setMinimumSize(QtCore.QSize(417, 462))
                MainWindow.setMaximumSize(QtCore.QSize(417, 462))
                MainWindow.setStyleSheet("\n"
        "background-repeat: no-repeat;")
                MainWindow.setDocumentMode(False)
                self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
                self.centralwidget.setStyleSheet("")
                self.centralwidget.setObjectName("centralwidget")
                self.widget = QtWidgets.QWidget(parent=self.centralwidget)
                self.widget.setGeometry(QtCore.QRect(0, 0, 417, 462))
                self.widget.setMinimumSize(QtCore.QSize(417, 462))
                self.widget.setStyleSheet("QWidget{\n"
        "    background-image: url(img/login.png);\n"
        "}\n"
        "")
                self.widget.setObjectName("widget")
                self.label = QtWidgets.QLabel(parent=self.widget)
                self.label.setGeometry(QtCore.QRect(80, 40, 251, 61))
                self.label.setStyleSheet("font: 75 40pt \"Futura\";\n"
        "color: rgb(255, 246, 244);")
                self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                self.label.setObjectName("label")
                self.label_2 = QtWidgets.QLabel(parent=self.widget)
                self.label_2.setGeometry(QtCore.QRect(60, 340, 91, 16))
                self.label_2.setStyleSheet("background-image: url(img/login-back.png);\n"
        "")
                self.label_2.setObjectName("label_2")
                self.label_3 = QtWidgets.QLabel(parent=self.widget)
                self.label_3.setGeometry(QtCore.QRect(60, 370, 91, 16))
                self.label_3.setStyleSheet("background-image: url(img/login-back.png);\n"
        "")
                self.label_3.setObjectName("label_3")
                self.txtUser = QtWidgets.QLineEdit(parent=self.widget)
                self.txtUser.setGeometry(QtCore.QRect(170, 340, 181, 21))
                self.txtUser.setStyleSheet("background-image: url(img/white.png);")
                self.txtUser.setText("")
                self.txtUser.setObjectName("lineEdit")
                self.txtPass = QtWidgets.QLineEdit(parent=self.widget)
                self.txtPass.setGeometry(QtCore.QRect(170, 370, 181, 21))
                self.txtPass.setStyleSheet("\n"
        "background-image: url(img/white.png);")
                self.txtPass.setText("")
                self.txtPass.setObjectName("lineEdit_2")
                self.txtPass.setEchoMode(QLineEdit.Password)
                self.btnAccept = QtWidgets.QPushButton(parent=self.widget)
                self.btnAccept.setGeometry(QtCore.QRect(80, 410, 113, 32))
                self.btnAccept.setStyleSheet("background-image: url(img/login-back.png);\n"
        "border: 1px solid black;\n"
        "border-radius:10px;\n"
        "")
                self.btnAccept.setCheckable(True)
                self.btnAccept.setDefault(True)
                self.btnAccept.setFlat(False)
                self.btnAccept.setObjectName("btnAccept")
                self.btnDeny = QtWidgets.QPushButton(parent=self.widget)
                self.btnDeny.setGeometry(QtCore.QRect(220, 410, 113, 32))
                self.btnDeny.setStyleSheet("background-image: url(img/login-back.png);\n"
        "border: 1px solid black;\n"
        "border-radius:10px;")
                self.btnDeny.setCheckable(True)
                self.btnDeny.setObjectName("btnDeny")
                MainWindow.setCentralWidget(self.centralwidget)
                
                self.retranslateUi(MainWindow)
                self.btnDeny.toggled['bool'].connect(MainWindow.close) # type: ignore
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
                self._translate = QtCore.QCoreApplication.translate
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "Phòng khám thú y"))
                self.label.setText(_translate("MainWindow", "Phòng khám"))
                self.label_2.setText(_translate("MainWindow", "Tên đăng nhập"))
                self.label_3.setText(_translate("MainWindow", "Mật khẩu"))
                self.btnAccept.setText(_translate("MainWindow", "Đăng nhập"))
                self.btnAccept.enterEvent = self.enter_accept_event
                self.btnAccept.leaveEvent = self.leave_accept_event
                self.btnAccept.clicked.connect(self.show_GUI)
                self.btnDeny.setText(_translate("MainWindow", "Huỷ"))
                self.btnDeny.enterEvent = self.enter_cancel_event
                self.btnDeny.leaveEvent = self.leave_cancel_event
        
        def enter_accept_event(self, event):
                self.btnAccept.setStyleSheet("font-weight:bold;background-image: url(img/login-back.png);\nborder: 2px solid black;\nborder-radius:10px;\n")
                event.accept()
                
        def leave_accept_event(self, event):
                self.btnAccept.setStyleSheet("background-image: url(img/login-back.png);\nborder: 1px solid black;\nborder-radius:10px;")  # Xóa bất kỳ styleSheet nào được thiết lập
                event.accept()
                
        def enter_cancel_event(self, event):
                self.btnDeny.setStyleSheet("font-weight:bold;background-image: url(img/login-back.png);\nborder: 2px solid black;\nborder-radius:10px;\n")
                event.accept()
                
        def leave_cancel_event(self, event):
                self.btnDeny.setStyleSheet("background-image: url(img/login-back.png);\nborder: 1px solid black;\nborder-radius:10px;")  # Xóa bất kỳ styleSheet nào được thiết lập
                event.accept()
                
        def show_dialog_insert(self):
                Dialog = QtWidgets.QDialog()
                ui = tb.Ui_Dialog()
                ui.setupUi(Dialog)
                ui.label.setText(self._translate("Dialog", self.checkLogin()))
                Dialog.exec_()
        
        def checkLogin(self):
                username = self.txtUser.text()
                password = self.txtPass.text()
                tkDAO = taikhoanDAO()
                taikhoan = tkDAO.checkPassword(username, password)
                # if taikhoan:
                #         if taikhoan.maloai == 1:
                                
                #         elif taikhoan.maloai == 2:
        
        def show_GUI(self):
                print("Đã bấm")
                sidebar = QtWidgets.QMainWindow()
                uisb = sb.Ui_MainWindow()
                uisb.setupUi(sidebar)
                print(sidebar.show())
                
if __name__=="__main__":
        app = QtWidgets.QApplication(sys.argv)
        sidebar = QtWidgets.QMainWindow()
        sbui = sb.Ui_MainWindow()
        sbui.setupUi(sidebar)
        sidebar.show()
        sys.exit(app.exec()) 
                
                

                
                
                
