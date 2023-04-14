import os
from glob import glob
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--nb_test", help="number of images in the test set (approximatly 10 images for 100)")

parser = argparse.ArgumentParser()
parser.add_argument("--nb_test",help="number of images in the test set (approximatly 10 images for 100)")
parser.add_argument("--path",help="path to annoted images e.g /home/user/images/")
args = parser.parse_args()


"""
parser = argparse.ArgumentParser()
parser.add_argument("path", help="path to folder where all (annoted) images are e.g /home/user/images/, dont forget the / at the end")
"""


alltxt = []
counter = 0
#for file in glob(args.path.replace("path=","")):
for file in glob(args.path+"*"):
    if not "txt" in file:
        alltxt.append(file)
file = open("result/test.txt","w")     
for i in range(int(args.nb_test.replace("nb_test=",""))):
    name = str(alltxt[counter])
    file.write(os.path.abspath(name))
    counter +=1
file = open("result/train.txt","w")  
for i in range(len(alltxt)-int(args.nb_test.replace("nb_test=",""))):
    name = str(alltxt[counter])
    file.write(os.path.abspath(name))
    counter +=1
