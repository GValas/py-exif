

import os
import piexif
from PIL import Image

 
# file = "data/01.02 - Cannes 2000/Cannes2000 08.jpg"
file = "data/01.01 - Cambrils2000/Cambrils2000 - Fanny - 03.jpg"
path = os.path.join(os.getcwd(), file)
 
img = Image.open(path)
exif_dict = piexif.load(img.info['exif'])

altitude = exif_dict['GPS'][piexif.GPSIFD.GPSAltitude]
print(altitude)
 

 