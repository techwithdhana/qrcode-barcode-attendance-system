# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 20:16:26 2021

@author: Dhanasekar
"""

import cv2
import numpy as np
from pyzbar.pyzbar import decode

# scan the qrcode and get the info about the image using decode funtion:

# img = cv2.imread("qr-code images/a.png")
# info = decode(img)

# for data in info:
#     print(data.data)
    
#     # decode the actual getting info
#     decodeData = data.data.decode('utf-8')
#     print(decodeData) 
    
# access the webcam:


cap = cv2.VideoCapture(0)
cap.set(3, 400)
cap.set(4, 600)

with open('namesList.txt') as f:
    listData = f.read().splitlines()
    print(listData)


while False:
    success, frame = cap.read()
    info = decode(frame)
    for data in info:
        decodeData = data.data.decode('utf-8')
        print(decodeData)

        if decodeData in listData:
            result = "Auth"
            color = (0, 255, 0)
        else:
            result = "Un-Auth"
            color = (0, 0, 255)


        pts = np.array([data.polygon], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(frame, [pts], True, (255, 0, 0 ), 2)
        pts1 = data.rect
        cv2.putText(frame, result, (pts1[0], pts1[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 3)
        
    cv2.imshow("stream", frame)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break
    