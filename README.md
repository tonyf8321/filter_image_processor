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

for example, the options that can be chosen are:

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

Images may be put into the *imgsGathered* directory. 

If they are not in the directory that *IMG_PATH = 'imgsGathered'* specifies, the program will have issues if the following below is not carried out.

Images do not have to be put into *imgsGathered* directory.
If this is the case, ensure the folder with images is in the same directory as *imgProcess.py*.

Next, change the value for IMG_PATH to the newly added directory that has the images:

```sh
IMG_PATH = '<directory_with_your_images>'
```

### Step 4:

Enter the name of an image into the IMG_NAME value area:

```sh
IMG_NAME = '<image_name_only_here>'
```

For example, if we have an image, *pineapple.jpg*, what is enter would be:

```sh
IMG_NAME = 'pineapple'
```

### Step 5:

Enter *True* or *False* for the CHECK_GREY value in code (default is False):

This option will convert the image to black and white, and nothing else further.

```sh
CHECK_GREY = <True_or_False>
```

**Important: when this is set to True, the filter option will be negated**.

With this in mind, setting to True than moving the image back to the IMG_PATH selected directory, it can be further filter while being grey if desired.

### Step 6

Set the IMG_EXT value to match the extension on the selected image:

```sh
IMG_EXT = '.<file_extension_goes_here>'
```

So, if we have *pie.jpg* we get *.jpg* and set the code to look like:

```sh
IMG_EXT = '.jpg'
```

### Step 7:

Set the FILT_IMG_FOLD directory name (default is *filteredImages*).

If the folder does not exists, one will be created and store the processed image.

This will save the processed images to this folder. Name as desired.

```sh
FILT_IMG_FOLD = '<processed_images_folder_name_here>'
```

**Note**: Images processed will be converted to *.png* format, and the name of the photo to be changed to <<originalName>,<filterOptName>,.png>.
