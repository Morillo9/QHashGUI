# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QFileDialog
import hashlib
import binascii

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
        MainWindow.setObjectName(_fromUtf8("QHashCheck"))
        MainWindow.resize(378, 322)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.horizontalLayout_6.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.listWidget_2 = QtGui.QListWidget(self.centralwidget)
        self.listWidget_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.listWidget_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget_2.setObjectName(_fromUtf8("listWidget_2"))
        self.horizontalLayout_2.addWidget(self.listWidget_2)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.user_input = QtGui.QTextEdit(self.centralwidget)
        self.user_input.setObjectName(_fromUtf8("user_input"))
        self.horizontalLayout_3.addWidget(self.user_input)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.comparison_frame = QtGui.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comparison_frame.setFont(font)
        self.comparison_frame.setObjectName(_fromUtf8("comparison_frame"))
        self.horizontalLayout_5.addWidget(self.comparison_frame)
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_5.addWidget(self.pushButton_2)
        self.gridLayout.addLayout(self.horizontalLayout_5, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("QHashCheck", "QHashCheck", None))
        self.pushButton.setText(_translate("QHashCheck", "Select File", None))
        self.label.setText(_translate("QHashCheck", "Computed Hashes", None))
        self.label_2.setText(_translate("QHashCheck", "User Hash               ", None))
        self.pushButton_2.setText(_translate("QHashCheck", "Compare Hash \n"
" Values", None))

    def Browse(self):

        self.listWidget_2.clear()

        fname = QFileDialog.getOpenFileName()
        self.hash_md5 = hashlib.md5()
        self.hash_sha256 = hashlib.sha256()
        self.hash_sha1 = hashlib.sha1()
        self.hash_sha224 = hashlib.sha224()
        self.hash_sha384 = hashlib.sha384()
        self.hash_crc32 = None

        with open(fname, "rb") as f:
            buf = f.read()
            self.hash_crc32 = (binascii.crc32(buf) & 0xFFFFFFFF)
            for chunk in iter(lambda: f.read(4096), b""):
                self.hash_md5.update(chunk)
                self.hash_sha256.update(chunk)
                self.hash_sha1.update(chunk)
                self.hash_sha224.update(chunk)
                self.hash_sha384.update(chunk)


        self.listWidget_2.addItem(self.hash_md5.hexdigest())
        self.listWidget_2.addItem(self.hash_sha1.hexdigest())
        self.listWidget_2.addItem(self.hash_sha256.hexdigest())
        self.listWidget_2.addItem(self.hash_sha224.hexdigest())
        self.listWidget_2.addItem(self.hash_sha384.hexdigest())
        self.listWidget_2.addItem(str(self.hash_crc32))


    def compare_Hashes(self):

        a = self.listWidget_2.item(0).text()
        b = self.listWidget_2.item(1).text()
        c = self.listWidget_2.item(2).text()
        x = self.listWidget_2.item(3).text()
        y = self.listWidget_2.item(4).text()
        z = self.listWidget_2.item(5).text()

        user_input = self.user_input.toPlainText()

        if str(a).rstrip() == str(user_input).rstrip():
            self.comparison_frame.setText("Hashes match, file verified \nMode: MD5")

        elif str(b).rstrip() == str(user_input).rstrip():
            self.comparison_frame.setText("Hashes match, file verified \nMode: SHA1")
        elif str(c).rstrip() == str(user_input).rstrip():
            self.comparison_frame.setText("Hashes match, file verified \nMode: SHA256")
        elif str(x).rstrip() == str(user_input).rstrip():
            self.comparison_frame.setText("Hashes match, file verified \nMode: SHA224")
        elif str(y).rstrip() == str(user_input).rstrip():
            self.comparison_frame.setText("Hashes match, file verified \nMode: SHA384")
        elif str(z).rstrip() == str(user_input).rstrip():
            self.comparison_frame.setText("Hashes match, file verified \nMode: CRC32")
        else:
            self.comparison_frame.setText("Hashes DO NOT match, file corrupt")



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

