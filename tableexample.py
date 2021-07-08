from tablewidget import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap
import csvops


class Main(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        loadUi("serverDialog.ui", self)
        self.load_data()
        # self.printlogo_pushButton.clicked.connect(self.add_image)
        self.server_tableWidget.cellPressed.connect(self.updatecell)

    def updatecell(self):
        print(self.server_tableWidget.show)

    def load_data(self):
        server_details = [{"username": "John", "servername": "45", "ip address": "New York"},
                          {"username": "Mark", "servername": "40", "ip address": "LA"},
                          {"username": "George", "servername": "30", "ip address": "London"}]
        print(server_details)
        row = 0
        self.server_tableWidget.setRowCount(len(server_details))
        for details in server_details:
            self.server_tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(details["username"])))
            self.server_tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(details["servername"])))
            self.server_tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(details["ip address"])))
            row = row + 1

    def add_image(self):
        # Add the image
        qpixmap = QPixmap('pythonlogo.png')
        self.logo_label.setPixmap(qpixmap)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    main = Main()
    main.show()
    app.exec_()
