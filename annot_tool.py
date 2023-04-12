from replaceformat import *
from matplotlib.backend_bases import MouseButton
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches
from glob import glob
from xml.etree import ElementTree as ET
import cv2
import os

import time
crop =-1
import sys
rects = []
im = None
counter = 0
t = np.arange(0.0, 1.0, 0.01)
s = np.sin(2 * np.pi * t)
filename = ""
#ax.plot(t, s)
firstcoord = [0,0]
secondcoord = [0,0]
first = True
import os
coordlist = []
from PIL import Image
import numpy as np
new = False
coords = {"images":[]}
line = {}
filename = ""

def fast_scandir(dirname):
    subfolders= [f.path for f in os.scandir(dirname) if f.is_dir()]
    for dirname in list(subfolders):
        subfolders.extend(fast_scandir(dirname))
    return subfolders
names = fast_scandir("images/")




def on_move(event):
    global secondcoord,firstcoord,new
    if event.inaxes:
        if new == True:
            if firstcoord != [0,0]:
                secondcoord[0] = event.xdata
                secondcoord[1] = event.ydata
                rect = patches.Rectangle((firstcoord[0], firstcoord[1]), secondcoord[0]-firstcoord[0], secondcoord[1]-firstcoord[1], linewidth=3, edgecolor='r', facecolor='none')
                rect2 = [rect, "new"]
                rects.append(rect2)
                
                    
                
                ax.add_patch(rect)
                
                plt.pause(0.0001)
                try:
                    rect.remove()
                except:
                    pass
    #plt.pause(0.0001)
                
nextimage = False
def on_close(event):
    global first,filename
    first = True
def on_key(event):
    global crop,nextimage
    if event.key == 'q':
        
        sys.exit()
    if event.key == 'c':
        crop = -crop
    if event.key == 'n':
        nextimage = True
        os.remove(filename)
def on_click(event):
    
    global counter,crop,new,im,first,nextimage,line,filename,coords,coordlist,firstcoord,secondcoord
    
    
    if event.button is MouseButton.LEFT:
        if first == True:
            new = True
            y = np.random.random([10,1])
            print("first coord")
            firstcoord[0] = event.xdata
            firstcoord[1] = event.ydata
            first = False
            #rect = patches.Rectangle((50, 100), 40, 30, linewidth=1, edgecolor='r', facecolor='none')
            """
            rect = patches.Rectangle((firstcoord[0], firstcoord[1]), secondcoord[0]-firstcoord[0], secondcoord[1]-firstcoord[1], linewidth=3, edgecolor='r', facecolor='none')
            ax.add_patch(rect)
            plt.pause(0.0001)
            """
            
        else:
            y = np.random.random([10,1])
            print("second coord")
            secondcoord[0] = event.xdata
            secondcoord[1] = event.ydata
            #plt.plot(y)
            if crop == -1:
                first = True
                new = False
                rect = patches.Rectangle((firstcoord[0], firstcoord[1]), secondcoord[0]-firstcoord[0], secondcoord[1]-firstcoord[1], linewidth=3, edgecolor='r', facecolor='none')
                ax.add_patch(rect)
                coordval = ((firstcoord[0],firstcoord[1]),(secondcoord[0],secondcoord[1]))
                import xml.etree.ElementTree as ET
                # Reading data from the xml file
                
                newname = filename.replace("images/","")
                
                newname = replace(newname)
                
                file = open("images/"+newname+".txt","a")
                firstcoord[0] = round(firstcoord[0],5)
                firstcoord[1] = round(firstcoord[1],5)
                secondcoord[0] = round(secondcoord[0],5)
                secondcoord[1] = round(secondcoord[1],5)
                centerx = (firstcoord[0]+secondcoord[0])/2/1000
                centery = (firstcoord[1]+secondcoord[1])/2/1000
                width = secondcoord[0]-firstcoord[0]
                height=secondcoord[1]-firstcoord[1]
                width = round(width,5)/1000
                height = round(height,5)/1000
                centerx = round(centerx,5)
                centery = round(centery,5)
                width = round(width,5)
                height = round(height,5)
                #print("center"+str(center))
                width = abs(width)
                height = abs(height)
                text = "0 "+str(centerx)+" "+str(centery)+" "+str(width)+" "+str(height)+"\n"
                file.write(text)
                #file.close()


                print(firstcoord[1])
                print(secondcoord[1])
                
                
                

                

                plt.pause(0.0001)
                nextimage = True
                
                coordlist.append(coordval)
                
                line = {filename : coordlist}
                
            if crop == 1:
                first = True
                new = False
                w=secondcoord[0]-firstcoord[0]
                h=secondcoord[1]-firstcoord[1]
                
                im = im[int(firstcoord[1]):int(firstcoord[1])+int(h), int(firstcoord[0]):int(firstcoord[0])+int(w)]
                
                
                im = cv2.resize(im, dsize=(416, 416), interpolation=cv2.INTER_CUBIC)
                ax.imshow(im)
                
                
                
                plt.pause(0.0001)
                
                [p.remove() for p in reversed(ax.patches)]
                try:
                    cv2.imwrite(filename, cv2.cvtColor(im, cv2.COLOR_RGB2BGR))
                    #filename = '/home/pierre/Documents/machinelearning/abeilles/coco/images/train/'+'cropped'+str(counter)+'.png'
                except:
                    
                    print("[error] errrror")
                counter +=1
                crop = -crop
        #if event.button is MouseButton.RIGHT:

first = 1
for file in glob("images/*"):
    filename = file
    
    print("file : "+filename)
    
        
    im = np.array(Image.open(filename), dtype=np.uint8)
    im = cv2.resize(im, dsize=(1000, 1000), interpolation=cv2.INTER_CUBIC)
    fig, ax = plt.subplots()
    ax.imshow(im)
    
    binding_id = plt.connect('motion_notify_event', on_move)
    plt.connect('button_press_event', on_click)
    plt.connect('key_press_event', on_key)
    plt.connect('close_event', on_close)
    plt.show()
    
    
    while nextimage == False:
        pass
        
            
    
    nextimage = False
           
        





