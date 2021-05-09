from PIL import Image
import cv2
import numpy as np
import matplotlib.pyplot as plt
import logging


# Create and configure logger
logging.basicConfig(level=logging.DEBUG,
                    filename="app.log",
                    format='%(lineno)s - %(levelname)s - %(message)s',
                    filemode='w')

# Creating an object
logger = logging.getLogger()

class image:
    def __init__(self,path):
            self.img =cv2.imread(path,0) 
            #self.height,self.width=self.img.shape
            # perform the 2-D fast Fourier transform on the image data
            self.DFT = np.fft.fft2(self.img)
            # compute the magnitudes (absolute values) of the complex numbers
            self.magnitude = np.abs(self.DFT)
            #phase 
            self.phase = np.angle(self.DFT)
            #real 
            self.real = np.real(self.DFT)
            #imaginary 
            self.imaginary= np.imag(self.DFT)
            # compute the common logarithm of each value to reduce the dynamic range
            self.mag_spectrum = np.log10(self.magnitude)
            #uniform magnitude
            self.uniform_magnitude = np.where(self.mag_spectrum, 1, self.mag_spectrum)
            #uniform phase
            #self.uniform_phase = np.where(self.phase, 0, self.phase)
            self.shape= self.img.shape
            self.uniform_magnitude = np.ones(self.shape)
            self.uniform_phase = np.zeros(self.shape)
        

    def image_mixer(self, imageToBeMixed: 'ImageModel', magnitudeOrRealRatio: float, phaesOrImaginaryRatio: float, mode):

        """a function that takes ImageModel object mag ratio, phase ration and return the magnitude of ifft of the mix return type ---> 2D numpy array
        """
        self.Modes={'magnitudeAndphase':[self.magnitude,imageToBeMixed.magnitude,self.phase,imageToBeMixed.phase],'realAndimaginary':[self.real,imageToBeMixed.real,self.imaginary,imageToBeMixed.imaginary],'uniformmagnitudeAnduniformphase':[self.uniform_magnitude , imageToBeMixed.uniform_magnitude ,self.uniform_phase,imageToBeMixed.uniform_phase],'magnitudeAnduniformphase':[self.magnitude,imageToBeMixed.magnitude,self.uniform_phase,imageToBeMixed.uniform_phase],'uniformmagnitudeAndphase':[self.uniform_magnitude, imageToBeMixed.uniform_magnitude,self.phase,imageToBeMixed.phase],'phaseAndmagnitude':[self.phase,imageToBeMixed.phase,self.magnitude,imageToBeMixed.magnitude],'imaginaryAndreal':[self.imaginary,imageToBeMixed.imaginary,self.real,imageToBeMixed.real],'uniformphaseAndmagnitude':[self.uniform_phase,imageToBeMixed.uniform_phase,self.magnitude,imageToBeMixed.magnitude],'phaseAnduniformmagnitude':[self.phase,imageToBeMixed.phase,self.uniform_magnitude,imageToBeMixed.uniform_magnitude],'uniformphaseAnduniformmagnitude':[self.uniform_phase,imageToBeMixed.uniform_phase,self.uniform_magnitude,imageToBeMixed.uniform_magnitude]}
        self.mag_phase_list=['magnitudeAndphase','uniformmagnitudeAnduniformphase','magnitudeAnduniformphase','uniformmagnitudeAndphase']
        self.phase_mag_list=['phaseAndmagnitude','uniformphaseAnduniformmagnitude','phaseAnduniformmagnitude','uniformphaseAndmagnitude']
        ratio_1 = magnitudeOrRealRatio
        ratio_2= phaesOrImaginaryRatio
        mixInverse = None
        if mode in self.Modes:
            mode_data=self.Modes.get(mode)
            mode_data1_mixing= (ratio_1*mode_data[0]+((1-ratio_1)*mode_data[1]))
            mode_data2_mixing= (ratio_2*mode_data[3]+((1-ratio_2)*mode_data[2]))
            if (mode in self.mag_phase_list ):
                combined = np.multiply(mode_data1_mixing, np.exp(1j * mode_data2_mixing))
                logger.info("Mixing Magnitude and Phase")
            elif (mode in self.phase_mag_list):
                combined = np.multiply(mode_data2_mixing, np.exp(1j * mode_data1_mixing))
            elif  mode =='realAndimaginary':
                combined =  mode_data1_mixing + mode_data2_mixing * 1j
                logger.info("Mixing Real And Imaginary")
            elif mode == 'imaginaryAndreal':
                 combined =  mode_data2_mixing + mode_data1_mixing * 1j
            mixInverse = np.real(np.fft.ifft2(combined))  
        return(mixInverse)
       
            
     

        
  