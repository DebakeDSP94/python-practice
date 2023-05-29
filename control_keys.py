import pyautogui

# type with quarter-second pause in between each key
pyautogui.typewrite('Hello world!\n', interval=0.2)

# slam mouse  to upper-left corner of screen to kill program

pyautogui.press('f1')  # press the F1 key
pyautogui.click(100, 100)
pyautogui.typewrite('Hello world!')  # click the mouse
pyautogui.press('enter')  # press the Enter key
pyautogui.press('esc')  # press the Esc key
pyautogui.keyDown('shift')  # hold down the Shift key
pyautogui.press('left')  # press the left arrow key
pyautogui.keyUp('shift')  # release the Shift key
pyautogui.hotkey('ctrl', 'c')  # press the Ctrl-C hotkey combination
pyautogui.press('volumeup')  # press the volume up button
pyautogui.press('volumemute')  # press the mute volume button
pyautogui.press('volumedown')  # press the volume down button
# press the left key 6 times
pyautogui.press(['left', 'left', 'left', 'left', 'left', 'left'])
pyautogui.keyDown('shift')
