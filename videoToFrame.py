
import cv2 
import math
import matplotlib.pyplot as plt  
# %matplotlib inline # For jupyternotbook or colab
import pandas as pd
from keras.preprocessing import image 
import numpy as np 
from keras.utils import np_utils
from skimage.transform import resize 

count = 0
videoFile = "input/mov1.mp4"
cap = cv2.VideoCapture(videoFile)
frameRate = cap.get(5) 
x=1
while(cap.isOpened()):
    frameId = cap.get(1) # number of images per second
    ret, frame = cap.read()
    if (ret != True):
        break
    if (frameId % math.floor(frameRate) == 0):
        filename ="output/frame%d.jpg" % count;count+=1
        cv2.imwrite(filename, frame) 
cap.release()
print ("Done!")
