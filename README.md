# Description
For yolov4 custom model train : annot data easily with this simple tool.
To use with this repo : https://github.com/AlexeyAB/darknet
# How to use
open terminal
- git clone https://github.com/proplayer2020/annot_data/
- cd annot_data
- python3 annot_tool.py

If you see an image (from your dataset) appearing on the screen, its most likely that its working

# FAQ
why do i get this error ? Traceback (most recent call last):
  File "annot_tool.py", line 199, in <module>
    im = np.array(Image.open(filename), dtype=np.uint8)
  File "/home/pierre/.local/lib/python3.8/site-packages/PIL/Image.py", line 3283, in open
    raise UnidentifiedImageError(msg)
PIL.UnidentifiedImageError: cannot identify image file 'images/instructions'

Verify that the images folder isnt empty and try again
