from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets 

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from GUI.sidebar import Ui_MainWindow
from GUI.login import Ui_login_form
from GUI.add_service_dialog import Ui_add_service_dialog
from GUI import phongbenh as pb, nhanvien as nv ,dichvu as dv, thunuoi as tn, home ,khachhang as kh, hoadon,phieunhap as pn,duocpham as dp
from DAO.serviceDAO import serviceDAO
from DAO.taikhoanDAO import taikhoanDAO
import GUI.thongbao as tb

class Login(QWidget, Ui_login_form):
    def __init__(self):
        super().__init__()
        self.window = QWidget()
        self.setupUi(self)
        self.thongbao = tb.Ui_Dialog()
        self.show()

        self.btnLogin.clicked.connect(self.handle_login)
        
    def keyPressEvent(self, event):
                if event.key() == 16777220:
                        self.handle_login()

    def handle_login(self):
        username = self.txtUser.text()
        password = self.txtPass.text()
        if not username or not password:
            self.thongbao.thongBao("Không được bỏ trống tài khoản hoặc mật khẩu")
        else:
            tk = taikhoanDAO()
            loai = tk.checkPassword(username,password)
            if loai is None:
                self.thongbao.thongBao("Bạn đã nhập sai mật khẩu hoặc tài khoản")
            elif loai == 1:
                self.sidebar = Main_Page()
                self.close()
                self.sidebar.show()
            elif loai == 2:
                self.sidebar = Main_Page()
                self.hide()
                self.sidebar.show()
        
                    
    
class Main_Page(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.window = QMainWindow()
        self.setupUi(self)

        self.icon_menu_widget.hide()

        self.home_form = home.Ui_Form()
        self.home_form.setupUi(self.home_Page)

        self.nv_form = nv.Ui_Form()
        self.nv_form.setupUi(self.employee_page)

        self.dv_form = dv.Ui_Form()
        self.dv_form.setupUi(self.service_Page)

        self.pn_form = pn.Ui_Form()
        self.pn_form.setupUi(self.phieunhap_page)

        self.dp_form = dp.Ui_Form()
        self.dp_form.setupUi(self.medicine_page)

        self.kh_form = kh.Ui_Form()
        self.kh_form.setupUi(self.customer_Page)

        self.tn_form = tn.Ui_Form()
        self.tn_form.setupUi(self.pets_Page)
        
        self.bed_form = pb.Ui_Form()
        self.bed_form.setupUi(self.bed_Page)

        self.add_service_dialog = Ui_add_service_dialog()

        self.eventHandling()
        self.dv_form.btnAdd.clicked.connect(self.show_add_dialog)
        self.pushButton_12.clicked.connect(self.dangXuat)
        self.pushButton_5.clicked.connect(self.dangXuat)
        self.loadServiceData()
    
    def dangXuat(self):
        self.login = Login()
        self.close()
        self.login.show()

    def showHome_Pages(self):
        self.stackedWidget.setCurrentIndex(0)
    
    def showCustomer_Pages(self):
        self.stackedWidget.setCurrentIndex(1)
    
    def showPets_Pages(self):
        self.stackedWidget.setCurrentIndex(2)
        
    def showBed_Pages(self):
        self.stackedWidget.setCurrentIndex(3)
    
    def showEmployee_Pages(self):
        self.stackedWidget.setCurrentIndex(4)
    
    def showPhieuNhap_Pages(self):
        self.stackedWidget.setCurrentIndex(5)

    def showMedicine_Pages(self):
        self.stackedWidget.setCurrentIndex(6)

    def showService_Pages(self):
        self.stackedWidget.setCurrentIndex(7)

    def showChart_Pages(self):
        self.stackedWidget.setCurrentIndex(8)
    
    def show_add_dialog(self):
        dialog = QtWidgets.QDialog()
        self.add_service_dialog = Ui_add_service_dialog()
        self.add_service_dialog.setupUi(dialog)
        dialog.exec_()
        dialog.show()

    # Xử lý giao diện
    def eventHandling(self):
        self.btnEmployee.clicked.connect(self.showEmployee_Pages)
        self.btnCustomer.clicked.connect(self.showCustomer_Pages)
        self.btnBed.clicked.connect(self.showBed_Pages)
        self.btnPets.clicked.connect(self.showPets_Pages)
        self.btnChart.clicked.connect(self.showChart_Pages)
        self.btnHome.clicked.connect(self.showHome_Pages)
        self.btnService.clicked.connect(self.showService_Pages)
        self.btnPhieuNhap.clicked.connect(self.showPhieuNhap_Pages)
        self.btnMedicine.clicked.connect(self.showMedicine_Pages)
        self.iconEmployee.clicked.connect(self.showEmployee_Pages)
        self.iconCustomer.clicked.connect(self.showCustomer_Pages)
        self.iconPets.clicked.connect(self.showPets_Pages)
        self.iconBed.clicked.connect(self.showBed_Pages)
        self.iconChart.clicked.connect(self.showChart_Pages)
        self.iconHome.clicked.connect(self.showHome_Pages)
        self.iconService.clicked.connect(self.showService_Pages)
        self.iconPhieuNhap.clicked.connect(self.showPhieuNhap_Pages)
        self.iconMedicine.clicked.connect(self.showMedicine_Pages)

    def loadServiceData(self):
        dao = serviceDAO()
        services = dao.getAllServices()
        row = 0
        self.dv_form.table_service.setRowCount(len(services))
        for service in services:
            self.dv_form.table_service.setItem(row, 0, QtWidgets.QTableWidgetItem(str(service.getMaDV())))
            self.dv_form.table_service.setItem(row, 1, QtWidgets.QTableWidgetItem(service.getTen()))
            self.dv_form.table_service.setItem(row, 2, QtWidgets.QTableWidgetItem(str(service.getGia())))
            row = row +1
