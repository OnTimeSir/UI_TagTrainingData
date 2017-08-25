# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 15:59:45 2017

@author: zfy
"""

import sys,PyQt5,TagData

app = 0
app = PyQt5.QtWidgets.QApplication(sys.argv)
tagWindow = PyQt5.QtWidgets.QMainWindow()

tagTrainingData = TagData.Ui_TagData()
tagTrainingData.setupUi(tagWindow)

tagWindow.show()
sys.exit(app.exec_())