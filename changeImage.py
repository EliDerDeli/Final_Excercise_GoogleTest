#!/usr/bin/env python3
import glob
import os
from PIL import Image

#3000x2000 px --> 600x400 px
size = 600,400
stud = "/home/student-03-e7f8bddc7273" #stud adresse

#.TIFF --> .JPEG (no overwritte)
for f in glob.glob( stud + "/supplier-data/images/*.tiff"):
   imC = Image.open(f).convert('RGB')
   newName = os.path.basename(f)[:3]
   imC.resize((size)).save(stud + "/supplier-data/images/" + newName + ".jpeg", "JPEG")
