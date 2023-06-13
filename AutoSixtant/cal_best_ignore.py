import win32gui
import pyautogui
import pyperclip
import random
import time


sixtant_value = {}

with open('sixtant_value.txt', 'a', encoding='utf-8')as f:
    for line in f:
        if ':' not in line:
            continue
        sixtant = line.split(':')[0]
        value = line.split(':')[1]
        sixtant_value['sixtant'] = value
        

        