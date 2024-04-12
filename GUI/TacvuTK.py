from PyQt5 import QtCore, QtGui, QtWidgets

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from DAO.taikhoanDAO import taikhoanDAO
from  DAO.employeeDAO import employeeDAO
from DTO.employeeDTO import employee
from DTO.taikhoanDTO import taikhoan
import GUI.thongbao as tb
import DAO.database as db
import mysql.connector


class Ui_Dialog(object):
    def setupUi(self, Dialog, type):
        self.type=type
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 276)
        Dialog.setMinimumSize(QtCore.QSize(400, 350))
        Dialog.setMaximumSize(QtCore.QSize(400, 350))
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 170, 91, 16))
        self.label.setObjectName("label")
        self.label_visible = QtWidgets.QLabel(Dialog)
        self.label_visible.setGeometry(QtCore.QRect(60, 90, 91, 16))
        self.label_visible.setObjectName("label_visible")
        self.label_visible.setVisible(False)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 210, 91, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(60, 250, 91, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(60, 130, 91, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(60, 90, 91, 16))
        self.label_5.setObjectName("label_5")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(0, -1, 401, 61))
        self.widget.setStyleSheet("background-color: rgb(0, 255, 244);\n"
"border:1px solid black;")
        self.widget.setObjectName("widget")
        self.title = QtWidgets.QLabel(self.widget)
        self.title.setGeometry(QtCore.QRect(70, 10, 500, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setStyleSheet("border:none;")
        self.title.setAlignment(QtCore.Qt.AlignLeft)
        self.title.setObjectName("title")
        self.txtName = QtWidgets.QLineEdit(Dialog)
        self.txtName.setGeometry(QtCore.QRect(170, 170, 181, 21))
        self.txtName.setObjectName("txtName")
        self.txtPwd = QtWidgets.QLineEdit(Dialog)
        self.txtPwd.setGeometry(QtCore.QRect(170, 210, 181, 21))
        self.txtPwd.setObjectName("txtPwd")
        self.txtStatus = QtWidgets.QLineEdit(Dialog)
        self.txtStatus.setGeometry(QtCore.QRect(170, 250, 181, 21))
        self.txtStatus.setObjectName("txtStatus")
        self.btnAccept = QtWidgets.QPushButton(Dialog)
        self.btnAccept.setGeometry(QtCore.QRect(80, 300, 113, 32))
        self.btnAccept.setCheckable(True)
        self.btnAccept.setObjectName("btnAccept")
        if type == 1:
            self.btnAccept.clicked.connect(self.show_dialog_insert)
        elif type == 2:
            self.btnAccept.clicked.connect(lambda: self.show_dialog_update(self.label_visible.text()))
        self.btnDeny = QtWidgets.QPushButton(Dialog)
        self.btnDeny.setGeometry(QtCore.QRect(210, 300, 113, 32))
        self.btnDeny.setCheckable(True)
        self.btnDeny.setObjectName("btnDeny")
        self.btnDeny.toggled['bool'].connect(Dialog.close)

        self.cbMaLTK = QtWidgets.QComboBox(Dialog)
        self.cbMaLTK.setGeometry(QtCore.QRect(170, 130, 181, 22))
        self.cbMaLTK.setObjectName("cbMaLTK")

        self.cbMaNV = QtWidgets.QComboBox(Dialog)
        self.cbMaNV.setGeometry(QtCore.QRect(170, 90, 181, 22))
        self.cbMaNV.setObjectName("cbMaNV")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        self._translate = QtCore.QCoreApplication.translate
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Username"))
        self.label_2.setText(_translate("Dialog", "Password"))
        self.label_3.setText(_translate("Dialog", "Trạng thái"))
        self.label_4.setText(_translate("Dialog", "Loại tài khoản"))
        self.label_5.setText(_translate("Dialog", "Nhân viên"))
        self.title.setText(_translate("Dialog", "THÊM TÀI KHOẢN"))
        self.btnAccept.setText(_translate("Dialog", "Xác nhận"))
        self.btnDeny.setText(_translate("Dialog", "Huỷ"))
        
    def show_dialog_update(self,id):
        Dialog = QtWidgets.QDialog()
        ui = tb.Ui_Dialog()
        ui.setupUi(Dialog)
        ui.label.setText(self._translate("Dialog", self.update_data(id)))
        Dialog.exec_()
        
    def show_dialog_insert(self):
        Dialog = QtWidgets.QDialog()
        ui = tb.Ui_Dialog()
        ui.setupUi(Dialog)
        ui.label.setText(self._translate("Dialog", self.insert_data()))
        Dialog.exec_()
        
        
    def insert_data(self):
        name = self.txtName.text()
        pwd = self.txtPwd.text()
        status = self.txtStatus.text()
        accType = self.cbMaLTK.currentIndex()+1

        accDAO = taikhoanDAO()
        if name and pwd:
            if int(status) == 0 or int(status) == 1:
                account = taikhoan("", name, pwd, status, accType)
                result = accDAO.insert(account)
                if result == "Thêm thành công !!!!":
                    self.txtName.setText("")
                    self.txtPwd.setText("")
                    self.txtStatus.setText("")
                    self.cbMaLTK.setCurrentText("")
                return result
            else:
                return 'Trạng thái phải có giá trị là 1 (hoạt động) hoặc 0 (không hoạt động) !!!!'
        else: 
            return 'Username và Password không được rỗng !!!!'
        
    def update_data(self, id):
        conn = db.connect_to_database()
        try:
            name = self.txtName.text()
            pwd = self.txtPwd.text()
            status = self.txtStatus.text()
            accType = self.cbMaLTK.currentIndex()+1
            empID = self.cbMaNV.currentIndex()+1

            conn.connect()
            query = f"update nhanvien set matk = '{id}' where manv = '{empID}'"
            db.execute_query(conn,query)

            accDAO = taikhoanDAO()
            if name and pwd:
                if status == "Hoạt động":
                    status = 1
                elif status == "Không hoạt động":
                    status = 0
                elif status != "1" and status != "0":
                    return 'Trạng thái phải có giá trị là 1 (hoạt động) hoặc 0 (không hoạt động) !!!!'
                account = taikhoan(id, name, pwd, status, accType)
                return accDAO.update(account)
            else: 
                return 'Username và Password không được rỗng !!!!'
        except mysql.connector.Error as error:
            return f'Lỗi: {error}'
        finally:
            conn.close()
        

