from pyautogui import *
import pyautogui
import keyboard
import time
import win32api, win32con

#X: 563 Y:  400 RGB
#X: 655 Y:  400 RGB
#X: 742 Y:  400 RGB
#X: 839 Y:  400 RGB

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    
    
while keyboard.is_pressed('q') == False:
    
    if pyautogui.pixel(563, 500)[0] == 0:
        click(563, 500)
    if pyautogui.pixel(655, 500)[0] == 0:
        click(655, 500)
    if pyautogui.pixel(742, 500)[0] == 0:
        click(742, 500)
    if pyautogui.pixel(839, 500)[0] == 0:
        click(839, 500)
        
