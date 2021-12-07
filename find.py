import pyautogui as pyg
import time
import keyboard
import random



PP = 0
w = 11
x = "Tylko 2mln akcji idzie ladnie zarobic przed premiera noiwej gry która jest"
y = "Wystrzeli jak CreepyJar do 1000?"
aut = "Amadiel"
tem = ["Czy Polyslash moze być drugim CreepyJar?",
       "Czy Polyslash moze być drugim CreepyJar?",
       "Czy Polyslash moze być drugim CreepyJar??",
       "Czy Polyslash moze być drugim CreepyJar?!",
       "Czy Polyslash moze być drugim CreepyJar??!",
       "Czy Polyslash moze być drugim Creepyjar",
       "Czy Polyslash moze być drugim Creepyjar?"]

while w > 0:
    pyg.click(0, 500)
    pyg.press('pagedown')
    bb = random.randint(1, 7)
    aa = ''.join(random.sample('!?.??!.', bb))
    pyg.click(1480, 492)
    pyg.click(1480, 500)
    pyg.click(1480, 532)
    pyg.click(1480, 545)
    time.sleep(1)
    pyg.click(1480, 570)
    pyg.click(1480, 590)
    time.sleep(1)
    pyg.write(x, interval=0.01)
    pyg.press('enter')
    pyg.write(y, interval=0.01)
    time.sleep(1)
    pyg.click(635, 362)
    pyg.write(aut, interval=0.01)
    pyg.press('tab')
    pyg.write(tem[PP]+aa, interval=0.01)
    w -= 1
    if PP == 6:
        PP = 0
    PP += 1
    pyg.click(750, 1000)
    time.sleep(3)
    pyg.hotkey('ctrl', 'w')
    time.sleep(1)

