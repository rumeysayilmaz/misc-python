import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QFont, QDoubleValidator, QIntValidator, QRegExpValidator

from buycoffee import Ui_MainWindow
from PyQt5.QtCore import QTranslator, pyqtSlot, QSize, QRegExp
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QToolTip
import qtawesome as qta


class CoffeeApp(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(CoffeeApp, self).__init__(parent)
        #   Default Settings
        self.setupUi(self)  # loading from buycoffee.py
        self.support_pushButton.setText('Support')
        self.support_pushButton.setEnabled(False)
        self.cup_lineEdit.setFocus()
        QToolTip.setFont(QFont('SansSerif', 10))
        self.coffee_pushButton.setIcon(qta.icon('fa.coffee'))
        self.coffee_pushButton.setStyleSheet("border-color: brown; border-radius: 10px")
        self.coffee_pushButton.setIconSize(QSize(27, 27))
        self.support_pushButton.setToolTip(self.tr("Treat Marmara Core Team cups of coffee"))
        self.regex = QRegExp("[1-9_]+")
        self.validator = QRegExpValidator(self.regex)
        self.cup_lineEdit.setValidator(self.validator)
        self.cup_lineEdit.textChanged.connect(self.calculate_amount)
        self.cup_lineEdit.returnPressed.connect(self.send_coins_to_team)
        self.support_pushButton.clicked.connect(self.send_coins_to_team)

    @pyqtSlot()
    def calculate_amount(self):
        number_of_cups = self.cup_lineEdit.text()
        if self.cup_lineEdit.text() == "":
            number_of_cups = 0
            self.support_pushButton.setEnabled(False)
            self.support_pushButton.setText('Support')
        else:
            amount = int(number_of_cups) * 50
            self.support_pushButton.setEnabled(True)
            self.support_pushButton.setText('Support (' + str(amount) + ' MCL)')


    @pyqtSlot()
    def send_coins_to_team(self):
        number_of_cups = self.cup_lineEdit.text()
        amount = int(number_of_cups) * 50
        self.support_pushButton.setText('Support (' + str(amount) + ' MCL)')
        # message_box = self.custom_message(self.tr('Confirm Transaction'),
        #                                   self.tr(
        #                                       f'You are about to send {amount} MCL to Marmara Core Team.'),
        #                                   "question",
        #                                   QMessageBox.Question)
        # if message_box == QMessageBox.Yes:
        #     self.worker_sendtoteam = marmarachain_rpc.RpcHandler()
        #     command = cp.sendtoaddress + ' ' + 'team address' + ' ' + str(amount)
        #     print(command)
        #     sendtoteam_thread = self.worker_thread(self.thread_sendtoteam, self.worker_sendtoteam,
        #                                               command)
        #     sendtoteam_thread.command_out.connect(self.send_coins_to_team_result)
        # if message_box == QMessageBox.No:
        #     self.bottom_info(self.tr('Transaction aborted'))

    @pyqtSlot(tuple)
    def send_coins_to_team_result(self, result_out):
        if result_out[0]:
            print(result_out[0])
        elif result_out[1]:
            if self.chain_status is False:
                self.bottom_err_info(self.tr(result_out[1]))
            result = str(result_out[1]).splitlines()
            print(result)
            if str(result_out[1]).find('error message:') != -1:
                index = result.index('error message:') + 1
                self.bottom_info(self.tr(result[index]))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    demo = CoffeeApp()
    demo.show()
    sys.exit(app.exec_())
