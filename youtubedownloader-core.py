# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from appcore import Downloader


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(10, 60, 371, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.btnDownload = QtWidgets.QPushButton(Form)
        self.btnDownload.setGeometry(QtCore.QRect(140, 110, 89, 25))
        self.btnDownload.setObjectName("btnDownload")

        self.retranslateUi(Form)
        self.btnDownload.clicked.connect(self.btnDownload_click)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Youtube Downloader"))
        self.btnDownload.setText(_translate("Form", "Download"))

    def btnDownload_click(self):
        if len(self.lineEdit.text())>0:
            print(self.lineEdit.text())
            dl = Downloader.Downloader(self.lineEdit.text())
            dl.download()
            print('Done')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())