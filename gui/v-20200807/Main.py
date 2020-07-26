#program: Graphical User Interface for OctoCAD
#author: Atharv Darekar
from PySide2.QtWidgets import (QApplication, QDesktopWidget, QComboBox, QDialog, QMessageBox, QDialogButtonBox,
                               QFormLayout, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QDoubleSpinBox,
                               QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit, QVBoxLayout);
from PySide2.QtGui import QIcon, QFont, QDoubleValidator;
import sys;
import os;
class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__();
        self.setWindowTitle("OctoCAD\N{COPYRIGHT SIGN}");
        self.setGeometry(0,0,600,400);
        self.setIcon();
        self.centering();
        self.show();
    def setIcon(self):
        icon=QIcon("/home/ubuntu/modules-OctoCAD/gui/v-20200807/logo_transparent_enlarged.png");
        self.setWindowIcon(icon);
    def centering(self):
        window=self.frameGeometry();
        center=QDesktopWidget().availableGeometry().center();
        window.moveCenter(center);
        self.move(window.topLeft());
obj_QApplication=QApplication(sys.argv);
obj_Main=Main();
obj_QApplication.exec_();
sys.exit(0);
