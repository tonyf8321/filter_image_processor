# filter_image_processor
-----BELOW UNFINISHED-----NEED FORMATTING EDIT-----
# Step 1:
# Choose what var1(this will dictate the filter applied to the image) is,
# for example, between the apostrophes type
# one of the option:
# SHARPEN, EMBOSS, FIND_EDGES, EDGE_ENHANCE, EDGE_ENHANCE_MORE, DETAIL,
# CONTOUR,
# FIND_EDGES, BLUR, SMOOTH, SMOOTH_MORE
# if any option were missed, checkout
# https://pillow.readthedocs.io/en/stable/reference/ImageFilter.html
# ?highlight=imagefilter
# for a list of filters.
# Step 2:
# The filter that you have selected in var1, copy and paste that filter name to
# filtered_img = img.filter(ImageFilter.<FilterNameGoesHere>), for example,
# if you selected filter CONTOUR, you will
# have filtered_img = img.filter(ImageFilter.CONTOUR) on line 43
# Step 3:
# ensure that this main file is in the same folder as the folder that has
# your images after that is done,
# in between the apostrophes of imgPath = '<FolderNameHere>' type in the
# folder name that has your images. As an
# example, if you have a folder name coolPhotos then what you will have is
# imgPath = 'coolPhotos'
# Step 4:
# Looking at imgName = '<imgNameGoesHere>', enter your image name between
# the apostrophes to set the image on this
# program to be further manipulated. As an example, if you have a image
# names bestImage, then what you will have is
# imgName = 'bestImage'
# Step 5:
# Where you see the variable, "checkGrey = False", you may have it equaled
# to False or True to enable the grey filter
# after the main filter is applied, this means it will apply step 1's filter
# and then if you have checkGrey = True
# then the image will be converted into a black and white type of image.
# Step 6:
# Very important like all the other steps, step six involves changing the
# extension to match that of the original image,
# so if you have an image, for example, named "smileyImage.jpg" you will
# look at the extension <.jpg> and type that
# between the apostrophes, so in this example you would have imgExt = '.jpg'
# Another example, say you have
# imageZebras.gif then you'd have imgExt = '.gif'
# Step 7
# Assuming you are running this on pycharm hold Shift and tap F10 and ensure
# that it highlights this program with
# its name to ensure everything runs accordingly. Once ran, a new folder
# will be made named filteredImages with a new
# filtered image(s) made by you. Expand filteredImages and double click on
# the image to view it, and rinse and repeat
# to form higher quality photos. Look into DETAIL and SHARPEN and
# EDGE_ENHANCE for the best upgraded quality pictures.
# Note: images will be converted to png format
