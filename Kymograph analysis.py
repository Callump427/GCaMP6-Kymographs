import sys
import easygui as eg
import cv2
import img as img
from mrc import imread
import pandas as pd
from pip._internal.cli.cmdoptions import src
from scipy import ndimage
from skimage import data, io, filters, img_as_float, img_as_ubyte, exposure, morphology, color, measure, feature
import matplotlib.pyplot as plt
import numpy as np
from skimage.filters import sobel
from scipy import ndimage
from skimage.feature import canny
from scipy.ndimage import distance_transform_edt
import argparse
import os
from skimage.feature import peak_local_max
from skimage.morphology import watershed
from skimage.segmentation import clear_border
import glob
import re
import imutils
import cmapy
from sklearn.cluster import KMeans

input_files = 'C:/Users/cp634/PycharmProjects/learningpython/Kymographs/'
image_file_list =os.listdir(input_files)
# print(im9age_file_list)
os.chdir(input_files)
fig= plt.figure(figsize=(12,8))
for file in image_file_list:
   image =plt.imread(file)
   plt.imshow(image,cmap="magma")
   plt.xlabel("Distance (Pixels)")
   plt.ylabel("Time (Frames)")
   plt.colorbar()
   plt.savefig("kymograph_final.pdf")
   plt.savefig("kymograph_final.png")








plt.show()




    # fig.subplots_adjust(right=0.8)
    # cbar_ax = fig.add_axes([0.85, 0.15, 0.05, 0.7])
    # fig.colorbar(im, cax=cbar_ax)

# plt.show()

# fig = plt.figure(constrained_layout =True)
# ax1 = fig.add_subplot(2,2,1)
# ax1.title.set_text('Mother Cell')
# ax1.imshow(mother_colorized)
# fig.colorbar(mother_colorized, ax1=ax1[0, 0])
#
#
# ax2 = fig.add_subplot(2,2,2)
# ax2.title.set_text('Apical Cell')
# ax2.imshow(Apical_colorized)
#
# ax3 = fig.add_subplot(2,2,3)
# ax3.title.set_text('Sub Apical Cell')
# ax3.imshow(Sub_colorized)
#
# ax4 = fig.add_subplot(2,2,4)
# ax4.title.set_text('C3')
# ax4.imshow(C3_colorized)
#
#
# plt.subplots_adjust(left=0.1,
#                     bottom=0.1,
#                     right=0.5,
#                     top=0.9,
#                     wspace=0.4,
#                     hspace=0.4)
#
# plt.show()






# img_colorized = cv2.applyColorMap(image, cmapy.cmap('RdBu'))
# plt.imshow(img_colorized)
# plt.ylabel("Time (Frames)")
# plt.xlabel("Distance (Pixels)")
# plt.title("Kymograph of GCaMP flouresence Apical Cell")
# plt.colorbar()
# plt.savefig("processed_file.pdf")

