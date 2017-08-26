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
        self.VideoCap = None
        self.PicList = None
        self.CurrentFrame = None
        self.FrameIdx = 0
        self.FrameWidth = 0
        self.FrameHeight = 0
        self.Scene = MyGraphicsScene()   
        self.EffectRect = [140, 200, 0, 0]
        self.SavePath = "Data\\BP2017\\"
        self.SaveName = ""
        self.SavePose = ""
        self.MsgInfo = ""
        self.TagInfo = ""
        
    def setupUi(self,tagWindow):
        super().setupUi(tagWindow)
        self.FrameView.setScene(self.Scene)
        self.OpenVedioButton.clicked.connect(self.OpenVedio)
        self.OpenPictureButton.clicked.connect(self.OpenPicture)
        self.CloseFileButton.clicked.connect(self.CloseFile)
        self.SaveButton.clicked.connect(self.SaveCurrent)
        self.NextButton.clicked.connect(self.LoadNext)
        self.NextButton.setAutoRepeat(True)    
        self.PrevButton.clicked.connect(self.LoadPrev)
        self.PrevButton.setAutoRepeat(True)  
          
    def OpenVedio(self):
        self.CloseFile()
        fileName, _ = QFileDialog.getOpenFileName(QWidget(),
                                                    "Open Vedio",
                                                    "Data\\",
                                                    "Vedio (*.avi);;All Files (*)") 
        path,name = os.path.split(fileName)
        
        self.SaveName = name.split('_')[0]
        self.SavePose = name.split('_')[2] + "_" +name.split('_')[3]
        if self.SavePose=="BP_L":
            self.SaveName += "0"
        if self.SavePose=="BP_R":    
            self.SaveName += "1"
        if len(self.SaveName) ==3:
            self.SaveName = "0" + self.SaveName 
        self.VideoCap = cv2.VideoCapture(fileName)
        rval, self.CurrentFrame = self.VideoCap.read()
        if rval:
            self.FrameWidth = self.CurrentFrame.shape[1]
            self.FrameHeight = self.CurrentFrame.shape[0]
            self.ShowGraph()
            
            sizeStr = self.SizeComboBox.currentText()
            self.EffectRect[2], self.EffectRect[3] = map(int, sizeStr.split('x')) 
            self.Scene.EffectReg.setRect(self.EffectRect[0], self.EffectRect[1], self.EffectRect[2], self.EffectRect[3]) 
        else:
            self.MsgInfo.append("-> Open error!")
            
           
    def OpenPicture(self):
        self.CloseFile()
        self.PicList, _ = QFileDialog.getOpenFileNames(QWidget(),
                                                    "Open Picture",
                                                    "Data\\",
                                                    "Picture (*.jpg;*.bmp;*.png;*.tiff);;All Files (*)") 
        path,name = os.path.split(self.PicList[self.FrameIdx])
        self.SaveName = path.split('/')[-3].split('_')[0]
        self.SavePose = path.split('/')[-2]
        if self.SavePose=="BP_L":
            self.SaveName += "0"
        if self.SavePose=="BP_R":    
            self.SaveName += "1"
        if len(self.SaveName) ==3:
            self.SaveName = "0" + self.SaveName 
        self.CurrentFrame = cv2.imread(self.PicList[self.FrameIdx])
        self.FrameWidth = self.CurrentFrame.shape[1]
        self.FrameHeight = self.CurrentFrame.shape[0]
        self.ShowGraph()
        
        sizeStr = self.SizeComboBox.currentText()
        self.EffectRect[2], self.EffectRect[3] = map(int, sizeStr.split('x')) 
        self.Scene.EffectReg.setRect(self.EffectRect[0], self.EffectRect[1], self.EffectRect[2], self.EffectRect[3])  
        
        
    def CloseFile(self):
        if self.VideoCap:
            self.VideoCap.release()
            self.VideoCap = None
        self.PicList = None
        self.CurrentFrame = None
        self.FrameIdx = 0
        self.FrameWidth = 0
        self.FrameHeight = 0
        self.MsgInfo.clear()
        self.TagInfo.clear()
        self.Scene.pixmap.setPixmap(QtGui.QPixmap())  
        self.Scene.EffectReg.setRect(0, 0, 0, 0)
        self.Scene.roi.setRect(0, 0, 0, 0)
        self.Scene.roiCoord = [0, 0, 0, 0]
            
    def SaveCurrent(self):   
        xmin = int(self.Scene.roiCoord[0]-self.EffectRect[0])
        ymin = int(self.Scene.roiCoord[1]-self.EffectRect[1])
        xmax = int(self.Scene.roiCoord[2]+xmin)
        ymax = int(self.Scene.roiCoord[3]+ymin)
        if xmin>=0 and ymin>=0 and xmax<=self.EffectRect[2] and ymax<=self.EffectRect[3]:
            name_str = self.SaveName +("%03d" % self.FrameIdx)
            crop_img = self.CurrentFrame[self.EffectRect[1]:self.EffectRect[1]+self.EffectRect[3], self.EffectRect[0]:self.EffectRect[0]+self.EffectRect[2]]
            cv2.imwrite(self.SavePath + "JPEGImages\\" + name_str + ".jpg", crop_img)
            labelFile = PascalVocWriter("BP2017", name_str + ".jpg", (self.EffectRect[2], self.EffectRect[3], 3))
            labelFile.addBndBox(xmin, ymin, xmax, ymax, self.ClassComboBox.currentText(), self.SavePose, False)
            labelFile.save(targetFile = self.SavePath + "Annotations\\" + name_str + ".xml")          
            self.TagInfo.append(name_str) 
        else:
            self.MsgInfo.append("-> Out of the effect region!")
        
    def LoadNext(self):
        if self.VideoCap:
            rval, self.CurrentFrame = self.VideoCap.read()
            if rval:
                self.FrameIdx  += 1
                self.ShowGraph()
            else:
                self.MsgInfo.append("-> Reach the last frame in the vedio!")
        else:
            if self.FrameIdx < len(self.PicList)-1:
                self.FrameIdx += 1
                self.CurrentFrame = cv2.imread(self.PicList[self.FrameIdx])
                self.ShowGraph()
            else:
                self.MsgInfo.append("-> Reach the last picture in the list!")
                
    def LoadPrev(self):
        if self.VideoCap:
            self.MsgInfo.append("-> Doesn't support previous operation in vedio mode!") 
        else:
            if self.FrameIdx > 0:
                self.FrameIdx -= 1
                self.CurrentFrame = cv2.imread(self.PicList[self.FrameIdx])
                self.ShowGraph()
            else:
                self.MsgInfo.append("-> Reach the first picture in the list!")        

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