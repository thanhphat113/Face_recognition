from main import Main_Page
from PyQt5.QtWidgets import QApplication
import sys

app = QApplication(sys.argv) 

window = Main_Page()
sys.exit(app.exec())