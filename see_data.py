import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from replaceformat import *
import cv2
import matplotlib.patches as patches
from matplotlib.patches import Ellipse
import matplotlib.transforms as transforms
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--datapath", help="path to the .txt file created using 'traintest_split.py' script")
args = parser.parse_args()
print(args.datapath)
files = open(args.datapath)
first = 1
for f in files:
    name = replacetxt(f)
    name = name.replace("\n","")
    file = open(name)
    print(file)
    first = 1
    for line in file:
        print(name)
        
        itemend = line.find(" ")
        path = line[0:itemend]
        
        remain = line[itemend+1:]
        #print(remain)
        itemend = remain.find(" ")
        centerx = int(float(remain[0:itemend])*1000)
        
        remain = remain[itemend+1:]
        
        itemend = remain.find(" ")
        
        centery = int(float(remain[0:itemend])*1000)
        #height= line[-1:3]
        remain = remain[itemend+1:]
        itemend = remain.find(" ")
        width = int(float(remain[0:itemend])*1000)
        remain = remain[itemend+1:]
        itemend = remain.find(" ")
        height = int(float(remain[0:itemend])*1000)
        #print("width :"+ str(width))
        #print("height :"+ str(height))
        #print("line :"+ line)
        #print("x :"+ str(centerx))
        #print("y :" +str(centery))
        
        #print(centery)
        #centery = 
        #circle1 = patches.Rect(xy=(int(centerx),int(centery)),width=int(width),height=int(height))
        rect = patches.Rectangle((int(centerx)-int(width)/2, int(centery)-int(height)/2), int(width), int(height), linewidth=3, edgecolor='r', facecolor='none')
        f = f.replace("\n","")
        if first == 1:
            im = np.array(Image.open(f), dtype=np.uint8)
            im = cv2.resize(im, dsize=(1000, 1000), interpolation=cv2.INTER_CUBIC)
            first = 0
            fig, ax = plt.subplots()
            
        
        ax.add_patch(rect)
        
        ax.imshow(im)
    plt.show()
