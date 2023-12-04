import os
import glob
import pandas as pd
import io
import xml.etree.ElementTree as ET
import argparse


path = 'Tensorflow/workspace/images/train'
for xml_file in glob.glob(path + '/*.xml'):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    for member in root.findall('object'):
        if member[0].text == 'airplane':
            print(member[0].text)
            member[0].text = 'Airplane'
            print(member[0].text)
        width = int(root.find('size')[0].text)
        height = int(root.find('size')[1].text)
        xmn = int(member[5][0].text)
        xmx = int(member[5][1].text)
        ymn = int(member[5][2].text)
        ymx = int(member[5][3].text)

        if xmn < 0:
            xmn = 0
        elif xmn > height:
            xmn = height
        if xmx < 0:
            xmx = 0
        elif xmx > height:
            xmx = height
        if ymn < 0:
            ymn = 0
        elif ymn > height:
            ymn = height
        if ymx < 0:
            ymx = 0
        elif ymx > height:
            ymx = height
        
        if xmn > xmx:
            member[5][0].text = str(xmx)
            member[5][1].text = str(xmn)
        if ymn > ymx:
            member[5][2].text = str(ymx)
            member[5][3].text = str(ymn)
    tree.write(xml_file)

path = 'Tensorflow/workspace/images/test'
for xml_file in glob.glob(path + '/*.xml'):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    for member in root.findall('object'):
        if member[0].text == 'airplane':
            print(member[0].text)
            member[0].text = 'Airplane'
            print(member[0].text)
            xmn = int(member[5][0].text)
        xmx = int(member[5][1].text)
        ymn = int(member[5][2].text)
        ymx = int(member[5][3].text)
        if xmn > xmx:
            member[5][0].text = str(xmx)
            member[5][1].text = str(xmn)
        if ymn > ymx:
            member[5][2].text = str(ymx)
            member[5][3].text = str(ymn)
    tree.write(xml_file)