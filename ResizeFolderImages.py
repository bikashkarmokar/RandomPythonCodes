# Resize all images in a directory to specific size.
#
# Have to install "python-resize-image" before using
# pip install python-resize-image
#
# If the script is in /images/ and the files are in /images/imagefolder
# call with: python ResizeFolderImages.py imagefolder
#
# Bikash Karmokar, 22/08/2018
#---------------------------------------------------

from PIL import Image
import os
import sys

directory = sys.argv[1]

for file_name in os.listdir(directory):
  print("Processing %s" % file_name)
  image = Image.open(os.path.join(directory, file_name))

  new_dimensions = (227, 227)
  output = image.resize(new_dimensions, Image.ANTIALIAS)

  output_file_name = os.path.join(directory,file_name)
  output.save(output_file_name, "JPEG", quality = 95)

print("Resize done")