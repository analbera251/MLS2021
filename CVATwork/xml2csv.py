#!/usr/bin/env python
# coding: utf-8

# In[10]:


import xml.etree.ElementTree as ET
import csv
tree = ET.parse('/home/sanu/Documents/track.xml')
root = tree.getroot()
print(root)
fields = ['frameno','xtl','ytl','xbr','ybr']
filename = "track.csv"    # name of the csv file

with open(filename,'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    
    csvwriter.writerow(fields)
Tracks = root.findall("track")

with open(filename,'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    for i in Tracks:
        for j in range(2):
            frame = i[j].attrib['frame']
            #print(frame2)
            frame = format(int(frame),'03d')
            row=(frame,i[1].attrib['xtl'],i[1].attrib['ytl'],i[1].attrib['xbr'],i[1].attrib['ybr'])
            print(row)
            csvwriter.writerow(row)
        

