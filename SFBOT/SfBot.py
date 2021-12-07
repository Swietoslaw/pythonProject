import pyautogui as pyg
import time
import keyboard
import random
from pyautogui import *

time.sleep(0.05)
PP = 0
PA = 0
w = 8
a = "Na dworze coraz bardziej słonecznie, niedługo trzeba będzie pokazać nogi... "

# Wpisywanie posta

x = ["https://www.facebook.com/StudioFiguraBydgoszczBartodzieje/photos/a.187248642196620/935964000658410/", "Zapraszamy! "]

while w > 0:

    pyg.click(10, 500)

    if pyg.locateOnScreen('SFBot1.jpg', confidence=0.6) is not None:
        a = (pyg.locateOnScreen('SFBot1.jpg', confidence=0.6))[0]
        b = (pyg.locateOnScreen('SFBot1.jpg', confidence=0.6))[1]

    elif pyg.locateOnScreen('oczym.jpg', confidence=0.6) is not None:
        a = (pyg.locateOnScreen('oczym.jpg', confidence=0.6))[0]
        b = (pyg.locateOnScreen('oczym.jpg', confidence=0.6))[1]

    elif pyg.locateOnScreen('NapszCos.jpg', confidence=0.6) is not None:
        a = (pyg.locateOnScreen('NapszCos.jpg', confidence=0.6))[0]
        b = (pyg.locateOnScreen('NapszCos.jpg', confidence=0.6))[1]

    else:
        pyg.hotkey('ctrl', 'tab')
        w -= 1
        continue

    pyg.click(a+10, b+10)
    time.sleep(1)
    pyg.write(x[1])
    pyg.write(x[0])
    time.sleep(2)
    a1 = (pyg.locateOnScreen('SFBot2.jpg', confidence=0.59))[0]
    b1 = (pyg.locateOnScreen('SFBot2.jpg', confidence=0.59))[1]
    pyg.click(a1 + 10, b1 + 10)
    time.sleep(1)
    pyg.hotkey('ctrl', 'tab')
    w -= 1
