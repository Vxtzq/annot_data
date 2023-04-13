# Description
For yolov4 custom model train : annot data easily with this simple tool.
To use with this repo : https://github.com/AlexeyAB/darknet
# How to use
open a terminal and type following commands : 

```git clone https://github.com/proplayer2020/annot_data/ ```

```cd annot_data```
  
  then naviguate to the "images" folder into annot_data and put your dataset here then, execute annotation code : 
  
```python3 annot_tool.py class_id=0```

If you see an image (from your dataset) appearing on the screen, its most likely that its working
HOW TO USE ANNOTATION TOOL : 

Just click on the first position IN TOP LEFT CORNER OF THE OBJECT, and then click in THE BOTTOM RIGHT CORNER, you will see a red bouding box that isn't moving with your cursor (if the bouding box moves, click again in the right position), then, just close the window, another image will appear.

Useful keybind in the annotation program : 
- 'q' to quit
- 'n' to skip image
- 'c' to crop (for zooming on a restricted area, this cannot be undoned)

## Annot a single class :
Just follow tutorial below

## Annot multiple classes :
Organize all classes in directories (one directory per class), for example :
    images/0/*

    images/1/*
    
    images/2/*
```python3 annot_tool.py class_id=0``` # for images/0/*

```python3 annot_tool.py class_id=1``` # for images/1/*

```python3 annot_tool.py class_id=2``` # for images/2/*

It is possible to change names later while training to change "obj.names" with all your names, in this order.

## What are the advantages and inconvenients of this program :

 ✔️  Easy to use
 
 ✔️  Totally free to use and no liscence
 
 ✔️  99% working lol
 
 ✔️  Im active and will respond to all of your concerns
 
 ❌ A bit slow to refresh (made with matplotlib lol)
 
 ❌ Sometimes the bounding box do weird things, (in that case type 'n' to go to next image and then delete the faulty image)

Once all of the images are annoted, enter in terminal : 

```python3 traintest_split.py images_nb=<number of image to put in test set>```

This code will split all annoted images into two .txt files : train.txt and test.txt.
Images_nb arg is to define the number of images in test.txt set (at least 10-15 percent)
All other images will go into train set.
Now you are all set to train a custom model with the githu below !
# Train custom yolov4 model with this github using the data this repository provides by following all the steps: 
  https://github.com/AlexeyAB/darknet
  
#Usefull links for begginners to custom yolo model training (in the link below): 

  -https://github.com/AlexeyAB/darknet#how-to-compile-on-linux-using-make - once the darknet repo downloaded, compile it using make command
  
  -https://github.com/AlexeyAB/darknet#how-to-train-to-detect-your-custom-objects - train custom yolov2, v3 or v4  (if you have used this repo, do yolov4)
  
  -https://github.com/AlexeyAB/darknet#how-to-train-tiny-yolo-to-detect-your-custom-objects - train yolov4 TINY for mobile developpmen

# Help
feel free to post issue, im active and i will try to respond to your questions
# Other usefull tools (Coming soon): 
use "convertdataset.py" to resize all images and convert them to jpg (no image replacing, but if you dont want all images to be sort of duplicated, do it in another directory) 
