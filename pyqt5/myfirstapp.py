#!/usr/bin/env python3
import sys
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication


class MainWindow(QWidget):
    def __init__(self):
        # Вызываем инитиз суперкласса
        super().__init__()
        # После чего вызываем  метод  главного окна.
        self.main()

    def main(self):
        # Экземпляр кнопки выхода
        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(200,190)
        # Размер окна
        self.center()
        self.setFixedSize(300,240)
        # Иконка
        self.setWindowTitle('MyFirstAPP')
        self.setWindowIcon(QIcon('/usr/share/icons/breeze/apps/16/kdeconnect.svg'))
        self.show()

    def center(self):
        qr = self.frameGeometry()
        print(qr)
        cp = QDesktopWidget().availableGeometry().center()
        print(cp)
        qr.moveCenter(cp)
        self.move(qr.center())

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
