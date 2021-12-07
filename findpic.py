from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

while 1:
    if pyautogui.locateOnScreen('zobacz.png', confidence=0.8 ) != None:
        print("Widze znaki")
        time.sleep(0.5)
    else:
        print("no nie widze")
        time.sleep(0.5)
    print((pyautogui.locateOnScreen('zobacz.png', confidence=0.8 ))[0],(pyautogui.locateOnScreen('zobacz.png', confidence=0.8 ))[1])