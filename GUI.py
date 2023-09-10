#!/usr/bin/python3
#
# Forked from https://www.pythonguis.com/tutorials/qprocess-external-programs/
#

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtCore import QProcess

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        self.board = ""
        self.fname = None
        self.p = None

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 40, 80, 25))
        self.pushButton.setText("Detect Board")
        self.dropdownlist = QtWidgets.QComboBox(self.centralwidget)
        self.dropdownlist.setGeometry(QtCore.QRect(220, 40, 100, 25))
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 140, 80, 25))
        self.pushButton_3.setText("Open .fs File")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(220, 140, 80, 25))
        self.pushButton_4.setText("Flash")
        self.pushButton_4.setDisabled (True)
        self.text = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.text.setGeometry(QtCore.QRect(10, 200, 380, 260))
        self.text.setObjectName("textEdit")
        self.text.setReadOnly(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.dropdownlist.addItem("tangnano1k")
        self.dropdownlist.addItem("tangnano4k")
        self.dropdownlist.addItem("tangnano9k")

        self.pushButton.pressed.connect(self.connection)
        self.pushButton_3.pressed.connect(self.openfile)
        self.pushButton_4.pressed.connect(self.start_process)
        self.dropdownlist.activated.connect(self.activated)

    def connection(self):
        if self.p is None:  # No process running.
            self.message("Executing process")
            self.p = QProcess()  # Keep a reference to the QProcess (e.g. on self) while it's running.
            self.p.readyReadStandardOutput.connect(self.handle_stdout)
            self.p.readyReadStandardError.connect(self.handle_stderr)
            self.p.stateChanged.connect(self.handle_state)
            self.p.finished.connect(self.process_finished)  # Clean up once complete.
            self.p.start("pkexec openFPGALoader --detect")

    def activated(self):
        self.board = self.dropdownlist.currentText()

    def openfile(self):
        self.fname = QFileDialog.getOpenFileName(None, 'Open file', './', '*.fs')
        self.pushButton_4.setEnabled(True)

    def message(self, s):
        self.text.appendPlainText(s)

    def start_process(self):
        if self.p is None:  # No process running.
            self.message("Executing process")
            self.p = QProcess()  # Keep a reference to the QProcess (e.g. on self) while it's running.
            self.p.readyReadStandardOutput.connect(self.handle_stdout)
            self.p.readyReadStandardError.connect(self.handle_stderr)
            self.p.stateChanged.connect(self.handle_state)
            self.p.finished.connect(self.process_finished)  # Clean up once complete.
            self.p.start("pkexec openFPGALoader -b " + self.board + " -f " + self.fname[0])

    def handle_stderr(self):
        data = self.p.readAllStandardError()
        stderr = bytes(data).decode("utf8")
        self.message(stderr)

    def handle_stdout(self):
        data = self.p.readAllStandardOutput()
        stdout = bytes(data).decode("utf8")
        self.message(stdout)

    def handle_state(self, state):
        states = {
            QProcess.NotRunning: 'Not running',
            QProcess.Starting: 'Starting',
            QProcess.Running: 'Running',
        }
        state_name = states[state]
        #self.message(f"State changed: {state_name}")

    def process_finished(self):
        self.message("Process finished.")
        self.p = None


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    w = QtWidgets.QMainWindow()
    ui.setupUi(w)
    w.show()
    sys.exit(app.exec_())
