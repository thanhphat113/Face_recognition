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
        self.txtMaNV = QtWidgets.QLineEdit(Dialog)
        self.txtMaNV.setGeometry(QtCore.QRect(170, 90, 181, 22))
        self.txtMaNV.setObjectName("txtMaNV")
        self.txtMaNV.setEnabled(False)
        self.txtName = QtWidgets.QLineEdit(Dialog)
        self.txtName.setGeometry(QtCore.QRect(170, 170, 181, 21))
        self.txtName.setObjectName("txtName")
        self.txtPwd = QtWidgets.QLineEdit(Dialog)
        self.txtPwd.setGeometry(QtCore.QRect(170, 210, 181, 21))
        self.txtPwd.setObjectName("txtPwd")
        self.cbbStatus = QtWidgets.QComboBox(Dialog)
        self.cbbStatus.addItem("Không hoạt động")
        self.cbbStatus.addItem("Hoạt động")
        self.cbbStatus.setGeometry(QtCore.QRect(170, 250, 181, 21))
        self.cbbStatus.setObjectName("cbbStatus")
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
        
    def update_data(self, id):
        conn = db.connect_to_database()
        try:
            name = self.txtName.text()
            pwd = self.txtPwd.text()
            matk = self.label_visible.text()
            status = self.cbbStatus.currentIndex()
            accType = self.cbMaLTK.currentIndex()+1

            conn.connect()
            query = f"update TaiKhoan set username = '{name}',password = '{pwd}', trangthai = '{status}', maloai ='{accType}' where matk = '{matk}'"
            db.execute_query(conn,query)
            return "Cập nhật thành công"
        except mysql.connector.Error as error:
            return f'Lỗi: {error}'
        finally:
            conn.close()
        

