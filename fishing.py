from pyautogui import *
import time
import keyboard
import ctypes
import sys
from datetime import datetime

# Customizable Keybinds
START_KEY = '`'
STOP_KEY = 'end'

CONFIDENCE = 0.4


print("Move your mouse to the top left corner of the desired region and press ENTER.")
keyboard.wait('enter')
x1, y1 = pyautogui.position()

print("Move your mouse to the bottom right corner of the desired region and press ENTER.")
keyboard.wait('enter')
x2, y2 = pyautogui.position()

REGION = (x1, y1, x2 - x1, y2 - y1)  # (x, y, width, height)

print(f"Press {START_KEY} to start and hold {STOP_KEY} to close.")
keyboard.wait(START_KEY)
last_skill = None
while not keyboard.is_pressed(STOP_KEY):
    now = datetime.now().time()

    # Define a list of images and their associated actions
    actions = [
        ('images/up.png', 'num8'),
        ('images/left.png', 'num4'),
        ('images/right.png', 'num6'),
        ('images/pull.png', 'num2'),
        ('images/release.png', 'num5'),
        ('images/target.png', 'waiting')
    ]

    for image, action in actions:
        if pyautogui.locateOnScreen(image, region=REGION, confidence=CONFIDENCE) is not None:
            if last_skill != action:
                if action == 'waiting':
                    print(now, "-> Waiting for skill")
                else:
                    keyboard.press_and_release(action)
                    if action == 'up' or action == 'down':  # double press for these actions
                        keyboard.press_and_release(action)
                    print(now, f"-> Performed action: {action}")
                last_skill = action
                break
    else:
        print(now, "-> Waiting for fish target")
        last_skill = None
        time.sleep(0.01)
