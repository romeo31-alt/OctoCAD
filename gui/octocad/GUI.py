#program: Graphical User Interface for OctoCAD
#author: Atharv Darekar
from PyQt5 import QtCore, QtGui, QtWidgets;
from Home import Home;
from Design import Design;
from CADmodel import CADmodel;
import sys;
class GUI():
    def centering(self,arg_window):
        window=arg_window.frameGeometry();
        center=QtWidgets.QDesktopWidget().availableGeometry().center();
        window.moveCenter(center);
        arg_window.move(window.topLeft());
    def openHome(self):
        self.obj_QMainWindow__openHome=QtWidgets.QMainWindow();
        self.centering(self.obj_QMainWindow__openHome);
        self.obj_Home=Home();
        self.obj_Home.setupUi(self.obj_QMainWindow__openHome);
        self.obj_QMainWindow__openHome.show();
        self.obj_Home.btn_design.clicked.connect(self.openDesign);
        self.obj_Home.btn_model.clicked.connect(self.openCADmodel);
    def openDesign(self):
        self.obj_QMainWindow__openDesign=QtWidgets.QMainWindow();
        self.centering(self.obj_QMainWindow__openDesign);
        self.obj_Design=Design();
        self.obj_Design.setupUi(self.obj_QMainWindow__openDesign);
        self.obj_QMainWindow__openHome.close();
        self.obj_QMainWindow__openDesign.show();
    def openCADmodel(self):
        self.obj_QMainWindow__openCADmodel=QtWidgets.QMainWindow();
        self.centering(self.obj_QMainWindow__openCADmodel);
        self.obj_CADmodel=CADmodel();
        self.obj_CADmodel.setupUi(self.obj_QMainWindow__openCADmodel);
        self.obj_QMainWindow__openHome.close();
        self.obj_QMainWindow__openCADmodel.show();
if __name__ == "__main__":
    obj_QApplication=QtWidgets.QApplication(sys.argv)
    obj_GUI=GUI();
    obj_GUI.openHome();
    sys.exit(obj_QApplication.exec_())
