#Read all this before starting
s
# Description
For yolov4 custom model train : annot data easily with this simple tool.
To use with this repo : https://github.com/AlexeyAB/darknet
# How to use
open terminal and type following commands : 

```git clone https://github.com/proplayer2020/annot_data/ ```

```cd annot_data```
  
  then naviguate to the "images" folder into annot_data and put your dataset here then, execute annotation code : 
  
```python3 annot_tool.py```

If you see an image (from your dataset) appearing on the screen, its most likely that its working

Useful keybind in the annotation program : 
- 'q' to quit
- 'n' to skip image
- 'c' to crop (for zooming on a restricted area, this cannot be undoned)

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
