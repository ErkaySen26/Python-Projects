import pyautogui as pg
import time


time.sleep(5)

mesaj="naber"

for i in range(30):
       pg.write(mesaj)
       pg.press("Enter")