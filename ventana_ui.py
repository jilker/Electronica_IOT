# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(928, 548)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Buscar_button = QtWidgets.QPushButton(self.centralwidget)
        self.Buscar_button.setGeometry(QtCore.QRect(330, 190, 171, 51))
        self.Buscar_button.setObjectName("Buscar_button")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 241, 461))
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.Generos_lista = QtWidgets.QListWidget(self.groupBox)
        self.Generos_lista.setGeometry(QtCore.QRect(10, 30, 221, 431))
        self.Generos_lista.setObjectName("Generos_lista")
        self.Siguiente_button = QtWidgets.QPushButton(self.centralwidget)
        self.Siguiente_button.setGeometry(QtCore.QRect(630, 430, 251, 51))
        self.Siguiente_button.setObjectName("Siguiente_button")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(280, 40, 281, 141))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.year_spin = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.year_spin.setMaximum(2020)
        self.year_spin.setProperty("value", 2000)
        self.year_spin.setObjectName("year_spin")
        self.horizontalLayout.addWidget(self.year_spin)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(260, 260, 321, 211))
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.Pictures = QtQuickWidgets.QQuickWidget(self.centralwidget)
        self.Pictures.setGeometry(QtCore.QRect(619, 40, 271, 341))
        self.Pictures.setResizeMode(QtQuickWidgets.QQuickWidget.SizeRootObjectToView)
        self.Pictures.setObjectName("Pictures")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 928, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Buscar_button.setText(_translate("MainWindow", "Buscar"))
        self.groupBox.setTitle(_translate("MainWindow", "Generos"))
        self.Siguiente_button.setText(_translate("MainWindow", "Siguiente"))
        self.label.setText(_translate("MainWindow", "Fecha más antigua"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Información General"))

from PyQt5 import QtQuickWidgets

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

