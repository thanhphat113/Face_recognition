from PyQt5.QtWidgets import *

def show_info_messagebox(message): 
    msg = QMessageBox() 
    msg.setIcon(QMessageBox.Information) 
  
    msg.setText(message) 
      
    msg.setWindowTitle("Thông báo") 
      
    msg.setStandardButtons(QMessageBox.Ok) 
      
    retval = msg.exec_() 

def show_warning_messagebox(message): 
    msg = QMessageBox() 
    msg.setIcon(QMessageBox.Warning) 
  
    msg.setText(message) 
      
    msg.setWindowTitle("Cảnh báo") 
      
    msg.setStandardButtons(QMessageBox.Ok) 
      
    retval = msg.exec_() 