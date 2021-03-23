#!/usr/bin/env python
# coding: utf-8

# In[49]:


import csv
import cv2
color = (0,0,255)

path1 = input('Enter the path of the csv file :')
path2 = input('Enter the path of directory where video frames are residing:')

#in my case: path1 = /home/sanu/track.csv
# path2 = /home/sanu/Documents/Koldrone_Frames/

def displaycsv(path1,path2):
    with open(path1,'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter = ",")
        for rows in csvfile:
            frame_details = list(rows.split(","))
            frameno = frame_details[0]
            framename =('Frame' + frameno + '.jpg')
            xtl=int(float(frame_details[1]))
            ytl=int(float(frame_details[2]))
            xbr=int(float(frame_details[3]))
            ybr=int(float(frame_details[4]))
            #print(type(xtl))
            start=(xtl,ytl)
            end=(xbr,ybr)
            img = cv2.imread(path2+framename)
            img = cv2.rectangle(img,start,end,color,2)
            #cv2.imwrite("/home/sanu/Documents/Annotated_Frames/"+ "Annotated" + frameno + ".jpg",img)
            filename = 'Annotated' + frameno + ".jpg" 
            cv2.imwrite("/home/sanu/Documents/Annotated_Frames/"+filename,img)

        

displaycsv(path1,path2)


# In[ ]:




