#program: Graphical User Interface for OctoCAD
#author: Atharv Darekar
from PySide2.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QWidget, QGroupBox, QHBoxLayout, QVBoxLayout, QPushButton, QDialog;
from PySide2.QtGui import QIcon, QFont, QDoubleValidator;
from PySide2.QtCore import QSize;
import sys;
import os;
class Main(QWidget):
    def __init__(self):
        super(Main, self).__init__();
        self.setWindowTitle("OctoCAD\N{COPYRIGHT SIGN}");
        self.setGeometry(0,0,600,400);
        self.setIcon();
        self.centering();
        self.createMainLayout();
        vbox=QVBoxLayout();
        vbox.addWidget(self.groupBox__createMainLayout);
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
    def createMainLayout(self):
        self.groupBox__createMainLayout=QGroupBox("Select");
        self.groupBox__createMainLayout.setFont(QFont("Sanserif",13));
        hbox=QHBoxLayout();
        btn_design=QPushButton("Design");
        btn_design.setIcon(QIcon("/home/ubuntu/modules-OctoCAD/gui/v-20200807/design.png"));
        btn_design.setIconSize(QSize(80,80));
        btn_design.setMinimumHeight(200);
        hbox.addWidget(btn_design);
        btn_design.clicked.connect(self.design);
        btn_3dmodel=QPushButton("Generate 3-D model");
        btn_3dmodel.setIcon(QIcon("/home/ubuntu/modules-OctoCAD/gui/v-20200807/3d-modeling.png"));
        btn_3dmodel.setIconSize(QSize(80,80));
        btn_3dmodel.setMinimumHeight(200);
        hbox.addWidget(btn_3dmodel);
        btn_3dmodel.clicked.connect(self.cadmodel);
        self.groupBox__createMainLayout.setLayout(hbox);
    def design(self):
        self.obj_QWidget__modules=QWidget();
        self.obj_QWidget__modules.setWindowTitle("Design");
        self.obj_QWidget__modules.setGeometry(0,0,600,400);
        groupBox=QGroupBox("Select");
        groupBox.setFont(QFont("Sanserif",13));
        hbox=QHBoxLayout();
        btn_module=QPushButton("<module>");
        btn_module.setIcon(QIcon("/home/ubuntu/modules-OctoCAD/gui/v-20200807/modules.png"));
        btn_module.setIconSize(QSize(40,40));
        btn_module.setMinimumHeight(100);
        hbox.addWidget(btn_module);
        groupBox.setLayout(hbox);
        vbox=QVBoxLayout();
        vbox.addWidget(groupBox);
        self.obj_QWidget__modules.setLayout(vbox);
        self.obj_QWidget__modules.show();
        self.hide();
    def cadmodel(self):
        self.obj_QWidget__cadmodel=QWidget();
        self.obj_QWidget__cadmodel.setWindowTitle("3-D Model");
        self.obj_QWidget__cadmodel.setGeometry(0,0,600,400);
        groupBox=QGroupBox("Select");
        groupBox.setFont(QFont("Sanserif",13));
        hbox=QHBoxLayout();
        btn_module=QPushButton("<module>");
        btn_module.setIcon(QIcon("/home/ubuntu/modules-OctoCAD/gui/v-20200807/modules.png"));
        btn_module.setIconSize(QSize(40,40));
        btn_module.setMinimumHeight(100);
        hbox.addWidget(btn_module);
        groupBox.setLayout(hbox);
        vbox=QVBoxLayout();
        vbox.addWidget(groupBox);
        self.obj_QWidget__cadmodel.setLayout(vbox);
        self.obj_QWidget__cadmodel.show();
        self.hide();
obj_QApplication=QApplication(sys.argv);
obj_Main=Main();
obj_QApplication.exec_();
sys.exit(0);
