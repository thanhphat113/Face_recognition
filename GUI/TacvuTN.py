from PyQt5 import QtCore, QtGui, QtWidgets

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from DAO.petDAO import petDAO
from DTO.petDTO import pet
from DAO.customerDAO import customerDAO
import GUI.thongbao as tb


class Ui_Dialog(object):
    def setupUi(self, Dialog, type):
        self.type=type
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 276)
        Dialog.setMinimumSize(QtCore.QSize(400, 320))
        Dialog.setMaximumSize(QtCore.QSize(400, 320))
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 130, 91, 16))
        self.label.setObjectName("label")
        self.label_visible = QtWidgets.QLabel(Dialog)
        self.label_visible.setGeometry(QtCore.QRect(60, 90, 91, 16))
        self.label_visible.setObjectName("label_visible")
        self.label_visible.setVisible(False)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 170, 91, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(60, 210, 91, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(60, 90, 91, 16))
        self.label_4.setObjectName("label_4")
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
        self.txtName.setGeometry(QtCore.QRect(170, 130, 181, 21))
        self.txtName.setObjectName("txtName")
        self.txtColor = QtWidgets.QLineEdit(Dialog)
        self.txtColor.setGeometry(QtCore.QRect(170, 170, 181, 21))
        self.txtColor.setObjectName("txtColor")
        self.txtWeight = QtWidgets.QLineEdit(Dialog)
        self.txtWeight.setGeometry(QtCore.QRect(170, 210, 181, 21))
        self.txtWeight.setObjectName("txtWeight")
        self.btnAccept = QtWidgets.QPushButton(Dialog)
        self.btnAccept.setGeometry(QtCore.QRect(80, 260, 113, 32))
        self.btnAccept.setCheckable(True)
        self.btnAccept.setObjectName("btnAccept")
        if type == 1:
            self.btnAccept.clicked.connect(self.show_dialog_insert)
        elif type == 2:
            self.btnAccept.clicked.connect(lambda: self.show_dialog_update(self.label_visible.text()))
        self.btnDeny = QtWidgets.QPushButton(Dialog)
        self.btnDeny.setGeometry(QtCore.QRect(210, 260, 113, 32))
        self.btnDeny.setCheckable(True)
        self.btnDeny.setObjectName("btnDeny")
        self.btnDeny.toggled['bool'].connect(Dialog.close)

        self.cbMaKH = QtWidgets.QComboBox(Dialog)
        self.cbMaKH.setGeometry(QtCore.QRect(170, 90, 181, 22))
        self.cbMaKH.setObjectName("cbMaKH")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        self._translate = QtCore.QCoreApplication.translate
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Tên thú nuôi"))
        self.label_2.setText(_translate("Dialog", "Màu lông"))
        self.label_3.setText(_translate("Dialog", "Cân nặng"))
        self.label_4.setText(_translate("Dialog", "Khách hàng"))
        self.title.setText(_translate("Dialog", "THÊM THÚ NUÔI"))
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
        ten = self.txtName.text()
        cannang = self.txtWeight.text()
        mau = self.txtColor.text()
        khachhang = self.cbMaKH.currentIndex() + 1
        dao = petDAO()
        if ten:
            subPet = pet("",ten, mau, cannang, khachhang)
            result = dao.insert(subPet)
            if result == "Thêm thành công !!!!":
                self.txtName.setText("")
                self.txtWeight.setText("")
                self.txtColor.setText("")
                self.cbMaKH.setCurrentText("")
            return result 
        else: 
            return 'Tên thú nuôi không được rỗng !!!!'
        
    def update_data(self, id):
        cus = customerDAO()
        ten = self.txtName.text()
        cannang = self.txtWeight.text()
        mau = self.txtColor.text()
        khachhang = self.cbMaKH.currentText()
        kh = cus.findByName(khachhang)
        dao = petDAO()
        if ten:
            subPet = pet(id, ten, mau, cannang, kh.get_makh())
            return dao.update(subPet)  
        else: 
            return 'Tên thú nuôi không được rỗng !!!!'


