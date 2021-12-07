from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con


tile1 = 587
tile2 = 680
tile3 = 773
tile4 = 875
tiley = 380

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.02)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

while keyboard.is_pressed('q') == False:

    if pyautogui.pixel(tile1, tiley)[0] == 255:
        click(tile1, tiley+2)

    if pyautogui.pixel(tile2, tiley)[0] == 0:
        click(tile2, tiley+2)

    if pyautogui.pixel(tile3, tiley)[0] == 0:
        click(tile3, tiley+2)

    if pyautogui.pixel(tile4, tiley)[0] == 0:
        click(tile4, tiley+2)