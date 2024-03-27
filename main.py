from PyQt5.QtWidgets import *
from sidebar import Ui_MainWindow
import nhanvien as nv
import dichvu as dv

class Main_Page(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.window = QMainWindow()
        self.setupUi(self)
        self.show()

        self.icon_menu_widget.hide()

        nv_form = nv.Ui_Form()
        nv_form.setupUi(self.employee_page)

        dv_form = dv.Ui_Form()
        dv_form.setupUi(self.service_Page)

        self.eventHandling()

    def showHome_Pages(self):
        self.stackedWidget.setCurrentIndex(0)
    
    def showCustomer_Pages(self):
        self.stackedWidget.setCurrentIndex(1)
    
    def showPets_Pages(self):
        self.stackedWidget.setCurrentIndex(2)
    
    def showEmployee_Pages(self):
        self.stackedWidget.setCurrentIndex(3)

    def showService_Pages(self):
        self.stackedWidget.setCurrentIndex(4)

    def showChart_Pages(self):
        self.stackedWidget.setCurrentIndex(5)
    
    
    # Xử lý giao diện
    def eventHandling(self):
        self.btnEmployee.clicked.connect(self.showEmployee_Pages)
        self.btnCustomer.clicked.connect(self.showCustomer_Pages)
        self.btnPets.clicked.connect(self.showPets_Pages)
        self.btnChart.clicked.connect(self.showChart_Pages)
        self.btnHome.clicked.connect(self.showHome_Pages)
        self.btnService.clicked.connect(self.showService_Pages)
        self.iconEmployee.clicked.connect(self.showEmployee_Pages)
        self.iconCustomer.clicked.connect(self.showCustomer_Pages)
        self.iconPets.clicked.connect(self.showPets_Pages)
        self.iconChart.clicked.connect(self.showChart_Pages)
        self.iconHome.clicked.connect(self.showHome_Pages)
        self.iconService.clicked.connect(self.showService_Pages)