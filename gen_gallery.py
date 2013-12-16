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


# #!/usr/local/bin/python
# import csv
# import glob
# import os
# from PIL import Image

# web_size = 960, 720

# with open('data/images.csv', 'rb') as csvfile:

#   for row in csv.DictReader(csvfile):

#     img_glob = "data/files/images/{}.{}.*".format(row['item_id'], row['image_id'])
#     img_name = glob.glob(img_glob)[0]
#     web_name = "data/files/web/{}.{}.jpg".format(row['item_id'], row['image_id'])
#     print "looking at {}".format(img_name)

#     try:
#       img = Image.open(img_name)
#       img.thumbnail(web_size, Image.ANTIALIAS)
#       if row['type'] == '0':
#         img.save(web_name, "JPEG", quality=50)
#       print "created {}".format(web_name)
#     except IOError:
#       print "could NOT create {}".format(web_name)

#     del img
