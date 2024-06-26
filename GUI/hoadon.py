# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/hoadon.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QTableView

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import GUI.TacvuHD as tv
import GUI.thongbao as tb
from  GUI.hoadon_dialog import Ui_hoadon_dialog
from  GUI.cthd_dialog import Ui_cthd_dialog
from  DAO.billDAO import billDAO
from  DAO.employeeDAO import employeeDAO
from  DAO.customerDAO import customerDAO
from  DAO.serviceDAO import serviceDAO
from  DAO.cthdDAO import cthdDAO
from  DAO.medicineDAO import medicineDAO
from  DTO.billDTO import bill
from  DTO.cthdDTO import CTHD
import GUI.mesage_box as msg
from GUI.cthd_dialog import Ui_cthd_dialog

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(875, 561)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.gridLayout_3 = QtWidgets.QGridLayout(Form)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setHorizontalSpacing(7)
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.groupBox_2 = QtWidgets.QGroupBox(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setContentsMargins(-1, 20, -1, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.txtSearchHD = QtWidgets.QLineEdit(self.groupBox_2)
        self.txtSearchHD.setMinimumSize(QtCore.QSize(0, 32))
        self.txtSearchHD.setObjectName("txtSearchHD")
        self.horizontalLayout_5.addWidget(self.txtSearchHD)
        self.cbSearchHD = QtWidgets.QComboBox(self.groupBox_2)
        self.cbSearchHD.setMinimumSize(QtCore.QSize(0, 32))
        self.cbSearchHD.setObjectName("cbSearchHD")
        self.cbSearchHD.addItem("")
        self.cbSearchHD.addItem("")
        self.cbSearchHD.addItem("")
        self.horizontalLayout_5.addWidget(self.cbSearchHD)
        self.btnSearchHD = QtWidgets.QPushButton(self.groupBox_2)
        self.btnSearchHD.setMinimumSize(QtCore.QSize(40, 40))
        self.btnSearchHD.setStyleSheet("background-color: #BDD5D7;")
        self.btnSearchHD.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui\\../img/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSearchHD.setIcon(icon)
        self.btnSearchHD.setObjectName("btnSearchHD")
        self.horizontalLayout_5.addWidget(self.btnSearchHD)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.table_hoadon = QtWidgets.QTableWidget(self.groupBox_2)
        self.table_hoadon.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_hoadon.setObjectName("table_hoadon")
        self.table_hoadon.setColumnCount(5)
        self.table_hoadon.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_hoadon.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_hoadon.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_hoadon.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_hoadon.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_hoadon.setHorizontalHeaderItem(4, item)
        self.table_hoadon.horizontalHeader().setStretchLastSection(True)
        self.table_hoadon.verticalHeader().setVisible(False)
        self.verticalLayout_3.addWidget(self.table_hoadon)
        self.horizontalLayout_4.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setContentsMargins(-1, 20, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.btnAddCTHD = QtWidgets.QPushButton(self.groupBox)
        self.btnAddCTHD.setMinimumSize(QtCore.QSize(40, 40))
        self.btnAddCTHD.setStyleSheet("background-color: rgb(159, 255, 153);\n"
"")
        self.btnAddCTHD.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ui\\../img/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAddCTHD.setIcon(icon1)
        self.btnAddCTHD.setObjectName("btnAddCTHD")
        self.horizontalLayout_6.addWidget(self.btnAddCTHD)
        self.btnEditCTHD = QtWidgets.QPushButton(self.groupBox)
        self.btnEditCTHD.setMinimumSize(QtCore.QSize(40, 40))
        self.btnEditCTHD.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"")
        self.btnEditCTHD.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("ui\\../img/edit_48px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnEditCTHD.setIcon(icon2)
        self.btnEditCTHD.setObjectName("btnEditCTHD")
        self.horizontalLayout_6.addWidget(self.btnEditCTHD)
        self.btnDeleteCTHD = QtWidgets.QPushButton(self.groupBox)
        self.btnDeleteCTHD.setMinimumSize(QtCore.QSize(40, 40))
        self.btnDeleteCTHD.setStyleSheet("background-color: rgb(255, 124, 125);\n"
"\n"
"")
        self.btnDeleteCTHD.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("ui\\../img/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnDeleteCTHD.setIcon(icon3)
        self.btnDeleteCTHD.setObjectName("btnDeleteCTHD")
        self.horizontalLayout_6.addWidget(self.btnDeleteCTHD)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.table_cthd = QtWidgets.QTableWidget(self.groupBox)
        self.table_cthd.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_cthd.setObjectName("table_cthd")
        self.table_cthd.setColumnCount(5)
        self.table_cthd.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_cthd.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_cthd.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_cthd.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_cthd.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_cthd.setHorizontalHeaderItem(4, item)
        self.table_cthd.horizontalHeader().setStretchLastSection(True)
        self.table_cthd.verticalHeader().setVisible(False)
        self.verticalLayout_2.addWidget(self.table_cthd)
        self.horizontalLayout_4.addWidget(self.groupBox)
        self.gridLayout_3.addWidget(self.widget_2, 1, 0, 1, 1)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.widget.setStyleSheet("QWidget{\n"
"background-color: rgb(133, 255, 246);    border:1px solid black\n"
"}\n"
"QLabel{\n"
"    border:none\n"
"}\n"
"\n"
"\n"
"")
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setMinimumSize(QtCore.QSize(0, 90))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout_3.addWidget(self.widget, 0, 0, 1, 1)
        self.widget_3 = QtWidgets.QWidget(Form)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_2.setContentsMargins(11, -1, -1, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(8, 5, 8, 5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(218, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btnAdd = QtWidgets.QPushButton(self.widget_3)
        self.btnAdd.setMinimumSize(QtCore.QSize(100, 30))
        self.btnAdd.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAdd.setStyleSheet("background-color: rgb(159, 255, 153);")
        self.btnAdd.setIcon(icon1)
        self.btnAdd.setIconSize(QtCore.QSize(20, 20))
        self.btnAdd.setFlat(False)
        self.btnAdd.setObjectName("btnAdd")
        self.horizontalLayout.addWidget(self.btnAdd)
        self.btnEdit = QtWidgets.QPushButton(self.widget_3)
        self.btnEdit.setMinimumSize(QtCore.QSize(100, 30))
        self.btnEdit.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"")
        self.btnEdit.setIcon(icon2)
        self.btnEdit.setObjectName("btnEdit")
        self.horizontalLayout.addWidget(self.btnEdit)
        self.btnDelete = QtWidgets.QPushButton(self.widget_3)
        self.btnDelete.setMinimumSize(QtCore.QSize(100, 30))
        self.btnDelete.setStyleSheet("background-color: rgb(255, 124, 125);\n"
"\n"
"")
        self.btnDelete.setIcon(icon3)
        self.btnDelete.setObjectName("btnDelete")
        self.horizontalLayout.addWidget(self.btnDelete)
        self.btnReset = QtWidgets.QPushButton(self.widget_3)
        self.btnReset.setMinimumSize(QtCore.QSize(100, 30))
        self.btnReset.setStyleSheet("background-color: #BDD5D7;")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("ui\\../img/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnReset.setIcon(icon4)
        self.btnReset.setObjectName("btnReset")
        self.horizontalLayout.addWidget(self.btnReset)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.widget_3, 2, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox_2.setTitle(_translate("Form", "THÔNG TIN HÓA ĐƠN"))
        self.cbSearchHD.setItemText(0, _translate("Form", "Mã hóa đơn"))
        self.cbSearchHD.setItemText(1, _translate("Form", "Mã nhân viên"))
        self.cbSearchHD.setItemText(2, _translate("Form", "Mã khách hàng"))
        item = self.table_hoadon.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Mã hóa đơn"))
        item = self.table_hoadon.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Mã nhân viên"))
        item = self.table_hoadon.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Mã khách hàng"))
        item = self.table_hoadon.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Ngày tạo"))
        item = self.table_hoadon.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Tổng tiền"))
        self.groupBox.setTitle(_translate("Form", "CHI TIẾT HÓA ĐƠN"))
        item = self.table_cthd.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Mã chi tiết hóa đơn"))
        item = self.table_cthd.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Mã hóa đơn"))
        item = self.table_cthd.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Tên dịch vụ"))
        item = self.table_cthd.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Số lượng"))
        item = self.table_cthd.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Đơn giá"))
        self.label.setText(_translate("Form", "Quản lý hóa đơn"))
        self.btnAdd.setText(_translate("Form", "Thêm"))
        self.btnEdit.setText(_translate("Form", "Sửa"))
        self.btnDelete.setText(_translate("Form", "Xóa"))
        self.btnReset.setText(_translate("Form", "Reset"))
        self.table_hoadon.itemClicked.connect(self.on_table_hoadon_clicked)
        self.btnAdd.clicked.connect(self.show_add_hd_dialog)
        self.btnDelete.clicked.connect(self.delete_HD)
        self.btnEdit.clicked.connect(self.show_update_hd_dialog)
        self.btnAddCTHD.clicked.connect(self.show_add_cthd_dialog)
        self.btnEditCTHD.clicked.connect(self.show_update_cthd_dialog)
        self.btnDeleteCTHD.clicked.connect(self.delete_CTHD)
        self.btnSearchHD.clicked.connect(self.searchHoaDon)
        self.btnReset.clicked.connect(self.resetHD)
        self.upload_hoadon()
    
    def fillTableHoaDon(self, bill_list):
        row = 0
        self.table_hoadon.setRowCount(len(bill_list))
        for bill in bill_list:
            self.table_hoadon.setItem(row, 0, QtWidgets.QTableWidgetItem(str(bill.get_mahd())))
            self.table_hoadon.setItem(row, 1, QtWidgets.QTableWidgetItem(str(bill.getNhanVien().tennv)))
            self.table_hoadon.setItem(row, 2, QtWidgets.QTableWidgetItem(str(bill.getKH().get_tenkh())))
            self.table_hoadon.setItem(row, 3, QtWidgets.QTableWidgetItem(str(bill.get_ngaytao())))
            self.table_hoadon.setItem(row, 4, QtWidgets.QTableWidgetItem(str(bill.get_tongtien())))
            row = row +1

    def fillTableCTHD(self, cthd_list):
        row = 0
        self.table_cthd.setRowCount(len(cthd_list))
        dao = serviceDAO()
        for cthd in cthd_list:
            service = dao.getServiceById(cthd.get_madv())
            self.table_cthd.setItem(row, 0, QtWidgets.QTableWidgetItem(str(cthd.get_macthd())))
            self.table_cthd.setItem(row, 1, QtWidgets.QTableWidgetItem(str(cthd.get_mahd())))
            self.table_cthd.setItem(row, 2, QtWidgets.QTableWidgetItem(service.getTen()))
            self.table_cthd.setItem(row, 3, QtWidgets.QTableWidgetItem(str(cthd.get_soLuong())))
            self.table_cthd.setItem(row, 4, QtWidgets.QTableWidgetItem(str(cthd.get_gia())))
            row = row +1

    def upload_hoadon(self):
        dao = billDAO()
        bill_list = dao.ReadFromDatabase()
        self.fillTableHoaDon(bill_list)
    
    def on_table_hoadon_clicked(self):
        selected_items = self.table_hoadon.selectedItems()
        if selected_items:
            selected_row = selected_items[0].row()
            id = self.table_hoadon.item(selected_row, 0).text()
            dao = cthdDAO()
            cthd_list = dao.getCTHDById(id)
            self.fillTableCTHD(cthd_list)

    def show_add_hd_dialog(self):
        dialog = QtWidgets.QDialog()
        self.hoadon_dialog = Ui_hoadon_dialog()
        self.hoadon_dialog.setupUi(dialog)
        self.loadComboboxMaNV()
        self.loadComboboxMaKH()
        self.hoadon_dialog.txtTotalPrice.setEnabled(False)
        self.hoadon_dialog.btnAccept.clicked.connect(self.addHoaDon)
        dialog.exec_()
        dialog.show()
        self.upload_hoadon()
    
    def show_add_cthd_dialog(self):
        dialog = QtWidgets.QDialog()
        self.cthd_dialog = Ui_cthd_dialog()
        self.cthd_dialog.setupUi(dialog)
        self.loadComboboxMaDV()
        self.cthd_dialog.txtPrice.setText('200000')

        selected_items = self.table_hoadon.selectedItems()
        if not selected_items:
            msg.show_warning_messagebox("Vui lòng chọn 1 dòng trong bảng dịch vụ")
            return
        
        selected_row = selected_items[0].row()
        id = self.table_hoadon.item(selected_row, 0).text()
        tongtien = self.table_hoadon.item(selected_row, 4).text()
        
        self.cthd_dialog.cbMaDV.currentIndexChanged.connect(self.loadPriceOfService)
        self.cthd_dialog.btnAccept.clicked.connect(lambda: self.addCTHD(id, int(tongtien)))
        dialog.exec_()
        dialog.show()
        self.upload_hoadon()

    def show_update_hd_dialog(self):
        dialog = QtWidgets.QDialog()
        self.hoadon_dialog = Ui_hoadon_dialog()
        self.hoadon_dialog.setupUi(dialog)
        self.hoadon_dialog.label_4.setText("SỬA HÓA ĐƠN")
        self.loadComboboxMaNV()
        self.loadComboboxMaKH()

        selected_row = self.table_hoadon.currentRow()
        if selected_row < 0:
            msg.show_warning_messagebox("Vui lòng chọn 1 dòng trong bảng hóa đơn")
            return

        selected_items = self.table_hoadon.selectedItems()
        row_data = [item.text() for item in selected_items]
        mahd = row_data[0]
        manv = row_data[1]
        makh = row_data[2]
        ngaytao = QtCore.QDate.fromString(row_data[3], "yyyy-M-d")   
        tongtien = row_data[4]   
        cbNV = self.hoadon_dialog.cbMaNV
        cbKH = self.hoadon_dialog.cbMaKH  
        for count in range(cbNV.count()):
            if manv in cbNV.itemText(count):
                indexNV = count

        for count in range(cbKH.count()):
            if makh in cbKH.itemText(count):
                indexKH = count

        self.hoadon_dialog.cbMaNV.setCurrentIndex(indexNV)
        self.hoadon_dialog.cbMaKH.setCurrentIndex(indexKH)
        self.hoadon_dialog.txtTotalPrice.setText(tongtien)
        self.hoadon_dialog.dateNgayTao.setDate(ngaytao)
        hd = bill(mahd, ngaytao, tongtien, manv, makh)

        self.hoadon_dialog.btnAccept.clicked.connect(lambda: self.update_HD(hd))
        dialog.exec_()
        dialog.show()

    def show_update_cthd_dialog(self):
        dialog = QtWidgets.QDialog()
        self.cthd_dialog = Ui_cthd_dialog()
        self.cthd_dialog.setupUi(dialog)
        self.cthd_dialog.label_4.setText("SỬA CTHD")
        self.loadComboboxMaDV()

        selected_hd = self.table_hoadon.selectedItems()
        if not selected_hd:
            msg.show_warning_messagebox("Vui lòng chọn 1 dòng trong bảng hóa đơn")
            return
        
        items_cthd = self.table_cthd.selectedItems()
        if not items_cthd:
            msg.show_warning_messagebox("Vui lòng chọn 1 dòng trong bảng chi tiết hóa đơn")
            return
        
        selected_row = items_cthd[0].row()
        macthd = self.table_cthd.item(selected_row, 0).text()
        mahd = self.table_cthd.item(selected_row, 1).text()
        tendv = self.table_cthd.item(selected_row, 2).text()
        sl = self.table_cthd.item(selected_row, 3).text()
        gia = self.table_cthd.item(selected_row, 4).text()
        thanhtiencu = int(sl) * int(gia)
        tongtien = self.table_hoadon.item(selected_hd[0].row(), 4).text()
        cbDV = self.cthd_dialog.cbMaDV
        for count in range(cbDV.count()):
            if tendv in cbDV.itemText(count):
                index = count
        self.cthd_dialog.cbMaDV.setCurrentIndex(index)
        self.cthd_dialog.txtQty.setText(sl)
        self.cthd_dialog.txtPrice.setText(gia)
        
        self.cthd_dialog.cbMaDV.currentIndexChanged.connect(self.loadPriceOfService)
        self.cthd_dialog.btnAccept.clicked.connect(lambda: self.update_CTHD(macthd, mahd, thanhtiencu, tongtien))
        dialog.exec_()
        dialog.show()
    
    def loadPriceOfService(self):
        madv = self.cthd_dialog.cbMaDV.currentText().split("-")[0]
        dao = serviceDAO()
        service = dao.getServiceById(madv)
        self.cthd_dialog.txtPrice.setText(str(service.getGia()))
    
    def loadComboboxMaNV(self):
        dao = employeeDAO()
        employees = dao.find_All()
        for emp in employees:
            self.hoadon_dialog.cbMaNV.addItem(f"{emp.manv} - {emp.tennv}")
    
    def loadComboboxMaKH(self):
        dao = customerDAO()
        customer = dao.ReadFromDatabase()
        for cus in customer:
            self.hoadon_dialog.cbMaKH.addItem(f"{cus.get_makh()} - {cus.get_tenkh()}")
    
    def loadComboboxMaDV(self):
        dao = serviceDAO()
        service = dao.getAllServices()

        for s in service:
            self.cthd_dialog.cbMaDV.addItem(f"{s.getMaDV()} - {s.getTen()}")

    def on_button_clicked(self):
        Dialog = QtWidgets.QDialog()
        ui = tb.Ui_Dialog()
        ui.setupUi(Dialog)
        selected_items = self.table_hoadon.selectedItems()
        if selected_items:
            selected_row = selected_items[0].row()
            value = self.table_hoadon.item(selected_row, 0).text()
            ui.label.setText(self._translate("Dialog", self.delete_HD(value)))
        else:
            ui.label.setText(self._translate("Dialog", "Vui lòng hãy chọn dòng muốn xoá"))
        Dialog.exec_()
        self.upload_hoadon()

                
    def delete_HD(self):
        selected_items = self.table_hoadon.selectedItems()
        if selected_items:
            selected_row = selected_items[0].row()
            id = self.table_hoadon.item(selected_row, 0).text()
            dao = billDAO()
            dao.delete(id)
            msg.show_warning_messagebox("Xóa hóa đơn đã chọn thành công")
            self.upload_hoadon()
            self.on_table_hoadon_clicked()
        else:
            msg.show_warning_messagebox("Vui lòng chọn 1 dòng trong bảng hóa đơn")
    
    def delete_CTHD(self):
        items_hd = self.table_hoadon.selectedItems()
        if not items_hd:
            msg.show_warning_messagebox("Vui lòng chọn 1 dòng trong bảng hóa đơn")
            return
        
        items_cthd = self.table_cthd.selectedItems()
        if items_cthd:
            selected_row_cthd = items_cthd[0].row()
            selected_row_hd = items_hd[0].row()
            macthd = self.table_cthd.item(selected_row_cthd, 0).text()
            sl = self.table_cthd.item(selected_row_cthd, 3).text()
            gia = self.table_cthd.item(selected_row_cthd, 4).text()
            mahd = self.table_hoadon.item(selected_row_hd, 0).text()
            tt = self.table_hoadon.item(selected_row_hd, 4).text()
            tongtien = int(tt) - (int(gia) * int(sl))
            
            hddao = billDAO()
            cthddao = cthdDAO()
            cthddao.deleteCTHD(macthd)
            hddao.updateTotalPrice(mahd, tongtien)
            msg.show_warning_messagebox("Xóa chi tiết hoá đơn đã chọn thành công")
            self.on_table_hoadon_clicked()
            self.upload_hoadon()
        else:
            msg.show_warning_messagebox("Vui lòng chọn 1 dòng trong bảng chi tiết hóa đơn")

            
    def addHoaDon(self):
        manv = int(self.hoadon_dialog.cbMaNV.currentText().split("-")[0])
        makh = int(self.hoadon_dialog.cbMaKH.currentText().split("-")[0])
        ngaytao = self.hoadon_dialog.dateNgayTao.date().toString('yyyy-MM-dd')

        hdDAO = billDAO()
        subBill = bill("", ngaytao, 0, manv, makh)
        hdDAO.insert(subBill)
        msg.show_info_messagebox("Thêm hóa đơn thành công")
    
    def addCTHD(self, mahd, tongtien):
        madv = self.cthd_dialog.cbMaDV.currentText().split("-")[0]
        gia = self.cthd_dialog.txtPrice.text()
        sl = self.cthd_dialog.txtQty.text()

        if not sl:
            msg.show_warning_messagebox("Vui lòng nhập đầy đủ dữ liệu")
            return
        
        if not sl.isnumeric() or int(sl) <= 0:
            msg.show_warning_messagebox("Vui lòng chỉ nhập số lớn hơn 0 cho trường số lượng")
            return
    
        tongtien += int(sl) * int(gia)

        hddao = billDAO()
        cthddao = cthdDAO()
        dpdao = serviceDAO()
        cthddao.insertCTHD(CTHD(None, mahd, madv, sl, gia))
        hddao.updateTotalPrice(mahd, tongtien)

        list = dpdao.isServiceUseMedicine(madv)
        dpdao = medicineDAO()
        if len(list) > 0:
            dpdao.updateDecQuantity(list, sl)
        
        msg.show_info_messagebox("Thêm chi tiết hóa đơn thành công")
        self.on_table_hoadon_clicked()
        
    def update_HD(self, hd):
        manv = self.hoadon_dialog.cbMaNV.currentText().split("-")[0]
        makh = self.hoadon_dialog.cbMaKH.currentText().split("-")[0]
        ngaytao = self.hoadon_dialog.dateNgayTao.date().toString('MM-dd-yyyy')
        tongtien = self.hoadon_dialog.txtTotalPrice.text()

        if not tongtien:
            msg.show_warning_messagebox("Vui lòng nhập đầy đủ dữ liệu")
            return
        
        if not tongtien.isnumeric() or int(tongtien) <= 0:
            msg.show_warning_messagebox("Vui lòng chỉ nhập số cho trường tổng tiền")
            return
        
        dao = billDAO()
        dao.update(bill(hd.get_mahd(), ngaytao, tongtien, manv, makh))
        msg.show_info_messagebox("Sửa hóa đơn thành công")
        self.upload_hoadon()

    def update_CTHD(self, macthd, mahd, thanhtiencu, tongtien):
        madv = self.cthd_dialog.cbMaDV.currentText().split("-")[0]
        gia = self.cthd_dialog.txtPrice.text()
        sl = self.cthd_dialog.txtQty.text()
        
        if not sl:
            msg.show_warning_messagebox("Vui lòng nhập đầy đủ dữ liệu")
            return
        
        if not sl.isnumeric() or int(sl) <= 0:
            msg.show_warning_messagebox("Vui lòng chỉ nhập số cho trường số lượng")
            return
            

        thanhtien = int(gia) * int(sl)
        ttmoi = int(tongtien) - thanhtiencu + int(thanhtien)

        hddao = billDAO()
        cthddao = cthdDAO()
        cthddao.updateCTHD(CTHD(macthd, mahd, madv, sl, gia))
        hddao.updateTotalPrice(mahd, ttmoi)
        msg.show_info_messagebox("Sửa chi tiết hóa đơn thành công")
        self.on_table_hoadon_clicked()
        self.upload_hoadon()

    def searchHoaDon(self):
        dao = billDAO()
        search = self.txtSearchHD.text()
        choice = self.cbSearchHD.currentIndex()
        pn = dao.searchHoaDon(search, choice)
        self.fillTableHoaDon(pn)

    def resetHD(self):
        self.fillTableHoaDon()
        self.table_cthd.setRowCount(0)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
