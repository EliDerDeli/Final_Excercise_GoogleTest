#!/usr/bin/env python3
import os
from reportlab.platypus import Paragraph, Spacer, Image, SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(title, attachment, paragraph):
   # title as Title, 
   # attachment as file Path of generated PDF,
   # paragraph as text descritption
   # generates a pdf called processed.pdf
   styles = getSampleStyleSheet() 
   report = SimpleDocTemplate(attachment)
   rTitle = Paragraph(title, styles['h1'])
   rBod = Paragraph(paragraph, styles['BodyText'])
   rLineSpace = Spacer(1,20)
   report.build([rTitle, rLineSpace, rBod, rLineSpace])
   


