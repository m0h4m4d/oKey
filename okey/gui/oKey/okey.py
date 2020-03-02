'''
this is sub module or main module outside the path
@author: imitate
@vendor: ispace
@vendor-page: github.com/ispace-port
'''

import os
import sys
import time
import random



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
        MainWindow.resize(640, 480)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(640, 480))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"selection-color: rgb(255, 255, 255);\n"
""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 114, 221, 91))
        font = QtGui.QFont()
        font.setPointSize(62)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(280, 190, 111, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(460, 210, 31, 31))
        self.pushButton.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(180, 210, 281, 31))
        self.lineEdit.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);"))
        self.lineEdit.setText(_fromUtf8(""))
        self.lineEdit.setMaxLength(38)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 640, 25))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuOKey = QtGui.QMenu(self.menuBar)
        self.menuOKey.setObjectName(_fromUtf8("menuOKey"))
        MainWindow.setMenuBar(self.menuBar)
        self.actionP2P = QtGui.QAction(MainWindow)
        self.actionP2P.setObjectName(_fromUtf8("actionP2P"))
        self.actionGenerate_iSpace_Link = QtGui.QAction(MainWindow)
        self.actionGenerate_iSpace_Link.setObjectName(_fromUtf8("actionGenerate_iSpace_Link"))
        self.actionGenerate_Phantom_LInk = QtGui.QAction(MainWindow)
        self.actionGenerate_Phantom_LInk.setObjectName(_fromUtf8("actionGenerate_Phantom_LInk"))
        self.menuOKey.addSeparator()
        self.menuOKey.addAction(self.actionP2P)
        self.menuOKey.addAction(self.actionGenerate_iSpace_Link)
        self.menuOKey.addAction(self.actionGenerate_Phantom_LInk)
        self.menuBar.addAction(self.menuOKey.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.lineEdit, QtCore.SIGNAL(_fromUtf8("editingFinished()")), generate_okey)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("pressed()")), generate_okey)
        QtCore.QObject.connect(self.actionP2P, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), generate_okey)
        QtCore.QObject.connect(self.actionGenerate_iSpace_Link, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), MainWindow.update)
        QtCore.QObject.connect(self.actionGenerate_Phantom_LInk, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), MainWindow.update)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    global ContinueEnter
    def ContinueEnter():
    	pass

    global OK
    def OK():
    	os.system('firefox https://okey.ispace:5000')
    	os.system('python razyar.py')


    global generate_okey
    def generate_okey():
    	okey_code = random.randint(100000, 900000)
    	okeyF = open('jumper.okey', 'w')
    	okeyF.write('#okey:'+str(okey_code))
    	okeyF.close()
    	os.system('python jumper.py')


    global generate_ispace 
    def generate_ispace():
    	pass

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "OKey", None))
        self.label_2.setText(_translate("MainWindow", "OnlineKeyboard", None))
        self.pushButton.setText(_translate("MainWindow", "OK", None))
        self.menuOKey.setTitle(_translate("MainWindow", "OKey", None))
        self.actionP2P.setText(_translate("MainWindow", "Generate OKey Link", None))
        self.actionGenerate_iSpace_Link.setText(_translate("MainWindow", "Generate iSpace Link", None))
        self.actionGenerate_Phantom_LInk.setText(_translate("MainWindow", "Generate Phantom Link", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

