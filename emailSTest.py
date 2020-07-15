#!/usr/bin/env python3
import os
import reports
import emails
import glob
import mimetypes
from datetime import date

studID = "mayer_elias" 

#creates E-Mail
myEMail = EmailMessage() #creates Email Obj
myEMail['From'] = "EliDerDeli_automation@example.com"
myEMail['To'] = "{}@yahoo.com".format(str(studID))
myEMail['Subject']  = " Upload Completed - Online Fruit Sto"
bod = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
myEMail.set_content(bod)

#create an E-Mail attachment (Attach my PDF from the reports script)
attachFilename = os.path.basename(attachmentPath)
mimetype = mimetype.guess_type(attachmentPath)
mime_type, mime_subtype = mimetype.split('/',1)

#attaches my PDF from external script run.py
with open(attachmentPath, 'rb') as ap:
    myEMail.add_attachment(ap.read(),mime_type,mime_subtype,attachFilename)

#inits mail server for sending
mail_server = smtplib.SMTP('localhost')
mail_server.send_message(message)
mail_server.quit()

#send my Mail
mail_server.send_email(myEmail)
