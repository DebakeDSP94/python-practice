import pyautogui
import os
os.chdir('/home/stuart/Documents/automate_online_materials')
pyautogui.screenshot('screenshot_example.png')
# pyautogui.locateOnScreen('calc7key.png') locate image on screen.  need to have an image file in the same directory
# pyautogui.locateCenterOnScreen('calc7key.png')  returns center of image
# pyautogui.moveTo((x, y), duration=num_seconds)  move mouse to x, y coordinates
# pyautogui.click((x, y))  click mouse at x, y coordinates
