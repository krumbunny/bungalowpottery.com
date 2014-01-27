#!/usr/local/bin/python

import glob
import os
from PIL import Image

with open('_data/gallery.yml', 'w+') as gallery_file:

  # os.chdir('images/gallery')

  for category in os.listdir('images/gallery'):
    if category[0] == '.': continue
    
    gallery_file.write(category + ':\n')

    img_glob = "images/gallery/{}/*.jp*g".format(category)
    for img_file in glob.glob(img_glob):
      img = Image.open(img_file)
      exif_data = img._getexif()

      gallery_file.write("  - file: " + img_file + "\n")
      gallery_file.write("    caption: " + exif_data[270] + "\n")
