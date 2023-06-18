# Description
For yolov4 custom model train : annotate data easily with this simple tool.
To use with this repo : https://github.com/AlexeyAB/darknet
# different OS
Probably work with Windows but i didn't tried.

May also work with Mac OS but i am unsure, feel free to try.

Totally works on Linux !
# How to use
open a terminal and type following commands : 

```git clone https://github.com/proplayer2020/annot_data/ ```

```cd annot_data```

Then, go into "images" folder and create as many folders as the number of classes (starting from 0) and put your images here (class order isnt important just do not shuffle classes into the same folder).

Here is an example (if the model will have to recognize flowers and cars):

```images/0/*``` (car images here)

```images/1/*``` (flower images here)

## Annotate a single class :
Just run this command :

```python3 annot_tool.py 0```

## Annotate multiple classes :
Organize all classes in directories (one directory per class), for example :

    images/0/*

    images/1/*
    
    images/2/*
```python3 annot_tool.py 0``` # for images/0/*

```python3 annot_tool.py 1``` # for images/1/*

```python3 annot_tool.py 2``` # for images/2/*


It is possible to change names later while training to change "obj.names" with all your names, in this order.

## how to use annotation tool : 

Just click on the first position IN TOP LEFT CORNER OF THE OBJECT, and then click in THE BOTTOM RIGHT CORNER, you will see a red bouding box that isn't moving with your cursor (if the bouding box moves, click again in the right position), then, just close the window, another image will appear.

Useful keybind in the annotation program : 
- 'q' to quit
- 'n' to skip image
- 'c' to crop (for zooming on a restricted area, this cannot be undoned)

## prepare data for training
When all images are annoted, copy paste them in the images folder (so delete all 0,1,2 folders)
Then enter in terminal

```python3 traintest_split.py --nb_test <number of image to put in test set> --path <path to image folder (containing all images with all .txt)> --nb_class <number of classes in the dataset>```

This code will split all annoted images into two .txt files : train.txt and test.txt.
Images_nb arg is to define the number of images in test.txt set (at least 10-15 percent)
All other images will go into train set.

The train command will use those files (where has been put all images name)
# Visualize data

Use the 'see_data.py' script to see if all images were annoted correctly

In the terminal : 

```python3 see_data.py --datapath <here the path of the train.txt or test.txt created previously with traintest_split.py>```

If some annotations are bad, go into the console (e.g the terminal) and delete image, txt file and the image name in the train.txt (or test.txt), else, the model will ignore the image or throw an error.
# How to use the output:

Download this repository following instructions : https://github.com/AlexeyAB/darknet

Then compile it to make it work : https://github.com/AlexeyAB/darknet#how-to-compile-on-linux-using-make

Take the two files generated in "result" folder in this repository (train.txt and test.txt) and put them in the data folder in the darknet repository

Prepare for training (YOLO) : https://github.com/AlexeyAB/darknet#how-to-train-to-detect-your-custom-objects
Prepare for training (YOLO tiny) : https://github.com/AlexeyAB/darknet#how-to-train-tiny-yolo-to-detect-your-custom-objects

NOTE : if "darknet.exe" is written in the command, replace it with ./darknet on linux.

# What are the advantages and inconvenients of this program :

 ✔️  Easy to use
 
 ✔️  Totally free to use and no liscence
 
 ✔️  99% working lol
 
 ✔️  Im active and will respond to all of your concerns
 
 ❌ A bit slow to refresh (made with matplotlib lol)
 
 ❌ Sometimes the bounding box do weird things, (in that case type 'n' to go to next image and then delete the faulty image)

Now you are all set to train a custom model with the githu below !

# Help
feel free to post issue, im active and i will try to respond to your questions
