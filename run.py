#! /usr/bin/env python3
import os, glob
import requests
import json
import re
import sys
import collections

sys.stdout.write("Started the Process")
dict = collections.OrderedDict()

stud = "/home/student-02-c4ee61e4549b" #stud adresse
myIp = "http://35.225.250.79" #ip target

keys = ["name","weight","description","image_name"]
hPath = glob.glob(stud + "/supplier-data/descriptions/*.txt")

#temp Storage Lists
listC = []  # for sorted versio
kThreeList = [] # for temo storing images
finList = [] # for merged final list - every ele ready for json export

for f in hPath:
      with open(f) as file:
        i = 0
        for realine in file:
            realine = realine.replace(u"\u00A0", " ")
            realine = realine.rstrip("\n")
            if i <= 2:
                if keys[i] == "weight": #weight to int
                    val = realine
                    intV = re.search('[0-9]*', val)
                    realine = int(intV.group(0))
                dict.update({keys[i] :realine})
                i = i + 1 # count trough keys
        f_Name = os.path.basename(f)
        img = f_Name.replace(".txt",".jpeg")
        kThreeList.append(img)
        listC.append(dict.copy()) #append to my List

for i in range(0,len(listC)): #merges the pics in my array
   dictSmall = listC[i]
   img = kThreeList[i]
   dictSmall.update({keys[3] : img})
   #sys.stdout.write(str(dictSmall))
   finList.append(dictSmall.copy())

an = 0
for ele in finList:
    ras = requests.post(myIp + "/fruits/",json=ele)
    sys.stdout.write(str(ras))
    an = an + 1
sys.stdout.write(" Finished the Process")

