# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'commandexecution.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 379)
        MainWindow.setMaximumSize(QtCore.QSize(1024, 800))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.execute_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.execute_pushButton.setObjectName("execute_pushButton")
        self.gridLayout.addWidget(self.execute_pushButton, 1, 1, 1, 1)
        self.cmd_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.cmd_lineEdit.setObjectName("cmd_lineEdit")
        self.gridLayout.addWidget(self.cmd_lineEdit, 1, 0, 1, 1)
        self.result_label = QtWidgets.QLabel(self.centralwidget)
        self.result_label.setMaximumSize(QtCore.QSize(1200, 16777215))
        self.result_label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.result_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.result_label.setText("")
        self.result_label.setObjectName("result_label")
        self.gridLayout.addWidget(self.result_label, 2, 0, 1, 2)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 3, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.cmd_lineEdit.editingFinished.connect(self.execute_pushButton.animateClick)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.execute_pushButton.setText(_translate("MainWindow", "Execute"))
        self.cmd_lineEdit.setPlaceholderText(_translate("MainWindow", "Enter a command"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

