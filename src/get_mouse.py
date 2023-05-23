import pyautogui
import os

print (str(pyautogui.position())[5:])

if not os.path.exists('config'):
    os.mkdir('config')
def write_pos(name):
    with open('config/position', 'a', encoding='utf-8')as f:
        pos = pyautogui.position()
        f.write(name + str(pos)[5:] + '\n')
        
write_pos('test')