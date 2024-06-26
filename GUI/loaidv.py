# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/loaidv.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from DAO.service_category_DAO import serviceCategoryDAO
from DTO.service_categoryDTO import ServiceCategory

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(799, 547)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 761, 521))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.groupBox_3 = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_3)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(20, 40, 461, 81))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setHorizontalSpacing(30)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.txtMaLoai = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.txtMaLoai.setMinimumSize(QtCore.QSize(0, 32))
        self.txtMaLoai.setStyleSheet("background-color: rgb(231, 231, 231);")
        self.txtMaLoai.setReadOnly(True)
        self.txtMaLoai.setObjectName("txtMaLoai")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtMaLoai)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.txtTenLoai = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.txtTenLoai.setMinimumSize(QtCore.QSize(0, 32))
        self.txtTenLoai.setObjectName("txtTenLoai")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtTenLoai)
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 140, 741, 50))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_6.setContentsMargins(8, 5, 8, 5)
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.btnAdd_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.btnAdd_2.setMinimumSize(QtCore.QSize(90, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btnAdd_2.setFont(font)
        self.btnAdd_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAdd_2.setStyleSheet("background-color: #9FC899;\n"
"border: none;\n"
"border-radius: 5px;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui\\../img/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAdd_2.setIcon(icon)
        self.btnAdd_2.setIconSize(QtCore.QSize(20, 20))
        self.btnAdd_2.setFlat(False)
        self.btnAdd_2.setObjectName("btnAdd_2")
        self.horizontalLayout_6.addWidget(self.btnAdd_2)
        self.btnDelete_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.btnDelete_2.setMinimumSize(QtCore.QSize(90, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btnDelete_2.setFont(font)
        self.btnDelete_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnDelete_2.setStyleSheet("background-color: rgb(255, 124, 125);\n"
"border: none;\n"
"border-radius: 5px;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ui\\../img/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnDelete_2.setIcon(icon1)
        self.btnDelete_2.setIconSize(QtCore.QSize(20, 20))
        self.btnDelete_2.setObjectName("btnDelete_2")
        self.horizontalLayout_6.addWidget(self.btnDelete_2)
        self.btnUpdate_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.btnUpdate_2.setMinimumSize(QtCore.QSize(90, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btnUpdate_2.setFont(font)
        self.btnUpdate_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnUpdate_2.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"border: none;\n"
"border-radius: 5px;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("ui\\../img/edit_48px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnUpdate_2.setIcon(icon2)
        self.btnUpdate_2.setIconSize(QtCore.QSize(20, 20))
        self.btnUpdate_2.setObjectName("btnUpdate_2")
        self.horizontalLayout_6.addWidget(self.btnUpdate_2)
        self.btnReset = QtWidgets.QPushButton(self.layoutWidget)
        self.btnReset.setMinimumSize(QtCore.QSize(90, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btnReset.setFont(font)
        self.btnReset.setStyleSheet("background-color: #BDD5D7;\n"
"border: none;\n"
"border-radius: 5px;")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("ui\\../img/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnReset.setIcon(icon3)
        self.btnReset.setObjectName("btnReset")
        self.horizontalLayout_6.addWidget(self.btnReset)
        spacerItem = QtWidgets.QSpacerItem(218, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.horizontalLayout_4.addWidget(self.groupBox_3)
        self.layoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.layoutWidget_2.setGeometry(QtCore.QRect(30, 220, 741, 50))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_5.setContentsMargins(8, 5, 8, 5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.input_search_2 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.input_search_2.setMinimumSize(QtCore.QSize(300, 32))
        self.input_search_2.setObjectName("input_search_2")
        self.horizontalLayout_5.addWidget(self.input_search_2)
        self.btnSearch_2 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.btnSearch_2.setMinimumSize(QtCore.QSize(90, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btnSearch_2.setFont(font)
        self.btnSearch_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSearch_2.setStyleSheet("background-color: #BDD5D7;\n"
"border: none;\n"
"border-radius: 5px;")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("ui\\../../PhongKhamThuY/img/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSearch_2.setIcon(icon4)
        self.btnSearch_2.setIconSize(QtCore.QSize(20, 20))
        self.btnSearch_2.setObjectName("btnSearch_2")
        self.horizontalLayout_5.addWidget(self.btnSearch_2)
        self.table_service_category = QtWidgets.QTableWidget(Dialog)
        self.table_service_category.setGeometry(QtCore.QRect(30, 270, 741, 261))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_service_category.sizePolicy().hasHeightForWidth())
        self.table_service_category.setSizePolicy(sizePolicy)
        self.table_service_category.setWordWrap(False)
        self.table_service_category.setColumnCount(2)
        self.table_service_category.setObjectName("table_service_category")
        self.table_service_category.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table_service_category.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table_service_category.setHorizontalHeaderItem(1, item)
        self.table_service_category.horizontalHeader().setCascadingSectionResizes(False)
        self.table_service_category.horizontalHeader().setSortIndicatorShown(False)
        self.table_service_category.horizontalHeader().setStretchLastSection(True)
        self.table_service_category.verticalHeader().setVisible(False)
        self.table_service_category.verticalHeader().setCascadingSectionResizes(False)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox_3.setTitle(_translate("Dialog", "Thông tin danh mục dịch vụ"))
        self.label_3.setText(_translate("Dialog", "Mã loại"))
        self.label_4.setText(_translate("Dialog", "Tên loại"))
        self.btnAdd_2.setText(_translate("Dialog", "Thêm"))
        self.btnDelete_2.setText(_translate("Dialog", "Xoá"))
        self.btnUpdate_2.setText(_translate("Dialog", "Sửa"))
        self.btnReset.setText(_translate("Dialog", "Reset"))
        self.label_6.setText(_translate("Dialog", "Tìm kiếm "))
        self.btnSearch_2.setText(_translate("Dialog", "Tìm"))
        self.table_service_category.setSortingEnabled(False)
        item = self.table_service_category.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Mã loại dịch vụ"))
        item = self.table_service_category.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Tên loại dịch vụ"))
        self.loadServiceCategories()
        self.btnAdd_2.clicked.connect(self.addServiceCategory)
        self.btnUpdate_2.clicked.connect(self.updateServiceCategory)
        self.btnDelete_2.clicked.connect(self.deleteServiceCategory)
        self.btnReset.clicked.connect(self.resetData)
        self.table_service_category.itemClicked.connect(self.selectedItemInTable)

    def loadServiceCategories(self):
        dao = serviceCategoryDAO()
        categories = dao.getAllServiceCategories()
        row = 0
        self.table_service_category.setRowCount(len(categories))
        for category in categories:
            self.table_service_category.setItem(row, 0, QtWidgets.QTableWidgetItem(str(category.getMaLoaiDV())))
            self.table_service_category.setItem(row, 1, QtWidgets.QTableWidgetItem(category.getTenLoai()))
            row = row +1

    def addServiceCategory(self):
        dao = serviceCategoryDAO()
        service_category = ServiceCategory(None, self.txtTenLoai.text())
        dao.insertServiceCategory(service_category)
        self.loadServiceCategories()

    def updateServiceCategory(self):
        dao = serviceCategoryDAO()
        service_category = ServiceCategory(self.txtMaLoai.text(), self.txtTenLoai.text())
        dao.updateServiceCategory(service_category)
        self.loadServiceCategories()
    
    def deleteServiceCategory(self):
        dao = serviceCategoryDAO()
        dao.deleteServiceCategory(self.txtMaLoai.text())
        self.loadServiceCategories()
        self.resetData()

    def selectedItemInTable(self):
        rowSelected = self.table_service_category.currentRow()
        id = self.table_service_category.item(rowSelected, 0).text()
        name = self.table_service_category.item(rowSelected, 1).text()
        self.txtMaLoai.setText(id)
        self.txtTenLoai.setText(name)

    def resetData(self):
        self.txtMaLoai.setText("")
        self.txtTenLoai.setText("")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
