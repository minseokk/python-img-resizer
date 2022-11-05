from PIL import Image

from resizeimage import resizeimage

import os

cur_path = os.path.dirname(__file__)

new_path = os.path.relpath('./input/', cur_path)

artist = "yoonji"
count = 1

for filename in os.listdir(new_path):
    print(filename)
    path_filename = './input/' + filename

    with open(path_filename, 'r+b') as f:
        with Image.open(f) as image:
            cover = resizeimage.resize_width(image, 500)
            new_filename = "./output/sm-" + artist + str(count) + os.path.splitext(filename)[1]
            print(new_filename)
            cover.save(new_filename, image.format)
            count += 1