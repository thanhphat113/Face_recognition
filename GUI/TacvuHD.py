from PyQt5 import QtCore, QtGui, QtWidgets

import time
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from DAO.billDAO import billDAO
from DTO.billDTO import bill
import GUI.thongbao as tb


class Ui_Dialog(object):
    def setupUi(self, Dialog, type):
        self.type=type
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 276)
        Dialog.setMinimumSize(QtCore.QSize(400, 276))
        Dialog.setMaximumSize(QtCore.QSize(400, 276))
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 90, 91, 16))
        self.label.setObjectName("label")
        self.label_visible = QtWidgets.QLabel(Dialog)
        self.label_visible.setGeometry(QtCore.QRect(60, 90, 91, 16))
        self.label_visible.setObjectName("label_visible")
        self.label_visible.setVisible(False)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 130, 91, 16))
        self.label_2.setObjectName("label_2")
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
        self.txtTime = QtWidgets.QLineEdit(Dialog)
        self.txtTime.setGeometry(QtCore.QRect(170, 90, 181, 21))
        self.txtTime.setObjectName("txtTime")
        
        self.txtPrice = QtWidgets.QLineEdit(Dialog)
        self.txtPrice.setGeometry(QtCore.QRect(170, 130, 181, 21))
        self.txtPrice.setObjectName("txtPrice")
        self.btnAccept = QtWidgets.QPushButton(Dialog)
        self.btnAccept.setGeometry(QtCore.QRect(80, 220, 113, 32))
        self.btnAccept.setCheckable(True)
        self.btnAccept.setObjectName("btnAccept")
        if type == 1:
            self.btnAccept.clicked.connect(self.show_dialog_insert)
        elif type == 2:
            self.btnAccept.clicked.connect(lambda: self.show_dialog_update(self.label_visible.text()))
        self.btnDeny = QtWidgets.QPushButton(Dialog)
        self.btnDeny.setGeometry(QtCore.QRect(210, 220, 113, 32))
        self.btnDeny.setCheckable(True)
        self.btnDeny.setObjectName("btnDeny")
        self.btnDeny.toggled['bool'].connect(Dialog.close)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        self._translate = QtCore.QCoreApplication.translate
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Ngày tạo"))
        self.label_2.setText(_translate("Dialog", "Tổng tiền"))
        self.title.setText(_translate("Dialog", "SỬA THÔNG TIN"))
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
        thoigian = time.localtime()
        self.txtTime.setText(f"{thoigian.tm_year}-{thoigian.tm_mon}-{thoigian.tm_mday}")

        ngay = self.txtTime.text()
        gia = self.txtPrice.text()
        dao = billDAO()
        if gia:
            subPet = bill("", ngay, gia, "", "")
            result = dao.insert(subPet)
            if result == "Thêm thành công !!!!":
                self.txtTime.setText("")
                self.txtPrice.setText("")
            return result 
        else: 
            return 'Tổng tiền không được rỗng !!!!'
        
    def update_data(self, id):
        ngay = self.txtTime.text()
        gia = self.txtPrice.text()
        dao = billDAO()
        if ngay and gia:
            subPet = bill(id, ngay, gia, "", "")
            return dao.update(subPet)  
        else: 
            return 'Ngày tạo và tổng tiền không được rỗng !!!!'

