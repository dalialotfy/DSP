from PyQt5 import QtWidgets, QtCore,QtGui,uic
from pyqtgraph import PlotWidget, plot
from mainwindow import Ui_MainWindow
import matplotlib.pyplot as plot
from random import randint
from threading import Timer
from scipy import signal
import pyqtgraph as pg
import pandas as pd
import numpy as np 
import pathlib 
import sys  # We need sys so that we can pass argv to QApplication
import os
import csv
import pyautogui
from PIL import Image

#open requirements
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog , QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages as pdf
import random


list_files=[]
file_path=0


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__()
        #Load the UI Page
        uic.loadUi('mainwindow.ui', self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #Samplingfrequency=2*Fmax 
        self.samplingfrequency=300
        #Actions of open menulist
        self.ui.actionChannel1.triggered.connect(self.load1)
        self.ui.actionChannel2.triggered.connect(self.load2)
        self.ui.actionChannel3.triggered.connect(self.load3)
        #Colors of every channels
        self.pen1 = pg.mkPen(color=(255, 0, 0))
        self.pen2 = pg.mkPen(color=(100, 100, 100))
        self.pen3 = pg.mkPen(color=(150, 200, 25))

        #Timers
        self.timer1 = QtCore.QTimer()
        self.timer2 = QtCore.QTimer()
        self.timer3 = QtCore.QTimer()
        #pause&resume buttons
        #ch_1
        self.ui.pushButton_9.clicked.connect(self.resume_1)
        self.ui.pushButton_10.clicked.connect(self.pause_1)
        #ch_2
        self.ui.pushButton_14.clicked.connect(self.resume_2)
        self.ui.pushButton_16.clicked.connect(self.pause_2)
        #ch_3
        self.ui.pushButton_20.clicked.connect(self.resume_3)
        self.ui.pushButton_22.clicked.connect(self.pause_3)

        #Activate Open Push Button
        self.ui.pushButton_2.clicked.connect(lambda : self.on_click())
        #Actions for zooming in:
        self.ui.pushButton_8.clicked.connect(lambda: self.zoomin1())
        self.ui.pushButton_11.clicked.connect(lambda: self.zoomin2())
        self.ui.pushButton_17.clicked.connect(lambda: self.zoomin3())
        #Actions for zooming out:
        self.ui.pushButton_7.clicked.connect(lambda: self.zoomout1())
        self.ui.pushButton_15.clicked.connect(lambda: self.zoomout2())
        self.ui.pushButton_21.clicked.connect(lambda: self.zoomout3())
        #Actions for spectrograms
        self.ui.pushButton.clicked.connect(lambda: self.spectro1())
        self.ui.pushButton_23.clicked.connect(lambda: self.spectro2())
        self.ui.pushButton_24.clicked.connect(lambda: self.spectro3())
        #Action for Scrolling:
        self.ui.pushButton_5.clicked.connect(lambda: self.scroll_right1())
        self.ui.pushButton_12.clicked.connect(lambda: self.scroll_right2())
        self.ui.pushButton_18.clicked.connect(lambda: self.scroll_right3())
        self.ui.pushButton_6.clicked.connect(lambda: self.scroll_left1())
        self.ui.pushButton_13.clicked.connect(lambda: self.scroll_left2())
        self.ui.pushButton_19.clicked.connect(lambda: self.scroll_left3())
        #Action for save:
        self.ui.actionSave.triggered.connect(self.save_pdf)
        self.ui.pushButton_4.clicked.connect(self.save_as_pdf)
        #Action for save as
        self.ui.actionSave_As.triggered.connect(self.save_as_pdf)
        self.ui.Channel1.setBackground('w')
        self.ui.Channel2.setBackground('w')
        self.ui.Channel3.setBackground('w')
      
    @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')
        self.openFileNameDialog()
        self.openFileNameDialog()
        self.openFileNameDialog()
        fname=list_files[0]
        if(fname[0]!=''):
            self.read_data1(fname) 
        else:
            pass
        fname=list_files[1]
        if(fname[0]!=''):
            self.read_data2(fname) 
        else:
            pass
        fname=list_files[2]
        if(fname[0]!=''):
            self.read_data3(fname) 
        else:
            pass 

    def openFileNameDialog(self):
        options =  QtWidgets.QFileDialog.Options()
        files=QtWidgets.QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "",
                        "(*.csv) ", options=options)
        if files:
            list_files.append(files)
            print(files)
            print(list_files)


       
    #Loading different formatted files 
    def load1(self):
        options =  QtWidgets.QFileDialog.Options()
        fname = QtWidgets.QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "",
                        "(*.csv) ", options=options)

        if(fname[0]!=''):
            self.read_data1(fname) 
        else:
            pass 
    def load2(self):
        options =  QtWidgets.QFileDialog.Options()
        fname = QtWidgets.QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "",
                        "(*.csv)", options=options) 
        if(fname[0]!=''):
            self.read_data2(fname) 
        else:
            pass 
    def load3(self):
        options =  QtWidgets.QFileDialog.Options()
        fname = QtWidgets.QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "",
                        "(*.csv) ", options=options) 
        if(fname[0]!=''):
            self.read_data3(fname) 
        else:
            pass
        
    #Reading data from files
    def read_data1(self,fname):
        path = fname[0]
        if fname[1] == "(*.csv)":
           self.data1 = np.genfromtxt(path, delimiter = ' ')
           self.x1= self.data1[: , 0]
           self.y1 =self.data1[: , 1] 
           self.x1= list(self.x1[:])
           self.y1= list(self.y1[:])
           self.channel1(self.data1)
        #self.spectro1(self.data1)
    def read_data2(self,fname):     
        path = fname[0]
        if fname[1] == "(*.csv)":
           self.data2 = np.genfromtxt(path, delimiter = ' ')
           self.x2= self.data2[: , 0]
           self.y2 =self.data2[: , 1] 
           self.x2= list(self.x2[:])
           self.y2= list(self.y2[:])
           self.channel2(self.data2)                        
    def read_data3(self,fname):
        path = fname[0]
        if fname[1] == "(*.csv)":
           self.data3 = np.genfromtxt(path, delimiter = ' ')
           self.x3= self.data3[: , 0]
           self.y3 =self.data3[: , 1] 
           self.x3= list(self.x3[:])
           self.y3= list(self.y3[:])
           self.channel3(self.data3)

    #Updating plots and repeating signals 
    def update_plot_data1(self,data_line,data):
        x = self.x1[:self.idx1]
        y = self.y1[:self.idx1]  
        self.idx1 +=10
        if self.idx1 > len(self.x1) :
            self.idx1 = 0 
        if  self.x1[self.idx1] >0.5:
            self.ui.Channel1.setLimits(xMin =min(x , default=0), xMax=max(x, default=0))
        self.ui.Channel1.plotItem.setXRange(max(x,default=0)-0.5 , max(x,default=0))
        self.data_line1.setData(x, y)
    def update_plot_data2(self,data_line,data):
        x = self.x2[:self.idx2]
        y = self.y2[:self.idx2]  
        self.idx2 +=10
        if self.idx2 > len(self.x2) :
            self.idx2 = 0 
        if  self.x2[self.idx2] >0.5:
            self.ui.Channel2.setLimits(xMin =min(x , default=0), xMax=max(x, default=0)) 
        self.ui.Channel2.plotItem.setXRange(max(x,default=0)-0.5 , max(x,default=0))
        self.data_line2.setData(x, y)
    def update_plot_data3(self,data_line,data):
        x = self.x3[:self.idx3]
        y = self.y3[:self.idx3]  
        self.idx3 +=10
        if self.idx3 > len(self.x3) :
            self.idx3 = 0 
        if  self.x3[self.idx3] >0.5:
            self.ui.Channel3.setLimits(xMin =min(x , default=0), xMax=max(x, default=0)) 
        self.ui.Channel3.plotItem.setXRange(max(x,default=0)-0.5 , max(x,default=0))
        self.data_line3.setData(x, y)
    #Displaying signals 
    def channel1 (self,data):
        
        self.data_line1 =self.ui.Channel1.plot( self.x1,self.y1,pen=self.pen1)
        self.ui.Channel1.plotItem.setLimits(xMin =0, xMax=12 , yMin =-0.6, yMax=0.6)
        self.idx1=0
        self.ui.Channel1.plotItem.getViewBox().setAutoPan(x=True,y=True)
        self.timer1.setInterval(20)
        self.timer1.timeout.connect(lambda:self.update_plot_data1(self.data_line1,data))
        self.timer1.start()
        self.ui.Channel1.show()
        self.ui.Channel1.setXRange(0,0.002*len(data))
    def channel2 (self,data):
     
        self.data_line2 =self.ui.Channel2.plot(self.x2,self.y2,pen=self.pen2)
        self.ui.Channel2.plotItem.setLimits(xMin =0, xMax=12 , yMin =-0.6, yMax=0.6)
        self.idx2=0
        self.ui.Channel2.plotItem.getViewBox().setAutoPan(x=True,y=True)
        self.timer2.setInterval(50)
        self.timer2.timeout.connect(lambda:self.update_plot_data2(self.data_line2,data))
        self.timer2.start()
        self.ui.Channel2.show()
        self.ui.Channel2.setXRange(0,0.002*len(data))
    def channel3 (self,data):
       
        self.data_line3 =self.ui.Channel3.plot( self.x3,self.y3,pen=self.pen3)
        self.ui.Channel3.plotItem.setLimits(xMin =0, xMax=12 , yMin =-0.6, yMax=0.6)
        self.idx3=0
        self.ui.Channel3.plotItem.getViewBox().setAutoPan(x=True,y=True)
        self.timer3.setInterval(50)
        self.timer3.timeout.connect(lambda:self.update_plot_data3(self.data_line3,data))
        self.timer3.start()
        self.ui.Channel3.show()
        self.ui.Channel3.setXRange(0,0.002*len(data))  

    #resume&pause
    #ch_1
    def resume_1(self):
        self.timer1.start()
        self.ui.pushButton_9.setEnabled(False)
        self.ui.pushButton_10.setEnabled(True)
    def pause_1(self):
        self.timer1.stop()
        self.ui.pushButton_10.setEnabled(False)
        self.ui.pushButton_9.setEnabled(True)
    #ch_2
    def resume_2(self):
        self.timer2.start()
        self.ui.pushButton_14.setEnabled(False)
        self.ui.pushButton_16.setEnabled(True)
    def pause_2(self):
        self.timer2.stop()
        self.ui.pushButton_16.setEnabled(False)
        self.ui.pushButton_14.setEnabled(True)
    #ch_3
    def resume_3(self):
        self.timer3.start()
        self.ui.pushButton_20.setEnabled(False)
        self.ui.pushButton_22.setEnabled(True)
    def pause_3(self):
        self.timer3.stop()              
        self.ui.pushButton_22.setEnabled(False)
        self.ui.pushButton_20.setEnabled(True)

    #Signal Power density spectogram 
    def spectro1(self,*arg):
        SP1 = self.data1.flatten()
        sepowerSpectrum, freqenciesFound, time, imageAxis = plot.specgram(SP1, NFFT=None, Fs=self.samplingfrequency, Fc=None)
        plot.xlabel('Time')
        plot.ylabel('Frequency')
        plot.show()
        plot.savefig('Channel1.png', dpi=300, bbox_inches='tight')
       
    def spectro2(self,*arg):
        SP2 = self.data2.flatten()
        sepowerSpectrum, freqenciesFound, time, imageAxis = plot.specgram(SP2, NFFT=None, Fs=self.samplingfrequency, Fc=None)
        plot.xlabel('Time')
        plot.ylabel('Frequency')
        plot.show()
        plot.savefig('Channel2.png', dpi=300, bbox_inches='tight')

    def spectro3(self,*arg):
        SP3= self.data3.flatten()
        sepowerSpectrum, freqenciesFound, time, imageAxis = plot.specgram(SP3, NFFT=None, Fs=self.samplingfrequency, Fc=None)
        plot.xlabel('Time')
        plot.ylabel('Frequency')
        plot.show()
        plot.savefig('Channel3.png', dpi=300, bbox_inches='tight')
        

 #Zooming in and out 
    def zoomin1 (self):
     self.ui.Channel1.plotItem.getViewBox().scaleBy(y=0.9 ,x=0.9)
    def zoomin2 (self):
     self.ui.Channel2.plotItem.getViewBox().scaleBy(y=0.9 ,x=0.9)
    def zoomin3 (self):
     self.ui.Channel3.plotItem.getViewBox().scaleBy(y=0.9 ,x=0.9)
    def zoomout1 (self):
       self.ui.Channel1.plotItem.getViewBox().scaleBy(y=1/0.9 ,x=1/0.9)
    def zoomout2 (self):
       self.ui.Channel2.plotItem.getViewBox().scaleBy(y=1/0.9 ,x=1/0.9)
    def zoomout3 (self):
       self.ui.Channel3.plotItem.getViewBox().scaleBy(y=1/0.9 ,x=1/0.9)

  #Scrolling Left,right
    def scroll_right1(self):
        self.ui.Channel1.plotItem.getViewBox().translateBy(x=-0.1,y=0)

    def scroll_right2(self):
        self.ui.Channel2.plotItem.getViewBox().translateBy(x=-0.1,y=0)
    def scroll_right3(self):
        self.ui.Channel3.plotItem.getViewBox().translateBy(x=-0.1,y=0)

    def scroll_left1(self):
        self.ui.Channel1.plotItem.getViewBox().translateBy(x=0.1,y=0)

    def scroll_left2(self):
        self.ui.Channel2.plotItem.getViewBox().translateBy(x=0.1,y=0)

    def scroll_left3(self): 
        self.ui.Channel3.plotItem.getViewBox().translateBy(x=0.1,y=0)


    #save plots as pdf

    def save_pdf (self):
       

        pdf_name=random.random()
        with pdf ("{}.pdf".format(pdf_name))as image:    
                #save channel 1 plot
                fig, (ax1,ax2) = plt.subplots(nrows=2)
                x1=self.x1
                y1=self.y1
                plt.title('Channel1')
                ax1.plot(x1,y1,color=['#ff0000','#646464','#96c819'][0], lw=0.5)    
                Fs=100
                SP1 = self.data1.flatten()
                Pxx, freqs, bins, im = ax2.specgram(SP1,  Fs=Fs)
                image.savefig(fig,bbox_inches="tight", dpi=300)
                plt.clf()
                #save channel 2 plot
                fig, (ax3,ax4) = plt.subplots(nrows=2)
                x2=self.x2
                y2=self.y2
                plt.title('Channel2')
                ax3.plot(x2,y2,color=['#ff0000','#646464','#96c819'][0], lw=0.5)               
                Fs=100
                SP2 = self.data2.flatten()
                Pxx, freqs, bins, im = ax4.specgram(SP2, Fs=Fs)
                image.savefig(fig,bbox_inches="tight", dpi=300)
                plt.clf()
                #save channel 3 plot
                fig, (ax5,ax6) = plt.subplots(nrows=2)
                x3=self.x3
                y3=self.y3
                plt.title('Channel3')
                ax5.plot(x3,y3,color=['#ff0000','#646464','#96c819'][0], lw=0.5)               
                Fs=100
                SP3 = self.data3.flatten()
                Pxx, freqs, bins, im = ax6.specgram(SP3,  Fs=Fs)
                image.savefig(fig,bbox_inches="tight", dpi=300)
                plt.clf()
               
                  

    def save_as_pdf(self):
            file_path = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
            print(file_path)

            with pdf ("{}\plots.pdf".format(file_path))as image:
                fig=plt.figure()
                plt.plot(self.x1,self.y1,color=['#ff0000','#646464','#96c819'][0], lw=0.5)
                plt.title("Channel 1")   
                plt.xlabel('Time')
                plt.ylabel('Amplitude')   
                image.savefig(fig,bbox_inches="tight", dpi=300)
                plt.clf()
                #save channel 1 spectrogram
                Fs=100
                fig, (ax2) = plt.subplots(nrows=1)
                SP1 = self.data1.flatten()
                Pxx, freqs, bins, im = ax2.specgram(SP1, Fs=Fs)
                plt.title("Channel 1 Spectrogram") 
                plt.xlabel('Time')
                plt.ylabel('Frequency')    
                image.savefig(fig,bbox_inches="tight", dpi=300)
                plt.clf()
             #save channel 2 plot
               #save channel 2 plot
                len_data2=len(self.data2)
                print(len_data2)
                x2=np.arange(0, len_data2,1).tolist()
                y2=self.data2
                plt.plot(x2,y2,color=['#ff0000','#646464','#96c819'][1], lw=0.5)
                plt.title("Channel 2") 
                plt.xlabel('Time')
                plt.ylabel('Amplitude')    
                image.savefig(fig,bbox_inches="tight", dpi=300)
                plt.clf()
                #save channel 2 spectrogram
                Fs=4
                fig, (ax2) = plt.subplots(nrows=1)
                Pxx, freqs, bins, im = ax2.specgram(y2, NFFT=NFFT, Fs=Fs, noverlap=900)
                plt.title("Channel 2 Spectrogram") 
                plt.xlabel('Time')
                plt.ylabel('Frequency')    
                image.savefig(fig,bbox_inches="tight", dpi=300)
                plt.clf()
                #save channel 3 plot
                len_data3=len(self.data3)
                print(len_data3)
                x3=np.arange(0, len_data3,1).tolist()
                y3=self.data3
                plt.plot(x3,y3,color=['#ff0000','#646464','#96c819'][2], lw=0.5)
                plt.title("Channel 3") 
                plt.xlabel('Time')
                plt.ylabel('Amplitude')    
                image.savefig(fig,bbox_inches="tight", dpi=300)
                plt.clf()
                #save channel 3 spectrogram
                Fs=100
                fig, (ax2) = plt.subplots(nrows=1)
                Pxx, freqs, bins, im = ax2.specgram(y3,Fs=Fs)
                plt.title("Channel 3 Spectrogram") 
                plt.xlabel('Time')
                plt.ylabel('Frequency')    
                image.savefig(fig,bbox_inches="tight", dpi=300)
                plt.clf()
           
                                            

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':      
 main()