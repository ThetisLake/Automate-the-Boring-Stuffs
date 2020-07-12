# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 23:56:55 2020

@author: erich
"""

import pyautogui

# Return size of the display
size = pyautogui.size()
print(size)

# Assign width and height to variables
width, height = size
print('size is '+str(width)+'x'+str(height))
print('width is '+str(width))
print('height is '+str(height))

#MOUSE
# Return mouse position
currentPosition = pyautogui.position()
print(currentPosition)

# Move mouse position to absolute location
pyautogui.moveTo(10,10, duration=1)

# Move mouse position to relative location
pyautogui.moveRel(900,900, duration=1)

# Click on a specific location
pyautogui.click(174,1010)

#KEYBOARD
# typewrite using pyautogui
pyautogui.typewrite(['winleft','winleft'], interval=1)

# Keys that can be used to return all the keyboard keys that can be placed in typewrite
print(pyautogui.KEYBOARD_KEYS)

# Also can use pyautogui.dragRel, pyautogui.drag
# We can quickly force the mouse to the left top corner (0,0) position to 
# Force kill the code