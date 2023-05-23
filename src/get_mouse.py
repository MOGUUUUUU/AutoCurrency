import pyautogui
import os

print (str(pyautogui.position())[5:])

    
def write_pos(name):
    if not os.path.exists('config'):
        os.mkdir('config')
    with open('config/position', 'a', encoding='utf-8')as f:
        pos = pyautogui.position()
        f.write(name + str(pos)[5:] + '\n')
        
