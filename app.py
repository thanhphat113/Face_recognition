import GUI.main as main
from PyQt5 import QtWidgets
import sys

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = main.Login()
    window.show()
    app.exec_()
