#program: Graphical User Interface for OctoCAD
#author: Atharv Darekar
from PySide2.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QWidget, QGroupBox, QStackedWidget, QGridLayout, QVBoxLayout, QPushButton, QDialog, QLabel;
from PySide2.QtGui import QIcon, QFont, QDoubleValidator;
from PySide2.QtCore import QSize;
import sys;
import os;
class Main(QWidget):
    def __init__(self):
        super(Main, self).__init__();
        self.obj_QWidget____init__=QWidget();
        self.obj_QWidget____init__.setWindowTitle("OctoCAD\N{COPYRIGHT SIGN}");
        self.obj_QWidget____init__.setGeometry(0,0,600,400);
        self.setIcon(self.obj_QWidget____init__);
        self.centering(self.obj_QWidget____init__);
        self.createMainLayout(self.obj_QWidget____init__);
        vbox=QVBoxLayout();
        vbox.addWidget(self.groupBox__createMainLayout);
        self.obj_QWidget____init__.setLayout(vbox);
        self.obj_QWidget____init__.show();
    def setIcon(self,arg_window):
        icon=QIcon("/home/ubuntu/modules-OctoCAD/gui/v-20200807/logo_transparent_enlarged.png");
        arg_window.setWindowIcon(icon);
    def centering(self,arg_window):
        window=arg_window.frameGeometry();
        center=QDesktopWidget().availableGeometry().center();
        window.moveCenter(center);
        arg_window.move(window.topLeft());
    def createMainLayout(self,arg_window):
        self.groupBox__createMainLayout=QGroupBox("Home");
        self.groupBox__createMainLayout.setFont(QFont("Sanserif",13));
        grid=QGridLayout();
        btn_design=QPushButton("Design",self);
        btn_design.setIcon(QIcon("/home/ubuntu/modules-OctoCAD/gui/v-20200807/design.png"));
        btn_design.setIconSize(QSize(80,80));
        btn_design.setMinimumHeight(200);
        grid.addWidget(btn_design,0,0);
        btn_design.clicked.connect(self.design);
        btn_3dmodel=QPushButton("Generate 3-D model");
        btn_3dmodel.setIcon(QIcon("/home/ubuntu/modules-OctoCAD/gui/v-20200807/3d-modeling.png"));
        btn_3dmodel.setIconSize(QSize(80,80));
        btn_3dmodel.setMinimumHeight(200);
        grid.addWidget(btn_3dmodel,0,1);
        btn_3dmodel.clicked.connect(self.cadmodel);
        btn_help=QPushButton("Help");
        btn_help.setIcon(QIcon("/home/ubuntu/modules-OctoCAD/gui/v-20200807/information.png"));
        btn_help.setIconSize(QSize(80,80));
        btn_help.setMinimumHeight(200);
        grid.addWidget(btn_help,1,0);
        btn_about=QPushButton("About Us");
        btn_about.setIcon(QIcon("/home/ubuntu/modules-OctoCAD/gui/v-20200807/about-us.png"));
        btn_about.setIconSize(QSize(80,80));
        btn_about.setMinimumHeight(200);
        grid.addWidget(btn_about,1,1);
        self.groupBox__createMainLayout.setLayout(grid);
    def design(self):
        self.obj_QWidget__design=QWidget();
        self.obj_QWidget__design.setWindowTitle("Design");
        self.obj_QWidget__design.setGeometry(0,0,600,400);
        self.centering(self.obj_QWidget__design);
        vbox=QVBoxLayout();
        self.obj_QStackedWidget__design=QStackedWidget();
        vbox.addWidget(self.obj_QStackedWidget__design);
        label=QLabel("Select");
        self.obj_QStackedWidget__design.addWidget(label);
        for x in range(0,8):
            self.button=QPushButton("<module "+str(x)+">");
            vbox.addWidget(self.button);
        vbox.addWidget(self.obj_QStackedWidget__design);
        self.obj_QWidget__design.setLayout(vbox);
        self.obj_QWidget__design.show();
        self.obj_QWidget____init__.close();
    def cadmodel(self):
        self.obj_QWidget__cadmodel=QWidget();
        self.obj_QWidget__cadmodel.setWindowTitle("3-D Model");
        self.obj_QWidget__cadmodel.setGeometry(0,0,600,400);
        self.centering(self.obj_QWidget__cadmodel);
        vbox=QVBoxLayout();
        self.obj_QStackedWidget__cadmodel=QStackedWidget();
        vbox.addWidget(self.obj_QStackedWidget__cadmodel);
        label=QLabel("Select");
        self.obj_QStackedWidget__cadmodel.addWidget(label);
        for x in range(0,8):
            self.button=QPushButton("<module "+str(x)+">");
            vbox.addWidget(self.button);
        vbox.addWidget(self.obj_QStackedWidget__cadmodel);
        self.obj_QWidget__cadmodel.setLayout(vbox);
        self.obj_QWidget__cadmodel.show();
        self.obj_QWidget____init__.close();
class Controller():
    def __init__(self):
        pass;
obj_QApplication=QApplication(sys.argv);
obj_Main=Main();
obj_QApplication.exec_();
sys.exit(0);
