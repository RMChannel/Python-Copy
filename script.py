import pyautogui
import time
time.sleep(5)
with open('copy.txt', 'r') as file:
    for linea in file:
        pyautogui.typewrite(linea)