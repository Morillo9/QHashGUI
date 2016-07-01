# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QFileDialog
import hashlib

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
        MainWindow.resize(388, 422)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 40, 181, 51))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.comboBox = QtGui.QComboBox(self.widget)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.comboBox)
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.widget1 = QtGui.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(10, 170, 357, 51))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.hash_output = QtGui.QTextEdit(self.widget1)
        self.hash_output.setObjectName(_fromUtf8("hash_output"))
        self.horizontalLayout_2.addWidget(self.hash_output)
        self.label = QtGui.QLabel(self.widget1)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.widget2 = QtGui.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(10, 240, 339, 51))
        self.widget2.setObjectName(_fromUtf8("widget2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget2)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.user_input = QtGui.QTextEdit(self.widget2)
        self.user_input.setObjectName(_fromUtf8("user_input"))
        self.horizontalLayout_3.addWidget(self.user_input)
        self.label_2 = QtGui.QLabel(self.widget2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.widget3 = QtGui.QWidget(self.centralwidget)
        self.widget3.setGeometry(QtCore.QRect(10, 100, 349, 51))
        self.widget3.setObjectName(_fromUtf8("widget3"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.widget3)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.file_directory = QtGui.QTextEdit(self.widget3)
        self.file_directory.setObjectName(_fromUtf8("file_directory"))
        self.horizontalLayout_4.addWidget(self.file_directory)
        self.pushButton = QtGui.QPushButton(self.widget3)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.widget4 = QtGui.QWidget(self.centralwidget)
        self.widget4.setGeometry(QtCore.QRect(10, 310, 369, 77))
        self.widget4.setObjectName(_fromUtf8("widget4"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.widget4)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.comparison_frame = QtGui.QTextEdit(self.widget4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comparison_frame.setFont(font)
        self.comparison_frame.setObjectName(_fromUtf8("comparison_frame"))
        self.horizontalLayout_5.addWidget(self.comparison_frame)
        self.pushButton_2 = QtGui.QPushButton(self.widget4)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_5.addWidget(self.pushButton_2)
        self.pushButton.raise_()
        self.file_directory.raise_()
        self.hash_output.raise_()
        self.comparison_frame.raise_()
        self.label.raise_()
        self.user_input.raise_()
        self.label_2.raise_()
        self.pushButton_2.raise_()
        self.comboBox.raise_()
        self.label_3.raise_()
        self.comparison_frame.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.hash_md5 = None
        self.hash_sha256 = None
        self.hash_sha1 = None

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def Browse(self):

        fname = QFileDialog.getOpenFileName()
        self.file_directory.setText(fname)
        self.hash_md5 = hashlib.md5()
        self.hash_sha256 = hashlib.sha256()
        self.hash_sha1 = hashlib.sha1()
        with open(fname, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                self.hash_md5.update(chunk)
                self.hash_sha256.update(chunk)
                self.hash_sha1.update(chunk)

    def compare_Hashes(self):

        hash_method = str(self.comboBox.currentText())
        if hash_method == 'MD5':
            self.hash_output.setText(self.hash_md5.hexdigest())
        elif hash_method == 'Sha256':
            self.hash_output.setText(self.hash_sha256.hexdigest())
        elif hash_method == 'Sha1':
            self.hash_output.setText(self.hash_sha1.hexdigest())

        a = self.hash_output.toPlainText()
        b = self.user_input.toPlainText()

        if a == b:
            self.comparison_frame.setText("Hashes match, file verified")
        else:
            self.comparison_frame.setText("Hashes DO NOT match, file corrupt")


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "MD5", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "Sha256", None))
        self.comboBox.setItemText(2, _translate("MainWindow", "Sha1", None))
        self.label_3.setText(_translate("MainWindow", "Hash Mode", None))
        self.label.setText(_translate("MainWindow", "Computed Hash", None))
        self.label_2.setText(_translate("MainWindow", "Control Hash", None))
        self.pushButton.setText(_translate("MainWindow", "Select File", None))
        self.pushButton_2.setText(_translate("MainWindow", "Compare Hash \n"
" Strings", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.pushButton.clicked.connect(ui.Browse)
    ui.pushButton_2.clicked.connect(ui.compare_Hashes)
    MainWindow.show()
    sys.exit(app.exec_())

