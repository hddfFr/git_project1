import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class MyWidget(QMainWindow):

    def __init__(self):
        super().__init__()
        # self.setupUi(self)
        uic.loadUi("C:/Users/Тимофей/Desktop/Duolingo2.ui", self)
        # self.basic_btn.clicked.connect(self.window2)



    def main_window(self):
        self.basic_btn.clicked.connect(self.window_2)


    def window_2(self):
        self.w = Window2()
        self.w.show()
        self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())