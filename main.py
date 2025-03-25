import os
from pyzbar.pyzbar import decode
import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

s = True
while s:
    s, img = cap.read()
    db = decode(img)
    for data in db:
        id, password = data.data.decode("utf-8").split()
        os.system(f'cmd /с "netsh wlan set hostednetwork mode=allow ssid={id} key={password}"')
        os.system(f'cmd /с "netsh wlan connect ssid={id} name={id}"')
    cv2.imshow("Result", img)
    cv2.waitKey(1)
