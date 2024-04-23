from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem,QTableView

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import GUI.TacvuTK as tv
import GUI.thongbao as tb
from  DAO.taikhoanDAO import taikhoanDAO
from  DAO.loaitaikhoanDAO import loaitaikhoanDAO

class Ui_Form(object):
    def setupUi(self, Form):
        self.tb = tb.Ui_Dialog()
        Form.setObjectName("Form")
        Form.resize(800, 500)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.gridLayout_3 = QtWidgets.QGridLayout(Form)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setHorizontalSpacing(6)
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setStyleSheet("QWidget{\n"
"    background-color: rgb(65, 255, 245);\n"
"    border:1px solid black\n"
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
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout_3.addWidget(self.widget, 0, 0, 1, 1)
        self.widget_3 = QtWidgets.QWidget(Form)
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(218, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnUpdate = QtWidgets.QPushButton(parent=self.widget_3)
        self.btnUpdate.setStyleSheet("background-color: rgb(188, 202, 255);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/refresh.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnUpdate.setIcon(icon2)
        self.btnUpdate.setIconSize(QtCore.QSize(20, 20))
        self.btnUpdate.setObjectName("btnUpdate")
        self.btnUpdate.clicked.connect(self.update_NV)
        self.btnRefesh = QtWidgets.QPushButton(parent=self.widget_3)
        self.btnRefesh.setStyleSheet("background-color: rgb(188, 100, 255);")
        # self.btnRefesh.setIcon(icon2)
        self.btnRefesh.setIconSize(QtCore.QSize(20, 20))
        self.btnRefesh.setObjectName("btnRefesh")
        
        self.horizontalLayout.addWidget(self.btnRefesh)
        self.horizontalLayout.addWidget(self.btnUpdate)

        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.widget_3, 2, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setStyleSheet("border:none;")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setEnabled(False)
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.cbbType_choise = QtWidgets.QComboBox(self.widget_2)
        self.cbbType_choise.setObjectName("comboBox")
        self.cbbType_choise.addItem("Admin")
        self.cbbType_choise.addItem("Nhân viên")
        self.cbbType_choise.setMinimumSize(150,20)
        self.cbbType_choise.setVisible(False)
        self.horizontalLayout_2.addWidget(self.cbbType_choise)
        self.comboBox = QtWidgets.QComboBox(self.widget_2)
        self.comboBox.setMinimumSize(QtCore.QSize(135, 5))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setMinimumSize(150,20)
        self.comboBox.addItem("Tất cả")
        self.comboBox.addItem("Mã tài khoản")
        self.comboBox.addItem("Username")
        self.comboBox.addItem("Trạng thái")
        self.comboBox.addItem("Loại tài khoản")
        self.comboBox.currentIndexChanged.connect(self.changeEnable)
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.widget_2)
        self.pushButton_4.setStyleSheet("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("img/search.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.findByCondition)
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.tableWidget = QtWidgets.QTableWidget(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tableWidget.setWordWrap(False)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(8, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.gridLayout_3.addWidget(self.widget_2, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        self._translate = QtCore.QCoreApplication.translate
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Quản lý tài khoản"))
        self.btnUpdate.setText(_translate("Form", "Sửa"))
        self.btnRefesh.setText(_translate("Form", "Reload"))
        self.btnUpdate.setMinimumSize(100, 30)
        self.btnRefesh.setMinimumSize(100, 30)
        self.btnRefesh.clicked.connect(self.upload_list)
        self.label_2.setText(_translate("Form", "Tìm kiếm "))

        self.pushButton_4.setText(_translate("Form", "Tìm"))
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setEditTriggers(QTableView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QTableView.SelectRows)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Mã tài khoản"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Username"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Password"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Trạng thái"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Loại tài khoản"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Nhân viên"))
        self.upload_list()
    

    def upload_list(self):
        taikhoan_list = taikhoanDAO().find_All()
        self.tableWidget.setRowCount(0)
        for tk in taikhoan_list:
            trangthai = 'Không hoạt động'
            if tk.trangthai == 1 :
                trangthai = 'Hoạt động'
            data = [tk.matk, tk.username, tk.password, trangthai, tk.loai[1], tk.nhanvien.tennv]
            self.add_row_to_table(data)
                    
    

    def add_row_to_table(self, data):
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)
        for column, item in enumerate(data):
            self.tableWidget.setItem(rowPosition, column, QTableWidgetItem(str(item)))
    
        
    def update_NV(self):
        Dialog = QtWidgets.QDialog()
        ui = tv.Ui_Dialog()
        ui.setupUi(Dialog,2)    
        ui.title.setText(self._translate("Dialog", "Sửa thông tin"))
        accType_list = loaitaikhoanDAO().find_All()
        for accType in accType_list:
            ui.cbMaLTK.addItem(f"{accType.tenloai}")
        selected_row = self.tableWidget.currentRow()
        if selected_row  >= 0:
            selected_items = self.tableWidget.selectedItems()
            row_data = [item.text() for item in selected_items]
            ui.label_visible.setText(self._translate("Dialog",row_data[0]))
            ui.txtName.setText(self._translate("Dialog",row_data[1]))
            ui.txtPwd.setText(self._translate("Dialog",row_data[2]))
            ui.cbbStatus.setCurrentText(self._translate("Dialog",row_data[3]))
            ui.txtMaNV.setText(self._translate("Dialog",row_data[5]))
            account_list = taikhoanDAO().findByAccTypeName(row_data[4])
            for acc in account_list:
                ui.cbMaLTK.setCurrentIndex(acc.maloai - 1)   
            Dialog.exec_()
            self.upload_list()
        else: 
            self.tb.thongBao('Vui lòng chọn 1 dòng để thực hiện sửa')
        

    
    def changeEnable(self):
        type = self.comboBox.currentIndex()
        if type == 0:
            self.lineEdit.setEnabled(False)
            self.hideCbbType_choise()
            self.upload_list()
        if type == 1:
            self.lineEdit.setEnabled(True)
            self.hideCbbType_choise()
        if type == 2:
            self.lineEdit.setEnabled(True)
            self.hideCbbType_choise()
        if type == 3:
            self.lineEdit.setEnabled(True)
            self.hideCbbType_choise()
        if type == 4:
            self.showCbbType_choise()
    
    def showCbbType_choise(self):
        self.lineEdit.setVisible(False)
        self.cbbType_choise.setVisible(True)
        
    def hideCbbType_choise(self):
        self.lineEdit.setVisible(True)
        self.cbbType_choise.setVisible(False)


    def findByCondition(self):
        type = self.comboBox.currentIndex()
        condition = self.lineEdit.text()

        if type == 1:
            self.lineEdit.setEnabled(True)
            result = taikhoanDAO().findById(condition)
        elif type == 2:
            self.lineEdit.setEnabled(True)
            result = taikhoanDAO().findByName(condition)
        elif type == 3:
            self.lineEdit.setEnabled(True)
            result = taikhoanDAO().findByStatus(condition)
        elif type == 4:
            value = self.cbbType_choise.currentIndex() + 1
            result = taikhoanDAO().findByAccTypeID(value)

        if type != 0:
            accType_list = loaitaikhoanDAO().find_All()
            self.tableWidget.setRowCount(0)
            for taikhoan in result:
                for accType in accType_list:
                    if accType.maloai == taikhoan.maloai:
                        data = [taikhoan.matk, taikhoan.username, taikhoan.password, taikhoan.trangthai, accType.tenloai]
                        self.add_row_to_table(data)
                        break
        else:
            self.upload_list()
        self.lineEdit.setText("")

