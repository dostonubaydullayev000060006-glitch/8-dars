import os
os.system("cls")

import cv2
camera = cv2.VideoCapture("http://192.168.181.227:4747/video")

while True:
    is_valid, image = camera.read()
    if is_valid:
        cv2.imshow("Selfi",image)

    if cv2.waitKey(1) & 0xfff==32:
        break  