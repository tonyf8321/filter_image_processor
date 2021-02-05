# filter_image_processor


# Setup
Get the associated repository file and folder to a virtual envrionment folder and activate the environment accordingly.

Install dependencies.

As a reminder:
```sh
$ pip install -r requirements.txt
```

# Usage:

### Step 1:

Choose what FILT_OPT(this will dictate the filter applied to the image) is,

```sh
FILT_OPT = 'FIND_EDGES'
```

for example, the option that can be chosen are:

SHARPEN, EMBOSS, FIND_EDGES, EDGE_ENHANCE, EDGE_ENHANCE_MORE, DETAIL,CONTOUR,FIND_EDGES, BLUR, SMOOTH, SMOOTH_MORE

If any options were missed, checkout
https://pillow.readthedocs.io/en/stable/reference/ImageFilter.html?highlight=imagefilter
for a list of filters.

### Step 2:
The filter that you have selected in **FILT_OPT**, copy and paste that filter name to
filtered_img = img.filter(ImageFilter.<FilterNameGoesHere>), 

```sh
def save_normal_option():
    ...
    filtered_img_inp = img.filter(ImageFilter.<filter_opt_typed_here>)
    ...
```

for example, following the previous FILT_OPT in step 1, we would set it to *FIND_EDGES*, giving:

filtered_img_inp = img.filter(ImageFilter.FIND_EDGES)
    
### Step 3:

Images may be put into the *imgsGathered* directory. If they are not in the directory that *IMG_PATH = 'imgsGathered'* specifies, the program will have issues if the following below is not carried out.

Images do not have to be put into *imgsGathered* directory.
If this is the case, ensure the folder with images is in the same directory as *imgProcess.py*.

Next, change the value for IMG_PATH to the newly added directory that has the images:

```sh
IMG_PATH = '<directory_with_your_images>'
```
# -----BELOW UNFINISHED-----NEED FORMATTING EDIT-----
### Step 4:
Looking at imgName = '<imgNameGoesHere>', enter your image name between
the apostrophes to set the image on this
program to be further manipulated. As an example, if you have a image
names bestImage, then what you will have is
imgName = 'bestImage'
  
  
Step 5:
Where you see the variable, "checkGrey = False", you may have it equaled
to False or True to enable the grey filter
after the main filter is applied, this means it will apply step 1's filter
and then if you have checkGrey = True
then the image will be converted into a black and white type of image.


Step 6:
Very important like all the other steps, step six involves changing the
extension to match that of the original image,
so if you have an image, for example, named "smileyImage.jpg" you will
look at the extension <.jpg> and type that
between the apostrophes, so in this example you would have imgExt = '.jpg'
Another example, say you have
imageZebras.gif then you'd have imgExt = '.gif'


Step 7
Assuming you are running this on pycharm hold Shift and tap F10 and ensure
that it highlights this program with
its name to ensure everything runs accordingly. Once ran, a new folder
will be made named filteredImages with a new
filtered image(s) made by you. Expand filteredImages and double click on
the image to view it, and rinse and repeat
to form higher quality photos. Look into DETAIL and SHARPEN and
EDGE_ENHANCE for the best upgraded quality pictures.
Note: images will be converted to png format
