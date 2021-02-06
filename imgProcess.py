from PIL import Image, ImageFilter
import pathlib

# Change these options accordingly
FILT_OPT = 'FIND_EDGES'
IMG_PATH = 'imgsGathered'
IMG_NAME = 'exampImg'
CHECK_GREY = False
IMG_EXT = '.jpg'
FILT_IMG_FOLD = 'filteredImages'


def save_grey_option():
    filtered_img_inp = img.convert('L')
    filtered_img_inp.save(f'./{FILT_IMG_FOLD}/{IMG_NAME}Grey.png', 'png')


def save_normal_option():
    # DON'T FORGET TO CHANGE THIS OPTION ACCORDINGLY
    filtered_img_inp = img.filter(ImageFilter.FIND_EDGES)
    filtered_img_inp.save(f'./{FILT_IMG_FOLD}/{IMG_NAME}{FILT_OPT}.png', 'png')


if __name__ == '__main__':
    with Image.open(f'./{IMG_PATH}/{IMG_NAME}{IMG_EXT}') as img:
        try:
            if CHECK_GREY:
                save_grey_option()
            else:
                save_normal_option()
        except FileNotFoundError:
            pathlib.Path(f'./{FILT_IMG_FOLD}').mkdir()
            if CHECK_GREY:
                save_grey_option()
            else:
                save_normal_option()
