import pyautogui

print(pyautogui.size())
width, height = pyautogui.size()
print(pyautogui.position())
# move mouse to 10, 10 over 1.5 seconds. Duration is optional
pyautogui.moveTo(10, 10, duration=1.5)
# move mouse relative to its current position
pyautogui.moveRel(200, 0, duration=2)
pyautogui.moveRel(0, 100, duration=1)

pyautogui.click(339, 38)

# double click the mouse coordinates are optional
pyautogui.doubleClick(339, 38)

pyautogui.rightClick(339, 38)  # right click the mouse coordinates are optional

# middle click the mouse coordinates are optional
pyautogui.middleClick(339, 38)

pyautogui.dragTo(339, 38, duration=2)  # drag mouse to coordinates

# drag mouse relative to current position
pyautogui.dragRel(200, 0, duration=2)

pyautogui.scroll(200)  # scroll up 200 pixels

pyautogui.scroll(-200)  # scroll down 200 pixels

# scroll up 200 pixels at coordinates 100, 100
pyautogui.scroll(200, x=100, y=100)

# scroll down 200 pixels at coordinates 100, 100
pyautogui.scroll(-200, x=100, y=100)
