import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Table Example')
        self.setGeometry(100, 100, 600, 300)

        # Tạo bảng với 5 cột và 5 hàng
        self.tableWidget = QTableWidget(5, 5, self)

        # Đặt tiêu đề cho các cột
        column_headers = ["Column 1", "Column 2", "Column 3", "Column 4", "Column 5"]
        self.tableWidget.setHorizontalHeaderLabels(column_headers)

        # Thêm dữ liệu vào từng ô của bảng
        for row in range(5):
            for col in range(5):
                item = QTableWidgetItem(f"Row {row + 1}, Col {col + 1}")
                self.tableWidget.setItem(row, col, item)

        # Tạo layout và thêm bảng vào layout
        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)

        # Tạo một widget mới và đặt layout vào widget
        widget = QWidget()
        widget.setLayout(layout)

        # Đặt widget làm nội dung chính của cửa sổ
        self.setCentralWidget(widget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
