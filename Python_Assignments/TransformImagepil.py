# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 16:44:51 2021

@author: dalia
"""

#Invert colors, double image size, flip on vertical axis

#Using PIL to invert the colors of an image
from PIL import Image
import PIL.ImageOps    

img = Image.open(r"C:/Users/dalia/OneDrive/Desktop/python/Assignment4/apple.jpg")
width, height = img.size

def invertImg(img):
    #Invert colors of the image
    invImg = PIL.ImageOps.invert(img)
    return invImg

def doubleSize(img):
    doubleImg = img.resize((width*2, height*2))
    return doubleImg

def flipImg(img):
    flipImg = img.transpose(PIL.Image.FLIP_LEFT_RIGHT)
    return flipImg

def main():
    invImg = invertImg(img)
    invImg.save("appleINV.jpg")
    dblImg = doubleSize(invImg)
    dblImg.save("appleDBL.jpg")
    flpImg = flipImg(dblImg)
    flpImg.save("appleFinal.jpg")
    

main()
#Save as new image
#invImage.save('apple3.png')
