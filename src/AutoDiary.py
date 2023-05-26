import os
import pyautogui
import win32gui
import pyperclip
import random
import time

no_wants = ('药剂','冷却','元素伤害','总回复速度')

def r():
    return random.uniform(0.01, 0.03)

def autowash(val):
    last_paste = None
    os.system('echo off | clip')
    pyautogui.hotkey('ctrl','c',interval=r())
    while last_paste==pyperclip.paste():
        last_paste = pyperclip.paste()
        pyautogui.click(button='left')
        time.sleep(r())
        pyautogui.hotkey('ctrl','c',interval=r())
        time.sleep(r())
        