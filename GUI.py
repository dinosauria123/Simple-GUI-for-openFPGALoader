#!/usr/bin/python3
#
# Forked from https://www.pythonguis.com/tutorials/qprocess-external-programs/
#

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtCore import QProcess

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        self.board = "ac701"
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

        self.dropdownlist.addItem("ac701")
        self.dropdownlist.addItem("acornCle215")
        self.dropdownlist.addItem("litex-acorn-baseboard-mini")
        self.dropdownlist.addItem("alchitry_au")
        self.dropdownlist.addItem("alchitry_au_plus")
        self.dropdownlist.addItem("alinx_ax516")
        self.dropdownlist.addItem("analogMax")
        self.dropdownlist.addItem("arty_a7_35t")
        self.dropdownlist.addItem("arty_a7_100t")
        self.dropdownlist.addItem("arty_s7_25")
        self.dropdownlist.addItem("arty_s7_50")
        self.dropdownlist.addItem("arty_z7_10")
        self.dropdownlist.addItem("arty_z7_20")
        self.dropdownlist.addItem("arty")
        self.dropdownlist.addItem("axu2cga")
        self.dropdownlist.addItem("basys3")
        self.dropdownlist.addItem("cmod_s7")
        self.dropdownlist.addItem("gatemate_evb_jtag")
        self.dropdownlist.addItem("gatemate_evb_spi")
        self.dropdownlist.addItem("gatemate_pgm_spi")
        self.dropdownlist.addItem("cmoda7_35t")
        self.dropdownlist.addItem("colorlight")
        self.dropdownlist.addItem("colorlight-i5")
        self.dropdownlist.addItem("colorlight-i9")
        self.dropdownlist.addItem("colorlight-i9+")
        self.dropdownlist.addItem("crosslinknx_evn")
        self.dropdownlist.addItem("cyc1000")
        self.dropdownlist.addItem("c10lp-refkit")
        self.dropdownlist.addItem("c5g")
        self.dropdownlist.addItem("de0")
        self.dropdownlist.addItem("de0nano")
        self.dropdownlist.addItem("de0nanoSoc")
        self.dropdownlist.addItem("de10lite")
        self.dropdownlist.addItem("de10nano")
        self.dropdownlist.addItem("de1Soc")
        self.dropdownlist.addItem("deca")
        self.dropdownlist.addItem("ecp5_evn")
        self.dropdownlist.addItem("ecpix5")
        self.dropdownlist.addItem("fireant")
        self.dropdownlist.addItem("fomu")
        self.dropdownlist.addItem("honeycomb")
        self.dropdownlist.addItem("hseda-xc6slx16")
        self.dropdownlist.addItem("ice40_generic")
        self.dropdownlist.addItem("icebreaker-bitsy")
        self.dropdownlist.addItem("kc705")
        self.dropdownlist.addItem("LD-KONFEKT")
        self.dropdownlist.addItem("LD-SCHOKO")
        self.dropdownlist.addItem("licheeTang")
        self.dropdownlist.addItem("machXO2EVN")
        self.dropdownlist.addItem("machXO3EVN")
        self.dropdownlist.addItem("machXO3SK")
        self.dropdownlist.addItem("mini_itx")
        self.dropdownlist.addItem("nexys_a7_50")
        self.dropdownlist.addItem("nexys_a7_100")
        self.dropdownlist.addItem("nexysVideo")
        self.dropdownlist.addItem("xem8320")
        self.dropdownlist.addItem("orbtrace_dfu")
        self.dropdownlist.addItem("orangeCrab")
        self.dropdownlist.addItem("papilio_one")
        self.dropdownlist.addItem("pipistrello")
        self.dropdownlist.addItem("pynq_z2")
        self.dropdownlist.addItem("qmtechCyclone10")
        self.dropdownlist.addItem("qmtechCycloneIV")
        self.dropdownlist.addItem("qmtechCycloneV")
        self.dropdownlist.addItem("qmtechCycloneV_5ce523")
        self.dropdownlist.addItem("qmtechKintex7")
        self.dropdownlist.addItem("genesys2")
        self.dropdownlist.addItem("redpitaya14")
        self.dropdownlist.addItem("runber")
        self.dropdownlist.addItem("spartanEdgeAccelBoard")
        self.dropdownlist.addItem("SPEC150")
        self.dropdownlist.addItem("stlv7325")
        self.dropdownlist.addItem("tangnano")
        self.dropdownlist.addItem("tangnano1k")
        self.dropdownlist.addItem("tangnano4k")
        self.dropdownlist.addItem("tangnano9k")
        self.dropdownlist.addItem("tangnano20k")
        self.dropdownlist.addItem("tangprimer20k")
        self.dropdownlist.addItem("tec0117")
        self.dropdownlist.addItem("trion_t120_bga576_spi")
        self.dropdownlist.addItem("trion_ti60_f225_spi")
        self.dropdownlist.addItem("ulx3s")
        self.dropdownlist.addItem("ulx3s_dfu")
        self.dropdownlist.addItem("xtrx")
        self.dropdownlist.addItem("xyloni_spi")
        self.dropdownlist.addItem("usrpx300")
        self.dropdownlist.addItem("usrpx310")
        self.dropdownlist.addItem("xmf3")
        self.dropdownlist.addItem("zc702")
        self.dropdownlist.addItem("zc706")
        self.dropdownlist.addItem("zcu102")
        self.dropdownlist.addItem("zcu106")
        self.dropdownlist.addItem("zedboard")
        self.dropdownlist.addItem("zybo_z7_10")
        self.dropdownlist.addItem("zybo_z7_20")
        self.dropdownlist.addItem("vcu118")
        self.dropdownlist.addItem("vcu128")
        self.dropdownlist.addItem("kcu116")

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
