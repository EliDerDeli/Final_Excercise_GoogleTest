#!/usr/bin/env python3

import datetime, os
from reports import generate_report # own cus py module
from emails import generate_email, send_email #own cus py module 


def createBodText(desc_dir): # simple function to convert Txt file in one string with right formating  (as prep for PDF reports.py)
    res = []
    for item in os.listdir(desc_dir):
      filename=os.path.join(desc_dir,item)
      with open(filename) as f:
        line=f.readlines()
        weight=line[1].strip('\n')
        name=line[0].strip('\n')
        res.append(('name: ' +name),('weight: '+weight)) # append string tuple
    # complete string
    finalStr = ""  # initializing the final String
    for i in range(len(res)):
        if res[i]:
            finalStr += res[i][0] + '<br />' + res[i][1] + '<br />' + '<br />'
    return finalStr


'''The global variable, __name__, in the module that is the entry point to your program, 
is '__main__'. Otherwise, it's the name you import the module by.'''

#----------------------MAIN---------------------------
if __name__ == "__main__":

    user = os.getenv('USER')
    dirDescr = '/home/{}/supplier-data/descriptions/'.format(user)  # The directory which contains all the files with data in it.

    current_date = datetime.date.today().strftime("%B %d, %Y")
    title = 'Processed Update on ' + str(current_date)

    BodFromTxt = createBodText(dirDescr)
    generate_report('/tmp/processed.pdf', title, BodFromTxt)  # reports >> cus module

    # content
    emailSub = 'Upload Completed - Online Fruit Store'
    emailBod = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'

    # final call function definitions
    reciever = '{}@example.com.com'.format(user)
    sender =  'automation@example.com'
    path = '/tmp/processed.pdf'

    # email >> cus module
    msg = generate_email(sender, reciever, emailSub, emailBod, path)
    send_email(msg)
