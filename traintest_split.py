import os
from glob import glob
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--nb_test", help="number of images in the test set (approximatly 10 images for 100)")

parser = argparse.ArgumentParser()
parser.add_argument("--nb_test",help="number of images in the test set (approximatly 10 images for 100)")
parser.add_argument("--nb_class",help="number of casses (including the class 0)")
parser.add_argument("--path",help="path to annoted images e.g /home/user/images/")
args = parser.parse_args()


"""
parser = argparse.ArgumentParser()
parser.add_argument("path", help="path to folder where all (annoted) images are e.g /home/user/images/, dont forget the / at the end")
"""


alltxt = []
print(alltxt)
counter = 0
#for file in glob(args.path.replace("path=","")):
for i in range(int(args.nb_class)):
    print(args.path+str(counter)+"/"+"*"+"\n")
    for file in glob(args.path+str(counter)+"/"+"*"):
        
        if not "txt" in file:
            alltxt.append(file)
            
    counter +=1
counter = 0
file = open("result/test.txt","w")     
for i in range(int(args.nb_test.replace("nb_test=",""))):
    name = str(alltxt[counter])
    file.write(os.path.abspath(name)+"\n")
    counter +=1
file = open("result/train.txt","w")  
for i in range(len(alltxt)-int(args.nb_test.replace("nb_test=",""))):
    name = str(alltxt[counter])
    file.write(os.path.abspath(name)+"\n")
    counter +=1
