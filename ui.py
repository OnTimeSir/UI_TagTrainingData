# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_UiBaseWindow(object):
    def setupUi(self, UiBaseWindow):
        UiBaseWindow.setObjectName("UiBaseWindow")
        UiBaseWindow.resize(1360, 850)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(UiBaseWindow.sizePolicy().hasHeightForWidth())
        UiBaseWindow.setSizePolicy(sizePolicy)
        UiBaseWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        UiBaseWindow.setStyleSheet("background-color: rgb(64, 66, 68);")
        self.UiWidget = QtWidgets.QWidget(UiBaseWindow)
        self.UiWidget.setObjectName("UiWidget")
        self.FrameView = QtWidgets.QGraphicsView(self.UiWidget)
        self.FrameView.setGeometry(QtCore.QRect(16, 25, 1040, 788))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FrameView.sizePolicy().hasHeightForWidth())
        self.FrameView.setSizePolicy(sizePolicy)
        self.FrameView.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.FrameView.setMouseTracking(False)
        self.FrameView.setStyleSheet("background-color: rgb(242, 242, 242);")
        self.FrameView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.FrameView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.FrameView.setObjectName("FrameView")
        self.InfoPanel = QtWidgets.QFrame(self.UiWidget)
        self.InfoPanel.setGeometry(QtCore.QRect(1060, 25, 281, 788))
        self.InfoPanel.setStyleSheet("background-color: rgb(242, 242, 242);")
        self.InfoPanel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.InfoPanel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.InfoPanel.setObjectName("InfoPanel")
        self.OpenVedioButton = QtWidgets.QPushButton(self.InfoPanel)
        self.OpenVedioButton.setGeometry(QtCore.QRect(30, 30, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.OpenVedioButton.setFont(font)
        self.OpenVedioButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.OpenVedioButton.setStyleSheet("background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.5, fx:0.494, fy:0.506, stop:0.0852273 rgba(255, 255, 255, 255), stop:0.892045 rgba(0, 0, 0, 227));\n"
"color: rgb(0, 0, 0);\n"
"")
        self.OpenVedioButton.setObjectName("OpenVedioButton")
        self.NextButton = QtWidgets.QPushButton(self.InfoPanel)
        self.NextButton.setGeometry(QtCore.QRect(150, 140, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.NextButton.setFont(font)
        self.NextButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.NextButton.setStyleSheet("background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.5, fx:0.494, fy:0.506, stop:0.0852273 rgba(255, 255, 255, 255), stop:0.892045 rgba(0, 0, 0, 227));\n"
"color: rgb(0, 0, 0);\n"
"")
        self.NextButton.setDefault(False)
        self.NextButton.setFlat(False)
        self.NextButton.setObjectName("NextButton")
        self.ClassComboBox = QtWidgets.QComboBox(self.InfoPanel)
        self.ClassComboBox.setGeometry(QtCore.QRect(150, 380, 91, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.ClassComboBox.setFont(font)
        self.ClassComboBox.setObjectName("ClassComboBox")
        self.ClassComboBox.addItem("")
        self.Classlabel = QtWidgets.QLabel(self.InfoPanel)
        self.Classlabel.setGeometry(QtCore.QRect(30, 380, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Classlabel.setFont(font)
        self.Classlabel.setAutoFillBackground(False)
        self.Classlabel.setObjectName("Classlabel")
        self.CloseFileButton = QtWidgets.QPushButton(self.InfoPanel)
        self.CloseFileButton.setGeometry(QtCore.QRect(150, 250, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.CloseFileButton.setFont(font)
        self.CloseFileButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CloseFileButton.setStyleSheet("background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.5, fx:0.494, fy:0.506, stop:0.0852273 rgba(255, 255, 255, 255), stop:0.892045 rgba(0, 0, 0, 227));\n"
"color: rgb(0, 0, 0);\n"
"")
        self.CloseFileButton.setDefault(False)
        self.CloseFileButton.setFlat(False)
        self.CloseFileButton.setObjectName("CloseFileButton")
        self.tabWidget = QtWidgets.QTabWidget(self.InfoPanel)
        self.tabWidget.setGeometry(QtCore.QRect(10, 460, 261, 311))
        self.tabWidget.setObjectName("tabWidget")
        self.InfoTab = QtWidgets.QWidget()
        self.InfoTab.setObjectName("InfoTab")
        self.MsgInfo = QtWidgets.QTextBrowser(self.InfoTab)
        self.MsgInfo.setGeometry(QtCore.QRect(8, 10, 241, 341))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.MsgInfo.setFont(font)
        self.MsgInfo.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.MsgInfo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.MsgInfo.setOpenLinks(True)
        self.MsgInfo.setObjectName("MsgInfo")
        self.tabWidget.addTab(self.InfoTab, "")
        self.ListTab = QtWidgets.QWidget()
        self.ListTab.setObjectName("ListTab")
        self.TagInfo = QtWidgets.QTextBrowser(self.ListTab)
        self.TagInfo.setGeometry(QtCore.QRect(8, 10, 241, 341))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.TagInfo.setFont(font)
        self.TagInfo.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.TagInfo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.TagInfo.setOpenLinks(True)
        self.TagInfo.setObjectName("TagInfo")
        self.tabWidget.addTab(self.ListTab, "")
        self.Sizelabel = QtWidgets.QLabel(self.InfoPanel)
        self.Sizelabel.setGeometry(QtCore.QRect(30, 420, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Sizelabel.setFont(font)
        self.Sizelabel.setAutoFillBackground(False)
        self.Sizelabel.setObjectName("Sizelabel")
        self.SizeComboBox = QtWidgets.QComboBox(self.InfoPanel)
        self.SizeComboBox.setGeometry(QtCore.QRect(150, 420, 91, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.SizeComboBox.setFont(font)
        self.SizeComboBox.setObjectName("SizeComboBox")
        self.SizeComboBox.addItem("")
        self.PrevButton = QtWidgets.QPushButton(self.InfoPanel)
        self.PrevButton.setGeometry(QtCore.QRect(30, 140, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.PrevButton.setFont(font)
        self.PrevButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PrevButton.setStyleSheet("background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.5, fx:0.494, fy:0.506, stop:0.0852273 rgba(255, 255, 255, 255), stop:0.892045 rgba(0, 0, 0, 227));\n"
"color: rgb(0, 0, 0);\n"
"")
        self.PrevButton.setDefault(False)
        self.PrevButton.setFlat(False)
        self.PrevButton.setObjectName("PrevButton")
        self.OpenPictureButton = QtWidgets.QPushButton(self.InfoPanel)
        self.OpenPictureButton.setGeometry(QtCore.QRect(150, 30, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.OpenPictureButton.setFont(font)
        self.OpenPictureButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.OpenPictureButton.setStyleSheet("background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.5, fx:0.494, fy:0.506, stop:0.0852273 rgba(255, 255, 255, 255), stop:0.892045 rgba(0, 0, 0, 227));\n"
"color: rgb(0, 0, 0);\n"
"")
        self.OpenPictureButton.setObjectName("OpenPictureButton")
        self.SaveButton = QtWidgets.QPushButton(self.InfoPanel)
        self.SaveButton.setGeometry(QtCore.QRect(30, 250, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.SaveButton.setFont(font)
        self.SaveButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SaveButton.setStyleSheet("background-color: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.5, fx:0.494, fy:0.506, stop:0.0852273 rgba(255, 255, 255, 255), stop:0.892045 rgba(0, 0, 0, 227));\n"
"color: rgb(0, 0, 0);\n"
"")
        self.SaveButton.setDefault(False)
        self.SaveButton.setFlat(False)
        self.SaveButton.setObjectName("SaveButton")
        UiBaseWindow.setCentralWidget(self.UiWidget)
        self.menubar = QtWidgets.QMenuBar(UiBaseWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1360, 26))
        self.menubar.setObjectName("menubar")
        UiBaseWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(UiBaseWindow)
        self.statusbar.setObjectName("statusbar")
        UiBaseWindow.setStatusBar(self.statusbar)

        self.retranslateUi(UiBaseWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(UiBaseWindow)

    def retranslateUi(self, UiBaseWindow):
        _translate = QtCore.QCoreApplication.translate
        UiBaseWindow.setWindowTitle(_translate("UiBaseWindow", "MainWindow"))
        self.OpenVedioButton.setText(_translate("UiBaseWindow", "Open\n"
"Vedio"))
        self.NextButton.setText(_translate("UiBaseWindow", "Next"))
        self.ClassComboBox.setItemText(0, _translate("UiBaseWindow", "Nerve"))
        self.Classlabel.setText(_translate("UiBaseWindow", "Object Class"))
        self.CloseFileButton.setText(_translate("UiBaseWindow", "Close"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.InfoTab), _translate("UiBaseWindow", "Infomations"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ListTab), _translate("UiBaseWindow", "SaveList"))
        self.Sizelabel.setText(_translate("UiBaseWindow", "Image Size"))
        self.SizeComboBox.setItemText(0, _translate("UiBaseWindow", "480x480"))
        self.PrevButton.setText(_translate("UiBaseWindow", "Prev"))
        self.OpenPictureButton.setText(_translate("UiBaseWindow", "Open\n"
"Picture"))
        self.SaveButton.setText(_translate("UiBaseWindow", "Save"))

