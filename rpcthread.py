import pathlib
import subprocess
import time
from PyQt5 import QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal, QThread, pyqtSlot
from commandexecution import Ui_MainWindow


path = str(pathlib.Path.home()) + '/komodo/src/'


# Object, which will be moved to another thread
class RpcWorker(QObject):
    commandInsert = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.command = ""

    @pyqtSlot(str)
    def set_command(self, cmd):
        self.command = cmd

    def execute_command(self):
        proc = subprocess.Popen(self.command, cwd=path, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        stdout = ""
        while True:
            line = proc.stdout.readline()
            if not line:
                proc.stdout.flush()
                proc.terminate()
                break
            out = str(line) + out
        out = stdout.replace("b'", ' ').replace("\\n", " ")
        self.commandInsert.emit(out)


# Object, which will be moved to another thread
class Worker(QObject):
    # This defines a signal called 'progressChanged' that takes
    # one integer argument.
    progressChanged = pyqtSignal(int)

    def axaa(self):
        while True:
            progressbar_value = 0
            while progressbar_value < 100:
                progressbar_value += 1
                self.progressChanged.emit(progressbar_value)
                time.sleep(0.1)


class Deneme(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Deneme, self).__init__(parent)
        self.setupUi(self)
        self.execute_pushButton.clicked.connect(self.execute_cmd)

        self.mythread = QThread()
        self.mythread.start()
        # create object which will be moved to another thread
        self.myworker = Worker()
        # move object to another thread
        self.myworker.moveToThread(self.mythread)
        # after that, we can connect signals from this object to slot in GUI thread
        self.myworker.progressChanged.connect(self.percentage_progress)
        # connect started signal to run method of object in another thread
        self.mythread.started.connect(self.myworker.axaa)

    @pyqtSlot(int)
    def percentage_progress(self, count):
        self.progressBar.setValue(count)

    def execute_cmd(self):
        rpcthread = QThread()
        rpcworker = RpcWorker()
        rpcworker.set_command(self.cmd_lineEdit.text())
        rpcthread.start()
        rpcworker.moveToThread(rpcthread)
        rpcworker.commandInsert.connect(self.setresult)
        rpcthread.started.connect(rpcworker.execute_command)

    @pyqtSlot(str)
    def setresult(self, out):
        self.result_label.setText(out)
        # result = executeproc.execute_cmd(cmd)

        # proc = subprocess.Popen(cmd, cwd=path, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        # stdout = ""
        # while True:
        #     line = proc.stdout.readline()
        #     if not line:
        #         proc.stdout.flush()
        #         proc.terminate()
        #         break
        #     stdout = str(line) + stdout
        # stdout = stdout.replace("b'", ' ').replace("\\n", " ")
        # print(stdout)
        #


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    ui = Deneme()
    ui.show()
    app.exec_()
