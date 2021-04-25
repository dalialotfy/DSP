from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog , QPushButton ,QMessageBox,QMainWindow
from PyQt5 import QtWidgets, QtCore,QtGui,uic,QtMultimedia
from mainwindow import Ui_MainWindow
import matplotlib.pyplot as plot
from scipy.fftpack import fft,rfft
from scipy.io import wavfile
from random import randint
import pandas as pd
import pyqtgraph as pg
import numpy as np 
import sys  
import os
import cmath 
import itertools
import operator
import wavio
import sounddevice as sd
#save state
from PyQt5.QtCore import QSettings, QPoint, QSize
QAction=QtWidgets.QAction
#generate pdf
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages as pdf
import random
#pdf variables
list_files=[]
file_path=0



class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__()
        #Load the UI Page
        uic.loadUi('mainwindow.ui', self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Main Variables
        self.spectrogram_pallette="viridis"
        self.spectrogram_gain=1
        self.samplerate=44100
        self.sample_length=0
        self.max=self.samplerate/2
        self.min=0
        self.data=np.array([])
        self.time=np.array([])
        self.IFFT=np.array([])
        self.slidersdata=np.array([])
        self.bandsdata=[]
        self.xmin=0
        self.xmax=0
        self.ymin=0
        self.ymax=0
        self.y2min=0
        self.y2max=0
#======================================================================================================================================
#======================================================= UI Actions ===================================================================
#======================================================================================================================================
    #Actions of open menulist
        self.ui.actionOpen.triggered.connect(self.load)
        self.ui.open_button.clicked.connect(lambda : self.load())
        self.ui.input_channel.setBackground('w')
        self.ui.output_channel.setBackground('w')
        self.ui.equalizer_area.setStyleSheet("background-color: white")
        self.ui.spectrogram_area.setStyleSheet("background-color: white")
        
    #Colors of every channels
        self.pen1 = pg.mkPen(color=(255, 0, 0))
        self.pen2 = pg.mkPen(color=(100, 100, 100))
    #Timers
        self.timer1 = QtCore.QTimer()
        self.timer2 = QtCore.QTimer()
    #pause&resume buttons
        self.ui.pause_button.clicked.connect(self.pause_1)
        self.ui.play_button.clicked.connect(self.resume_1)
    #Actions for zooming in:
        self.ui.zoom_in_button.clicked.connect(lambda: self.zoomin1())
    #Actions for zooming out:
        self.ui.zoom_out_button.clicked.connect(lambda: self.zoomout1())
    #Action for Scrolling:
        self.ui.scroll_left_button.clicked.connect(lambda: self.scroll_right1())
        self.ui.scroll_right_button.clicked.connect(lambda: self.scroll_left1())
        self.ui.scroll_up_button.clicked.connect(lambda: self.scroll_up1())
        self.ui.scroll_down_button.clicked.connect(lambda: self.scroll_down1())
    #spin box set speed
        self.ui.set_speed_spinBox.setSingleStep(5)
        self.ui.set_speed_spinBox.setValue(5)
        self.ui.set_speed_spinBox.setMinimum(5)
        self.ui.set_speed_spinBox.setMaximum(95)
        self.ui.set_speed_spinBox.valueChanged.connect(lambda: self.set_speed())
    #Combo Box Choose Pallete
        self.ui.choose_pallette_combobox.activated.connect(self.choose_pallete)  
    #Show / Hide
        self.ui.show_hide_checkbox.clicked.connect(self.show_hide)   
        # self.ui.show_hide_checkbox_2.clicked.connect(self.ui.spectrogram_area.show) 
    #Sliders
        self.sliders = [self.ui.gain_slider_1,self.ui.gain_slider_2,self.ui.gain_slider_3,self.ui.gain_slider_4,self.ui.gain_slider_5,self.ui.gain_slider_6,self.ui.gain_slider_7,self.ui.gain_slider_8,self.ui.gain_slider_9,self.ui.gain_slider_10]

    #Configure each sliderflat_list
        for slid in self.sliders:
            slid.setMinimum(0)
            slid.setMaximum(5)
            slid.setPageStep(1)
            slid.setValue(1)
            slid.setSingleStep(1)
            slid.setTickPosition(QtWidgets.QSlider.TicksAbove)
    #sliders    
        self.sliders[0].valueChanged.connect(lambda: self.sliderChanged(0))
        self.sliders[1].valueChanged.connect(lambda: self.sliderChanged(1))
        self.sliders[2].valueChanged.connect(lambda: self.sliderChanged(2))
        self.sliders[3].valueChanged.connect(lambda: self.sliderChanged(3))
        self.sliders[4].valueChanged.connect(lambda: self.sliderChanged(4))
        self.sliders[5].valueChanged.connect(lambda: self.sliderChanged(5))
        self.sliders[6].valueChanged.connect(lambda: self.sliderChanged(6))
        self.sliders[7].valueChanged.connect(lambda: self.sliderChanged(7))
        self.sliders[8].valueChanged.connect(lambda: self.sliderChanged(8))
        self.sliders[9].valueChanged.connect(lambda: self.sliderChanged(9))
    # Hoizontal sliders
        self.ui.set_max_frequency.valueChanged.connect(self.spectrogram_intensity_set)
        self.ui.set_min_frequency.valueChanged.connect(self.spectrogram_intensity_set)
    #Action for save pdf
        self.ui.actionSave_As.triggered.connect(self.save_as_pdf)
        self.ui.actionSave.triggered.connect(self.save_pdf)
        self.ui.save_button.clicked.connect(lambda: self.save_pdf())
    #Action new window
        self.ui.actionNew_Project.triggered.connect(self.addNewWindow)
        self.start = 50
        self.end = 50
        quit = QAction("Quit", self)
        quit.triggered.connect(self.close)   
        self.popups = []
#======================================================================================================================================
#============================================== Functions of reading and plotting signal ==============================================
#======================================================================================================================================

#load file           
    def load(self):
        options =  QtWidgets.QFileDialog.Options()
        fname = QtWidgets.QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "",
                        "(*.wav) ", options=options) 
        if(fname[0]!=''):
            self.read_data(fname)

        else:
            pass
        
#Reading data from file
    def read_data(self,fname):
        path = fname[0]
        self.samplerate,self.data = wavfile.read(path)
        self.sample_length = self.data.shape[0] 
        self.time = np.arange(self.sample_length) / self.samplerate
        self.ui.input_channel.plot(self.time,self.data,pen=self.pen1)
        self.xmin=0.0
        self.xmax=max(self.time)
        self.ymin=min(self.data)
        self.ymax=max(self.data)
        self.ui.input_channel.plotItem.getViewBox().setLimits(xMin=self.xmin, xMax=self.xmax, yMin=self.ymin, yMax=self.ymax)
        self.FFT(self.data,self.samplerate,self.sample_length)
        self.play(self.data,self.samplerate)

#play signals      
    def play(self,data,samplerate):
        sd.play(self.data, self.samplerate)

#======================================================================================================================================
#==================================================== Functions of Equalizer ==========================================================
#======================================================================================================================================
# recieve index of slider to get value and pass to gain
    def sliderChanged(self, slider):
        sliderValue = self.sliders[slider].value()
        self.gain(slider,sliderValue)
    
#get the signal data after gain
    def gain(self,slider,sliderValue):
            self.bandsdata[slider] = np.multiply(self.bands[slider], sliderValue)
            flat_list = [item for sublist in self.bandsdata for item in sublist]
            self.gaineddata=[]
            for sublist in self.bandsdata:
                for item in sublist:
                    self.gaineddata.append(item)
            self.gainedsignal=np.multiply(np.array(self.gaineddata),np.exp(1j*self.phase))
            self.slidersdata=np.copy(self.gainedsignal)
            self.ui.output_channel.removeItem(self.data_line1)
            self.inverse(self.gainedsignal)
               
# calculate FFT then call inverse           
    def FFT(self,data,samplerate,sample_length):
        self.FFT = np.fft.rfft(data)
        # Normalize
        self.fftmagnitude = abs(self.FFT)
        self.phase=np.angle(self.FFT)
        self.frequencies = np.fft.rfftfreq(len(data),1/samplerate) 
        self.min=int(self.frequencies.min())
        self.max=int(self.frequencies.max())
        self.ui.set_max_frequency.setMaximum(int(self.max))
        self.ui.set_max_frequency.setMinimum(int(self.min))
        self.ui.set_min_frequency.setMaximum(int(self.max))
        self.ui.set_min_frequency.setMinimum(int(self.min))
        self.ui.set_min_frequency.setValue(int(self.max))
        self.ui.set_max_frequency.setValue(int(self.min))
        self.bands = []  # creating Bands
        for i in range(10):
            self.bands.append(self.fftmagnitude[int(i / 10 * len(self.fftmagnitude)): int(
                min(len(self.fftmagnitude) + 1, (i + 1) / 10 * len(self.fftmagnitude)))])
        
        for i in range (10):
           self.bandsdata.append([])
        self.bandsdata=list.copy(self.bands)
        self.slidersdata=np.copy(self.FFT)
        self.inverse(self.FFT)

#apply inverse fft and plot output data               
    def inverse(self,gain_data):
        self.IFFT= np.fft.irfft(gain_data)
        # wavio.write("Output.wav", self.IFFT, self.samplerate, sampwidth=1)
        self.data_line1= self.ui.output_channel.plot(self.time,self.IFFT,pen=self.pen2)
        self.y2min=min(self.IFFT)
        self.y2max=max(self.IFFT)
        self.ui.output_channel.plotItem.getViewBox().setLimits(xMin=self.xmin, xMax=self.xmax, yMin=self.y2min, yMax=self.y2max)
        self.play(self.IFFT,self.samplerate)
        self.spectrogram_intensity_set()
        
#set the max and min freq of data  
    def spectrogram_intensity_set(self):
        self.min_slider=self.ui.set_max_frequency.value()
        self.max_slider=self.ui.set_min_frequency.value()
        if((self.min_slider!=self.min)or(self.max_slider!=self.max)):
            if((self.max_slider)>(self.min_slider)):
                self.min_updated=int(np.where(self.frequencies==self.min_slider)[0])
                self.max_updated=int(np.where(self.frequencies==self.max_slider)[0])
                self.data_ranged_freq=self.slidersdata[self.min_slider:(self.max_updated+1)]  
                self.IFFT_spectrogram= np.fft.irfft(self.data_ranged_freq)         
        else:
            self.IFFT_spectrogram=np.copy(self.IFFT)
        self.spectrogram_updated()      
    

#select color pallete
    def choose_pallete(self):
        self.ui.spectrogram_area.clear()
        palette_options=["Pallette 1","Pallette 2","Pallette 3","Pallette 4","Pallette 5"]
        palette_colors=["viridis","RdPu","magma","inferno","plasma"]
        for color_index in range(5):
            if (self.ui.choose_pallette_combobox.currentText()==palette_options[color_index]):
                self.spectrogram_pallette=palette_colors[color_index]
        self.spectrogram_updated()    


#plot spectrogram
    def spectrogram_updated(self):
        plot.clf()
        sepowerSpectrum, freqenciesFound, time, imageAxis = plot.specgram(self.IFFT_spectrogram,Fs=2400,Fc=0,cmap=self.spectrogram_pallette)
        plot.savefig('Input1.png', bbox_inches='tight')
        self.ui.spectrogram_area.setPixmap(QtGui.QPixmap('Input1.png'))
        os.remove("Input1.png")

               

#======================================================================================================================================
#=============================================== Functions of Signal Display control ==================================================
#======================================================================================================================================
    def show_hide(self):
        if self.ui.spectrogram_area.isVisible()==True:
            visible=False
        else:
            self.ui.spectrogram_area.setHidden(False)
            visible=True
        self.ui.spectrogram_area.setVisible(visible)
        
    def resume_1(self):
        self.timer1.start()
        self.timer2.start()
        self.ui.play_button.setEnabled(False)
        self.ui.pause_button.setEnabled(True)
        
    def pause_1(self):
        self.timer1.stop()
        self.timer2.stop()
        self.ui.pause_button.setEnabled(False)
        self.ui.play_button.setEnabled(True)
        
#Zooming in and out 
    def zoom (self,signal_scale):
        self.ui.input_channel.plotItem.getViewBox().scaleBy(y=signal_scale ,x=signal_scale)
        self.ui.output_channel.plotItem.getViewBox().scaleBy(y=signal_scale ,x=signal_scale)

    def zoomin1 (self):
        signal_scale=0.9
        self.zoom(signal_scale)

    def zoomout1 (self):
        signal_scale=1/0.9
        self.zoom(signal_scale)
        

#Scrolling Left,right
    def scroll(self,xt,yt):
        self.ui.input_channel.plotItem.getViewBox().translateBy(x=xt,y=yt)
        self.ui.output_channel.plotItem.getViewBox().translateBy(x=xt,y=yt)
    def scroll_right1(self):
        xt=-0.1
        yt=0
        self.scroll(xt,yt)

    def scroll_left1(self):
        xt=0.1
        yt=0
        self.scroll(xt,yt)

    def scroll_up1(self):
        xt=0
        yt=(self.ymax)/10
        self.scroll(xt,yt)

    def scroll_down1(self):
        xt=0
        yt=-30
        self.scroll(xt,yt)


#set speed of dynamic plot
    def set_speed(self):
        self.timer1.setInterval(self.ui.set_speed_spinBox.value())
        self.timer1.timeout.connect(self.update_plot_data1(self.data_line1,time,data))
        self.timer1.start()
        self.timer2.setInterval(self.ui.set_speed_spinBox.value())
        self.timer2.timeout.connect(lambda:self.update_plot_data2(self.data_line2,time,IFFT))
        self.timer2.start()

#======================================================================================================================================
#=================================================== New Window and Closing ===========================================================
#======================================================================================================================================
# new window
    def addNewWindow(self):
            new_window = MainWindow2()
            new_window.show()
            
            if self.start > 1600:
                self.start = 50
                self.end = self.end + 250
            new_window.setGeometry(self.start, self.end, 1581, 921)
            self.popups.append(new_window)
            self.start = self.start + 250
#closing  
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Quit Equalizer',
                                            "Are you sure to quit?",
                                            QMessageBox.Save | QMessageBox.Close | QMessageBox.Cancel, QMessageBox.Save)

        if reply == QMessageBox.Close:
            event.accept()

        elif reply == QMessageBox.Save:
            self.save_as_pdf()
            self.save_wav_output()
            event.accept()
        else:
            event.ignore()
#======================================================================================================================================
#=================================================== Saving Pdf and Sound file=========================================================
#======================================================================================================================================
    
    def save1(self,file_path):
        fig, ((self.ax1, self.ax2), (self.ax3, self.ax4)) = plt.subplots(2, 2, constrained_layout=True)
        fig.set_constrained_layout_pads(w_pad=4 / 72, h_pad=4 / 72, hspace=0.2,wspace=0.2)
        #input signal
        self.ax1.plot(self.time,self.data,color='#ff0000', lw=0.5)
        self.ax1.set_xlabel('time')
        self.ax1.set_ylabel('amplitude')
        self.ax1.set_title('input signal')
        #input spectrogram
        sepowerSpectrum, freqenciesFound, time, imageAxis = self.ax2.specgram(self.data,Fs=2400,Fc=0,cmap=self.spectrogram_pallette)
        self.ax2.set_xlabel('time')
        self.ax2.set_ylabel('frequency')
        self.ax2.set_title('input spectrogram')
        #output signal
        self.ax3.plot(self.time,self.IFFT,color='#646464', lw=0.5)
        self.ax3.set_xlabel('time')
        self.ax3.set_ylabel('amplitude')
        self.ax3.set_title('output signal')
        #output spectrogram
        sepowerSpectrum, freqenciesFound, time, imageAxis = self.ax4.specgram(self.IFFT_spectrogram,Fs=2400,Fc=0,cmap=self.spectrogram_pallette)
        self.ax4.set_xlabel('time')
        self.ax4.set_ylabel('frequency')
        self.ax4.set_title('output spectrogram')

        if file_path:
            fig.savefig("{}\Report.pdf".format(file_path))
        else:
            fig.savefig("Report.pdf")        
               

    def save_pdf (self):
        file_path=[]
        self.save1(file_path)
        

    def save_as_pdf(self):
        file_path = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.save1(file_path)
        
        

    def save_wav_output(self):
        wavio.write("Output.wav", self.IFFT, self.samplerate, sampwidth=1)

                 
#======================================================================================================================================
#===================================================== New Window Class================================================================
#======================================================================================================================================           
class MainWindow2(MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__()
        


def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':      
 main()
