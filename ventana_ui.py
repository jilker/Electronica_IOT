# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'M_ventana_ui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(987, 653)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 241, 491))
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.Generos_lista = QtWidgets.QListWidget(self.groupBox)
        self.Generos_lista.setGeometry(QtCore.QRect(10, 30, 221, 431))
        self.Generos_lista.setObjectName("Generos_lista")
        self.Siguiente_button = QtWidgets.QPushButton(self.centralwidget)
        self.Siguiente_button.setGeometry(QtCore.QRect(690, 440, 251, 51))
        self.Siguiente_button.setObjectName("Siguiente_button")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(280, 40, 371, 141))
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
        self.Buscar_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Buscar_button.setObjectName("Buscar_button")
        self.verticalLayout_2.addWidget(self.Buscar_button)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(270, 190, 391, 351))
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowser.setGeometry(QtCore.QRect(10, 27, 372, 318))
        self.textBrowser.setObjectName("textBrowser")
        self.Pictures = QtWidgets.QLabel(self.centralwidget)
        self.Pictures.setGeometry(QtCore.QRect(670, 20, 311, 381))
        self.Pictures.setText("")
        self.Pictures.setScaledContents(True)
        self.Pictures.setWordWrap(False)
        self.Pictures.setOpenExternalLinks(False)
        self.Pictures.setObjectName("Pictures")
        self.Aceptar_button = QtWidgets.QPushButton(self.centralwidget)
        self.Aceptar_button.setGeometry(QtCore.QRect(690, 510, 251, 51))
        self.Aceptar_button.setObjectName("Aceptar_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 987, 22))
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
        self.groupBox.setTitle(_translate("MainWindow", "Generos"))
        self.Siguiente_button.setText(_translate("MainWindow", "Siguiente"))
        self.label.setText(_translate("MainWindow", "Fecha más antigua"))
        self.Buscar_button.setText(_translate("MainWindow", "Buscar"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Información General"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.Aceptar_button.setText(_translate("MainWindow", "Selecionar"))

