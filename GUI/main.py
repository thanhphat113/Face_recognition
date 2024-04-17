from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets 

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from GUI.sidebar import Ui_MainWindow
from GUI.login import Ui_login_form
from GUI import phongbenh as pb, nhanvien as nv ,dichvu as dv, thunuoi as tn, home ,khachhang as kh, hoadon,phieunhap as pn,duocpham as dp,taikhoan as tk,nhacungcap as ncc,thongtin as tt,doimk as mk
from DAO.serviceDAO import serviceDAO
from DAO.taikhoanDAO import taikhoanDAO
from DAO.employeeDAO import employeeDAO
from DTO.employeeDTO import employee
import GUI.thongbao as tb

class Login(QWidget, Ui_login_form):
    def __init__(self):
        self.empDAO = employeeDAO()
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
            taikhoan = tk.checkPassword(username,password)
            if taikhoan is not None:
                nhanvien = self.empDAO.getEmployeeById(taikhoan[5])
            
                if taikhoan[3] == 0:
                    self.thongbao.thongBao("Tài khoản của bạn đã bị ngưng hoạt động")
                # elif taikhoan[5] is None:
                #     self.thongbao.thongBao("Bạn đã nhập sai mật khẩu hoặc tài khoản")
                elif taikhoan[4] == 1:
                    self.sidebar = Main_Page(nhanvien)
                    self.close()
                    self.sidebar.show()
                elif taikhoan[4] == 2:
                    self.sidebar = Main_Page(nhanvien,2)
                    self.hide()
                    self.sidebar.show()
            else: self.thongbao.thongBao("Bạn đã nhập sai mật khẩu hoặc tài khoản")
        
                    
    
class Main_Page(QMainWindow, Ui_MainWindow):
    def __init__(self, nhanvien:employee, type=1):
        self.nhanvien = nhanvien
        super().__init__()

        self.window = QMainWindow()
        self.setupUi(self)
        
            
        self.btnAcc.clicked.connect(lambda: self.showInfor(self.nhanvien))
            
        self.icon_menu_widget.hide()

        self.home_form = home.Ui_Form()
        self.home_form.setupUi(self.home_Page)

        self.nv_form = nv.Ui_Form()
        self.nv_form.setupUi(self.employee_page)
        
        self.ac_form = tk.Ui_Form()
        self.ac_form.setupUi(self.account_page)

        self.dv_form = dv.Ui_Form()
        self.dv_form.setupUi(self.service_Page)

        self.pn_form = pn.Ui_Form()
        self.pn_form.setupUi(self.phieunhap_page)
        
        self.ncc_form = ncc.Ui_Form()
        self.ncc_form.setupUi(self.ncc_page)

        self.dp_form = dp.Ui_Form()
        self.dp_form.setupUi(self.medicine_page)

        self.kh_form = kh.Ui_Form()
        self.kh_form.setupUi(self.customer_Page)

        self.tn_form = tn.Ui_Form()
        self.tn_form.setupUi(self.pets_Page)
        
        self.bed_form = pb.Ui_Form()
        self.bed_form.setupUi(self.bed_Page)
        
        self.taikhoan_form = tk.Ui_Form()
        self.taikhoan_form.setupUi(self.account_page)

        self.hd_form = hoadon.Ui_Form()
        self.hd_form.setupUi(self.bill_page)

        self.eventHandling()
        self.pushButton_12.clicked.connect(self.dangXuat)
        self.pushButton_5.clicked.connect(self.dangXuat)
        self.loadServiceData()
        
       
        if type == 2:
            self.btnService.setVisible(False)
            self.iconService.setVisible(False)
            self.btnEmployee.setVisible(False)
            self.iconEmployee.setVisible(False)
            self.btnPhieuNhap.setVisible(False)
            self.iconPhieuNhap.setVisible(False)
            self.btnAccount.setVisible(False)
            self.iconAccount.setVisible(False)
            self.btnBill.setVisible(False)
            self.iconBill.setVisible(False)
            self.btnNcc.setVisible(False)
            self.iconNcc.setVisible(False)
            
    
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
        
    def showAccount_Pages(self):
        self.stackedWidget.setCurrentIndex(5)

    def showHoaDon_Pages(self):
        self.stackedWidget.setCurrentIndex(6)

    def showPhieuNhap_Pages(self):
        self.stackedWidget.setCurrentIndex(7)
        
    def showNcc_Pages(self):
        self.stackedWidget.setCurrentIndex(8)

    def showMedicine_Pages(self):
        self.stackedWidget.setCurrentIndex(9)

    def showService_Pages(self):
        self.stackedWidget.setCurrentIndex(10)
        
    # Xử lý giao diện
    def eventHandling(self):
        self.btnEmployee.clicked.connect(self.showEmployee_Pages)
        self.btnCustomer.clicked.connect(self.showCustomer_Pages)
        self.btnAccount.clicked.connect(self.showAccount_Pages)
        self.btnBed.clicked.connect(self.showBed_Pages)
        self.btnPets.clicked.connect(self.showPets_Pages)
        self.btnNcc.clicked.connect(self.showNcc_Pages)
        self.btnHome.clicked.connect(self.showHome_Pages)
        self.btnService.clicked.connect(self.showService_Pages)
        self.btnPhieuNhap.clicked.connect(self.showPhieuNhap_Pages)
        self.btnMedicine.clicked.connect(self.showMedicine_Pages)
        self.btnBill.clicked.connect(self.showHoaDon_Pages)
        self.iconEmployee.clicked.connect(self.showEmployee_Pages)
        self.iconCustomer.clicked.connect(self.showCustomer_Pages)
        self.iconAccount.clicked.connect(self.showAccount_Pages)
        self.iconPets.clicked.connect(self.showPets_Pages)
        self.iconNcc.clicked.connect(self.showNcc_Pages)
        self.iconBed.clicked.connect(self.showBed_Pages)
        self.iconHome.clicked.connect(self.showHome_Pages)
        self.iconService.clicked.connect(self.showService_Pages)
        self.iconPhieuNhap.clicked.connect(self.showPhieuNhap_Pages)
        self.iconMedicine.clicked.connect(self.showMedicine_Pages)
        self.iconBill.clicked.connect(self.showHoaDon_Pages)

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
            
    def showInfor(self,nv:employee):
        Dialog = QtWidgets.QDialog()
        ui = tt.Ui_Dialog()
        ui.setupUi(Dialog)
        ui.txtName.setText(nv.tennv)
        ui.txtSdt.setText(nv.sdt)
        ui.txtEmail.setText(nv.email)
        ui.pushButton.clicked.connect(lambda: self.doiMatKhau(str(nv.manv)))
        Dialog.exec_()
        
    def doiMatKhau(self,manv):
        Dialog = QtWidgets.QDialog()
        ui = mk.Ui_Dialog()
        ui.setupUi(Dialog)
        ui.manv.setText(manv)
        Dialog.exec_()
