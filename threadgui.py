# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'threadgui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(674, 311)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(60, 100, 551, 131))
        self.frame.setObjectName("frame")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(180, 20, 160, 89))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stop_thread_1_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.stop_thread_1_pushButton.setObjectName("stop_thread_1_pushButton")
        self.verticalLayout_2.addWidget(self.stop_thread_1_pushButton)
        self.stop_thread_2_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.stop_thread_2_pushButton.setObjectName("stop_thread_2_pushButton")
        self.verticalLayout_2.addWidget(self.stop_thread_2_pushButton)
        self.stop_thread_3_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.stop_thread_3_pushButton.setObjectName("stop_thread_3_pushButton")
        self.verticalLayout_2.addWidget(self.stop_thread_3_pushButton)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(350, 20, 160, 89))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.thread1_progressBar = QtWidgets.QProgressBar(self.verticalLayoutWidget)
        self.thread1_progressBar.setProperty("value", 24)
        self.thread1_progressBar.setObjectName("thread1_progressBar")
        self.verticalLayout.addWidget(self.thread1_progressBar)
        self.thread2_progressBar = QtWidgets.QProgressBar(self.verticalLayoutWidget)
        self.thread2_progressBar.setProperty("value", 24)
        self.thread2_progressBar.setObjectName("thread2_progressBar")
        self.verticalLayout.addWidget(self.thread2_progressBar)
        self.thread3_progressBar = QtWidgets.QProgressBar(self.verticalLayoutWidget)
        self.thread3_progressBar.setProperty("value", 24)
        self.thread3_progressBar.setObjectName("thread3_progressBar")
        self.verticalLayout.addWidget(self.thread3_progressBar)
        self.gridLayoutWidget = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 160, 89))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.start_thread1_pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.start_thread1_pushButton.setObjectName("start_thread1_pushButton")
        self.gridLayout.addWidget(self.start_thread1_pushButton, 1, 0, 1, 1)
        self.start_thread3_pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.start_thread3_pushButton.setObjectName("start_thread3_pushButton")
        self.gridLayout.addWidget(self.start_thread3_pushButton, 4, 0, 1, 1)
        self.start_thread2_pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.start_thread2_pushButton.setObjectName("start_thread2_pushButton")
        self.gridLayout.addWidget(self.start_thread2_pushButton, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 674, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.frame.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>this is a frame</p></body></html>"))
        self.stop_thread_1_pushButton.setText(_translate("MainWindow", "Stop Thread 1"))
        self.stop_thread_2_pushButton.setText(_translate("MainWindow", "Stop Thread 2"))
        self.stop_thread_3_pushButton.setText(_translate("MainWindow", "Stop Thread 3"))
        self.start_thread1_pushButton.setText(_translate("MainWindow", "Start Thread 1"))
        self.start_thread3_pushButton.setText(_translate("MainWindow", "Start Thread 3"))
        self.start_thread2_pushButton.setText(_translate("MainWindow", "Start Thread 2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

