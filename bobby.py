import cv2
import os
from os import listdir
import numpy as np
folderdir="/Users/anikethluchmapurkar/Desktop/hackathons/2023-hacktj/asl_alphabet_test/"
count=1

for images in os.listdir(folderdir):
    print (count)
# Load an ASLsign image
    if images!=".DS_Store":
        print(folderdir+images)
        img = cv2.imread(folderdir+images, cv2.IMREAD_GRAYSCALE)

    # Apply Gaussian filter to reduce noise

        img = cv2.GaussianBlur(img, (5, 5), 0)



    # Detect edges using Canny edge detection

        edges = cv2.Canny(img, 50, 150)



        # Display the edge map


        cv2.imwrite(folderdir+images,edges)
        count+=1