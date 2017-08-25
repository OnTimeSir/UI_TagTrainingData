# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 10:07:24 2017

@author: zfy
"""
import os.path
import cv2
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QFileDialog, QWidget, QGraphicsScene

from ui import Ui_UiBaseWindow
from pascal_voc_io import PascalVocWriter

class Ui_TagData(Ui_UiBaseWindow):   
    def __init__(self):
        super().__init__()
        self.Init()
        
    def Init(self):
        self.VideoCap = cv2.VideoCapture("")
        _,self.CurrentFrame = self.VideoCap.read()
        self.FrameIdx = 0
        self.FrameWidth = 0
        self.FrameHeight = 0
        self.Scene = MyGraphicsScene()   
        self.EffectRect = [140, 200, 0, 0]
        self.SavePath = "Data\\BP2017\\"
        self.SaveName = ""
        self.SaveSouse = ""
        self.ImgInfo = ""
        self.TagInfo = ""
        
    def setupUi(self,tagWindow):
        super().setupUi(tagWindow)
        self.FrameView.setScene(self.Scene)
        self.OpenFileButton.clicked.connect(self.OpenFile)
        self.CloseFileButton.clicked.connect(self.CloseFile)
        self.SaveButton.clicked.connect(self.SaveCurrent)
        self.NextButton.clicked.connect(self.LoadNext)
        self.NextButton.setAutoRepeat(True)    
          
    def OpenFile(self):
        self.CloseFile()
        VideoName, filetype = QFileDialog.getOpenFileName(QWidget(),
                                                    "Open Video ",
                                                    "Data\\",
                                                    "Video Files (*.avi);;All Files (*)") 
        _,tmp = os.path.split(VideoName)
        self.SaveName, self.SaveSouse, _ = tmp.split('_',2)
        self.VideoCap = cv2.VideoCapture(VideoName)
        rval, self.CurrentFrame = self.VideoCap.read()
        self.FrameIdx = 0
        if rval:
            self.FrameWidth = self.CurrentFrame.shape[1]
            self.FrameHeight = self.CurrentFrame.shape[0]
            self.FrameIdx  += 1
            self.ShowGraph()
            
            sizeStr = self.SizeComboBox.currentText()
            self.EffectRect[2], self.EffectRect[3] = map(int, sizeStr.split('x')) 
            self.Scene.EffectReg.setRect(self.EffectRect[0], self.EffectRect[1], self.EffectRect[2], self.EffectRect[3])           
            
    def CloseFile(self):
        if self.VideoCap:
            self.VideoCap.release()
            self.ImgInfo.clear()
            self.TagInfo.clear()
            self.Scene.pixmap.setPixmap(QtGui.QPixmap())  
            self.Scene.EffectReg.setRect(0, 0, 0, 0)
            self.Scene.roi.setRect(0, 0, 0, 0)
            self.Scene.roiCoord = [0, 0, 0, 0]
            
    def SaveCurrent(self):
        if self.VideoCap:    
            xmin = int(self.Scene.roiCoord[0]-self.EffectRect[0])
            ymin = int(self.Scene.roiCoord[1]-self.EffectRect[1])
            xmax = int(self.Scene.roiCoord[2]+xmin)
            ymax = int(self.Scene.roiCoord[3]+ymin)
            if xmin>=0 and ymin>=0 and xmax<=self.EffectRect[2] and ymax<=self.EffectRect[3]:
                name_str = self.SaveName +("%03d" % self.FrameIdx)
                crop_img = self.CurrentFrame[self.EffectRect[1]:self.EffectRect[1]+self.EffectRect[3], self.EffectRect[0]:self.EffectRect[0]+self.EffectRect[2]]
                cv2.imwrite(self.SavePath + "JPEGImages\\" + name_str + ".jpg", crop_img)
                labelFile = PascalVocWriter("BP2017", name_str + ".jpg", (self.EffectRect[2], self.EffectRect[3], 3), databaseSrc=self.SaveSouse)
                labelFile.addBndBox(xmin, ymin, xmax, ymax, self.ClassComboBox.currentText(), False)
                labelFile.save(targetFile = self.SavePath + "Annotations\\" + name_str + ".xml")          
                self.ImgInfo.append(name_str + ".jpg")
                self.TagInfo.append(name_str + ".xml")             
        
    def LoadNext(self):
        rval, self.CurrentFrame = self.VideoCap.read()
        if rval:
            self.FrameIdx  += 1
            self.ShowGraph()
        else:
            self.CloseFile()
            

    def ShowGraph(self):
            self.CurrentFrame = cv2.cvtColor(self.CurrentFrame, cv2.COLOR_BGR2RGB)
            qImg = QtGui.QImage(self.CurrentFrame.data, self.FrameWidth, self.FrameHeight, QtGui.QImage.Format_RGB888)
            self.Scene.pixmap.setPixmap(QtGui.QPixmap.fromImage(qImg))  
            self.Scene.roi.setRect(0, 0, 0, 0)
            self.Scene.roiCoord = [0, 0, 0, 0]
            
class MyGraphicsScene(QGraphicsScene):
    def __init__(self, parent=None):
        super (MyGraphicsScene, self).__init__ (parent)
        self.Init()
        
    def Init(self):
        self.pixmap = self.addPixmap(QtGui.QPixmap())
        self.roi = self.addRect(0, 0, 0, 0, QtGui.QPen(QtGui.QColor(255, 0, 0), 3, QtCore.Qt.SolidLine))
        self.roiCoord = [0, 0, 0, 0]
        
        self.EffectReg = self.addRect(0, 0, 0, 0, QtGui.QPen(QtGui.QColor(0, 0, 255), 2, QtCore.Qt.SolidLine))
    
    def mousePressEvent(self, event):
        StartPos = event.scenePos()
        self.roiCoord[0] = StartPos.x()
        self.roiCoord[1] = StartPos.y()
        if self.roiCoord[0]>=0 and self.roiCoord[1] >=0:
            self.roi.setRect(self.roiCoord[0], self.roiCoord[1], 0, 0)
            
    def mouseMoveEvent(self, event):
        Pos = event.scenePos()
        self.roiCoord[2] = Pos.x() - self.roiCoord[0]
        self.roiCoord[3] = Pos.y() - self.roiCoord[1]
        if self.roiCoord[2]>=0 and self.roiCoord[3] >=0:
            self.roi.setRect(self.roiCoord[0], self.roiCoord[1], self.roiCoord[2], self.roiCoord[3])
        
    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            Pos = event.scenePos()
            self.roiCoord[2] = Pos.x() - self.roiCoord[0]
            self.roiCoord[3] = Pos.y() - self.roiCoord[1]
            if self.roiCoord[2]>=0 and self.roiCoord[3] >=0:
                self.roi.setRect(self.roiCoord[0], self.roiCoord[1], self.roiCoord[2], self.roiCoord[3])
        if event.button() == QtCore.Qt.RightButton:
            self.roi.setRect(0, 0, 0, 0)
            
    def mouseDoubleClikEvent(self, event):
        pass
    
    def wheelEvent(self, event):
        pass
    
    def dragEnterEvent(event):
        pass
        
    def dragLeaveEvent(event):
        pass
        
    def dragMoveEvent(event):
        pass