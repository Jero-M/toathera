# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created: Thu May 03 22:21:59 2018
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(292, 243)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.org_label = QtGui.QLabel(self.centralwidget)
        self.org_label.setObjectName(_fromUtf8("org_label"))
        self.gridLayout.addWidget(self.org_label, 0, 0, 1, 1)
        self.org_comboBox = QtGui.QComboBox(self.centralwidget)
        self.org_comboBox.setObjectName(_fromUtf8("org_comboBox"))
        self.gridLayout.addWidget(self.org_comboBox, 0, 1, 1, 1)
        self.project_label = QtGui.QLabel(self.centralwidget)
        self.project_label.setObjectName(_fromUtf8("project_label"))
        self.gridLayout.addWidget(self.project_label, 1, 0, 1, 1)
        self.project_comboBox = QtGui.QComboBox(self.centralwidget)
        self.project_comboBox.setObjectName(_fromUtf8("project_comboBox"))
        self.gridLayout.addWidget(self.project_comboBox, 1, 1, 1, 1)
        self.destination_label = QtGui.QLabel(self.centralwidget)
        self.destination_label.setObjectName(_fromUtf8("destination_label"))
        self.gridLayout.addWidget(self.destination_label, 2, 0, 1, 1)
        self.destination_entry = QtGui.QLineEdit(self.centralwidget)
        self.destination_entry.setObjectName(_fromUtf8("destination_entry"))
        self.gridLayout.addWidget(self.destination_entry, 2, 1, 1, 1)
        self.upload_button = QtGui.QPushButton(self.centralwidget)
        self.upload_button.setObjectName(_fromUtf8("upload_button"))
        self.gridLayout.addWidget(self.upload_button, 3, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.org_label.setText(_translate("MainWindow", "Org:", None))
        self.project_label.setText(_translate("MainWindow", "Project:", None))
        self.destination_label.setText(_translate("MainWindow", "Destination:", None))
        self.upload_button.setText(_translate("MainWindow", "Upload", None))

