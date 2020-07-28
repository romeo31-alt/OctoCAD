#program: Graphical User Interface for OctoCAD
#author: Atharv Darekar
from PySide2.QtWidgets import (QApplication, QDesktopWidget, QComboBox, QDialog, QMessageBox, QDialogButtonBox,
                               QFormLayout, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QDoubleSpinBox,
                               QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit, QVBoxLayout);
from PySide2.QtGui import QIcon, QFont, QDoubleValidator;
from PySide2.QtCore import QSize;
import sys;
import os;
class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__();
        self.setWindowTitle("OctoCAD\N{COPYRIGHT SIGN}");
        self.setGeometry(0,0,600,400);
        self.setIcon();
        self.centering();
        self.createLayout();
        vbox=QVBoxLayout();
        vbox.addWidget(self.groupBox);
        self.setLayout(vbox);
        self.show();
    def setIcon(self):
        icon=QIcon("/home/ubuntu/modules-OctoCAD/gui/v-20200807/logo_transparent_enlarged.png");
        self.setWindowIcon(icon);
    def centering(self):
        window=self.frameGeometry();
        center=QDesktopWidget().availableGeometry().center();
        window.moveCenter(center);
        self.move(window.topLeft());
    def createLayout(self):
        self.groupBox=QGroupBox("Select");
        self.groupBox.setFont(QFont("Sanserif",13));
        hbox=QHBoxLayout();
        btn_design=QPushButton("Design");
        btn_design.setIcon(QIcon("/home/ubuntu/modules-OctoCAD/gui/v-20200807/design.png"));
        btn_design.setIconSize(QSize(80,80));
        btn_design.setMinimumHeight(200);
        hbox.addWidget(btn_design);
        btn_3dmodel=QPushButton("Generate 3-D model");
        btn_3dmodel.setIcon(QIcon("/home/ubuntu/modules-OctoCAD/gui/v-20200807/3d-modeling.png"));
        btn_3dmodel.setIconSize(QSize(80,80));
        btn_3dmodel.setMinimumHeight(200);
        hbox.addWidget(btn_3dmodel);
        self.groupBox.setLayout(hbox);
obj_QApplication=QApplication(sys.argv);
obj_Main=Main();
obj_QApplication.exec_();
sys.exit(0);
