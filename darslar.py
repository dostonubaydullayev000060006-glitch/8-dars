import os
os.system("cls")

import cv2

camera = cv2.VideoCapture(0)

is_valid, image = camera.read()

if is_valid:
    cv2.imwrite("rasm.png",image)
    print("Rasam saqlandi: ")

else:
    print("Xatolik...")