import os
from glob import glob
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("nb_images", help="number of images in the test set (approximatly 10 images for 100)")
args = parser.parse_args()
alltxt = []
counter = 0
for file in glob("images/*"):
    if not "txt" in file:
        alltxt.append(file)
file = open("result/test.txt","w")     
for i in range(int(args.nb_images.replace("nb_images=",""))):
    name = str(alltxt[counter])
    file.write(os.path.abspath(name))
    counter +=1
file = open("result/train.txt","w")  
for i in range(len(alltxt)-int(args.nb_images.replace("nb_images=",""))):
    name = str(alltxt[counter])
    file.write(os.path.abspath(name))
    counter +=1
