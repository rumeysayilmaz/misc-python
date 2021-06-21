import pathlib
import subprocess
import time
from PyQt5 import QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal, QThread, pyqtSlot
from commandexecution import Ui_MainWindow

path = str(pathlib.Path.home())


# Object, which will be moved to another thread
class RpcWorker(QObject):
    # This defines a signal called 'commandInsert' that takes
    # one string argument.
    commandInsert = pyqtSignal(str)
    finished = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.command = ""

    @pyqtSlot(str)
    def set_command(self, cmd):
        self.command = cmd

    @pyqtSlot()
    def do_execute_command(self):
        print(f'Beginning executing command: {self.command}')
        self._execute_command()
        self.finished.emit()

    def _execute_command(self):
        print("inside execute command")
        proc = subprocess.Popen(self.command, cwd=path, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out = ""
        while True:
            line = proc.stdout.readline()
            if not line:
                proc.stdout.flush()
                proc.terminate()
                break
            out = str(line) + out
        out = out.replace("b'", ' ').replace("\\n", " ")
        self.commandInsert.emit(out)


# Object, which will be moved to another thread
class Worker(QObject):
    # This defines a signal called 'progressChanged' that takes
    # one integer argument.
    progressChanged = pyqtSignal(int)

    def progressing(self):
        while True:
            progressbar_value = 0
            while progressbar_value < 100:
                progressbar_value += 1
                self.progressChanged.emit(progressbar_value)
                time.sleep(0.1)


class MainGui(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainGui, self).__init__(parent)
        self.setupUi(self)

        # create thread
        self.mythread = QThread()
        # create object which will be moved to another thread
        self.myworker = RpcWorker()
        # create thread
        self.progressthread = QThread()
        # create object which will be moved to another thread
        self.progressworker = Worker()
        # move object to another thread
        self.progressworker.moveToThread(self.progressthread)
        # after that, we can connect signals from this object to slot in GUI thread
        self.progressworker.progressChanged.connect(self.percentage_progress)
        # connect started signal to run method of object in another thread
        self.progressthread.started.connect(self.progressworker.progressing)
        # start thread
        self.progressthread.start()
        self.execute_pushButton.clicked.connect(self.get_input)

    @pyqtSlot(int)
    def percentage_progress(self, count):
        self.progressBar.setValue(count)

    def get_input(self):
        cmd = self.cmd_lineEdit.text()
        workerthread = self.worker_thread(cmd, self.mythread, self.myworker)
        workerthread.connect(self.setresult)

    def worker_thread(self, cmd, thread, worker):
        worker.set_command(cmd)
        thread.start()
        worker.finished.connect(thread.quit)
        worker.moveToThread(thread)
        thread.started.connect(worker.do_execute_command)
        return worker.commandInsert

    @pyqtSlot(str)
    def setresult(self, out):
        self.result_label.setText(out)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    ui = MainGui()
    ui.show()
    app.exec_()
