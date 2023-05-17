import win32gui
import pyautogui
import random
import time

#Start_Point(x=1274, y=592)
#End_Point(x=1899, y=845)
#avrx=52,avry=50

def putting():
    xpos, ypos = 1294,614
    pyautogui.keyDown('ctrl')
    while xpos < 1899:
        while ypos < 845:
            pyautogui.moveTo(xpos+random.randint(-5,5),ypos+random.randint(-5,5))
            pyautogui.click(button='left')
            ypos += 50
        xpos += 52
        ypos = 614
    pyautogui.keyUp('ctrl')

if __name__ == '__main__':
    hld = win32gui.FindWindow(None,u"Path of Exile")
    win32gui.SetForegroundWindow(hld)
    putting()