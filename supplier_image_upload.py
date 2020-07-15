#! /usr/bin/env python3
import requests
import glob
import os

stud = "/home/student-03-e7f8bddc7273" #stud adresse

url = "http://localhost/upload/"
for files in glob.glob(stud + "/supplier-data/images/*.jpeg"):
   with open(files, 'rb') as f:
      r = requests.post(url, files={'file': f})


