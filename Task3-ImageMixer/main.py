from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog , QPushButton,QMessageBox
from PyQt5 import QtWidgets, QtCore,QtGui,uic,QtMultimedia
from mainwindow import Ui_MainWindow
from ImageClass import image  #Importing class from another python file 
import matplotlib.pyplot as plot
from scipy.fftpack import fft,rfft
import pandas as pd
import pyqtgraph as pg
import numpy as np 
import logging
import sys  # We need sys so that we can pass argv to QApplication
import cv2
import os

# Create and configure logger
logging.basicConfig(level=logging.DEBUG,
                    filename="app.log",
                    format='%(lineno)s - %(levelname)s - %(message)s',
                    filemode='w')

# Creating an object
logger = logging.getLogger()

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__()
    #======================================================= UI Actions ===================================================================
 
        #Load the UI Page
        self.MainWindow = MainWindow
        uic.loadUi('mainwindow.ui', self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Load Buttons
        self.loadButtons = [self.ui.Open_Image_1,self.ui.Open_Image_2]
        # Displaying areas
        self.Imagedisplay=[self.ui.Image1_Area,self.ui.Image2_Area]
        self.image_components_display = [self.ui.Image_1_Components_Area,self.ui.Image_2_Components_Area]
        self.images_output_display=[self.ui.Output1_Area,self.ui.Output2_Area]
        self.ImageViewAreas=[self.ui.Image1_Area,self.ui.Image2_Area,self.ui.Image_2_Components_Area,self.ui.Image_1_Components_Area,self.ui.Output1_Area,self.ui.Output2_Area]
        # Images list
        self.images=[...,...] 
        # Combo Lists
        self.image_components = [self.ui.Image_1_Components,self.ui.Image_2_Components] 
         # Load Buttons and Combo Connections   
        for i in range(2):
           self.images_combo_counter(i)
           self.loading_counter(i)
        # Images dimensions
        self.size = [..., ...]
         # Image Options combos list 
        self.image_options=[self.ui.Input1,self.ui.Input2]
        #Mixer
        self.component_options=[self.ui.Component_Input1,self.ui.Component_Input2] 
        #for Mixer_Inputs in self.component_options:
        self.component_options[0].activated.connect(lambda: self.Selected_images_options()) 
        self.component_options[1].activated.connect(lambda: self. update_mixer_data())
        self.Mixer_Components=[] 
        #sliders
        self.Mixer_Sliders=[self.ui.Input1_Percentage,self.ui.Input2_Percentage]
        for Mixer_Percent in self.Mixer_Sliders:
            self.min=Mixer_Percent.setMinimum(0)
            Mixer_Percent.setMaximum(100)
            Mixer_Percent.valueChanged.connect(lambda: self.update_mixer_data()) 
        #combos:
        self.Mixer_data=[self.ui.Input1,self.ui.Input2,  self.ui.Mixer_Output_Area]
        for Mixer_Inputs in self.Mixer_data:
            Mixer_Inputs.activated.connect(lambda: self.update_mixer_data()) 
        logger.info("The Application started successfully")
 #============================================== Functions of loading  and reading Images ==============================================
    def load(self,imgindex):
        logger.info("Browsing the files...")
        options =  QtWidgets.QFileDialog.Options()
        fname = QtWidgets.QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "",
                        "*.jpg;;" "*.jpeg;;" "*.png;;", options=options) 
        self.imgindex=imgindex
        if(fname[0]!=''):
            self.read_data(fname)  
        else:
            pass
    def read_data(self,fname):
        self.path = fname[0]
        self.imgName = fname[-1] 
        self.image=image(self.path)
        self.size[self.imgindex] =self.image.shape
        if (self.images==[...,...]):
            self.dispaly_image(self.image.img,self.Imagedisplay[self.imgindex])
        else :
          if (all(img == self.size[self.imgindex] for img in self.size)):
               self.dispaly_image(self.image.img,self.Imagedisplay[self.imgindex])
          else:
                self.showMessage("Warning!!", "Image sizes must be the same, please upload another image",
                                     QMessageBox.Ok, QMessageBox.Warning)
                logger.warning("Warning!!. Image sizes must be the same, please upload another image")
        self.image_components[self.imgindex].setEnabled(True)
        self.images[self.imgindex]=self.image
       #===========================================Functions of displaying Images and its components====================================================
    
    def dispaly_image(self,image_data,DisplayingArea):
        DisplayingArea.setImage(image_data.T)
        DisplayingArea.view.setRange(xRange=[0, self.size[self.imgindex][1]], yRange=[0, self.size[self.imgindex][0]],padding=0)
        DisplayingArea.show()
        logger.info(f"Added Image or its components {self.imgindex+1} from {self.path}: has loaded correctly'")  

    def input_Components(self,component_id):
        ## move the zero-frequency component to the center of the Fourier spectrum
        self.shifted_DFT = np.fft.fftshift(self.images[component_id].DFT)
        self.shifted_magnitude = 20*np.log(np.abs(self.shifted_DFT))
        self.shifted_real = 20 * np.log(np.real(self.shifted_DFT))
        self.shifted_imag=np.imag(self.shifted_DFT)
        self.shifted_imag[self.shifted_imag<=0]=10**-8
        self.shifted_imag=20*np.log(self.shifted_imag)
        self.component_options[self.imgindex].setEnabled(True)
        ## Image components options
        Image_components=["magnitude","phase","real","imaginary"]
        components_data=[self.shifted_magnitude ,self.images[component_id].phase,self.shifted_real,self.shifted_imag]
        for component_index in range(len(Image_components)):
            if (self.image_components[component_id].currentText().lower()== Image_components[component_index]):
                self.dispaly_image(components_data[component_index] ,self.image_components_display[component_id])
                logger.info(f"Viewing {Image_components[component_id]} Component Of Image")

       #=============================================== Functions of displaying Mixed_Images ===================================================
    
    def Selected_images_options(self):
        self.Mixer_options=[["magnitude","uniformmagnitude"],["phase","uniformphase"],["real"],["imaginary"]]
        self.component_options[1].clear()
        self.component_options[1].addItem("Choose component") 
        for Mixer_option in range(len(self.Mixer_options)):
            if self.ui.Component_Input1.currentText().lower() in self.Mixer_options[Mixer_option]:
                if Mixer_option %2 ==0:
                   Mixer_option= Mixer_option+1
                else:
                    Mixer_option= Mixer_option-1
                self.component_options[1].addItems(self.Mixer_options[Mixer_option])
            if self.ui.Component_Input1.currentText().lower()=="uniformphase" or self.ui.Component_Input1.currentText().lower()=="uniformmagnitude":
                self.ui.Input1_Percentage.setValue(0)
                self.ui.Input1_Percentage.setEnabled(False)
            else:
                self.ui.Input1_Percentage.setEnabled(True)

    def update_mixer_data(self):
        mixer_output=...
        self.Mixer_Components=[self.ui.Component_Input1.currentText().lower(),self.ui.Component_Input2.currentText().lower()]
        self.images_indexes=[]
        self.Mixer_sliders_Values=[]
        for mixer_data in range(2):
           self.images_indexes.append(self.image_options[mixer_data].currentIndex())
           self.Mixer_sliders_Values.append(self.Mixer_Sliders[mixer_data].value()/100.0)
        self.ui.label_slider.setText(str(self.Mixer_sliders_Values))

        try:
          if ( all(Mix_Comp != "Choose component" for Mix_Comp in  self.Mixer_Components)):
             self.mode=self.Mixer_Components[0]+'And'+self.Mixer_Components[1]
             self.ui.Mixer_Output_Area.setEnabled(True)
             if (self.component_options[1].currentText().lower()=='uniformphase' or self.component_options[1].currentText().lower()=="uniformmagnitude"):
                 self.Mixer_Sliders[1].setValue(0)
                 self.Mixer_Sliders[1].setEnabled(False)
             else:
                 self.Mixer_Sliders[1].setEnabled(True)
             self.imgindex=self.images_indexes[0]
             mixer_output = self.images[self.images_indexes[0]].image_mixer(self.images[self.images_indexes[1]],self.Mixer_sliders_Values[0],self.Mixer_sliders_Values[1],self.mode)
          if type(mixer_output) !=type(...):
             if (self.ui.Mixer_Output_Area.currentText() !='Choose Output Area'):
               self.Mixer_Output_Area=self.ui.Mixer_Output_Area.currentIndex()
               logger.info(f"Mixing{self.mode} has been done correctly")
               self.dispaly_image(mixer_output,self.images_output_display[self.Mixer_Output_Area-1])
               logger.info(f"Mixer_output{self.images_output_display[self.Mixer_Output_Area-1]} has been generated and displayed")
        except Exception as e:
            logger.error("Exception occurred", exc_info=True)

    def images_combo_counter(self,i:int):
        self.image_components[i].currentIndexChanged.connect(lambda:self.input_Components(i))  
    def loading_counter(self,i:int):
        self.loadButtons[i].clicked.connect(lambda: self.load(i))
      
    def showMessage(self, header, message, button, icon):
        msg = QMessageBox()
        msg.setWindowTitle(header)
        msg.setText(message)
        msg.setIcon(icon)
        msg.setStandardButtons(button)
        x = msg.exec_()     

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':      
 main()
