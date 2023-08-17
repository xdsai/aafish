from pyautogui import *
import time
import keyboard
from datetime import datetime

# Customizable Keybinds
START_KEY = '`'
STOP_KEY = 'end'

CONFIDENCE = 0.60
REGION=(830, 64,72, 36)

print(f"Press {START_KEY} to start and hold {STOP_KEY} to close.")
keyboard.wait(START_KEY)
last_skill = None
while not keyboard.is_pressed(STOP_KEY):
    now = datetime.now().time()

    # Define a list of images and their associated actions
    actions = [
        ('images/up.png', 'up'),
        ('images/up2.png', 'up'),
        ('images/left.png', 'left'),
        ('images/left2.png', 'left'),
        ('images/right.png', 'right'),
        ('images/right2.png', 'right'),
        ('images/pull.png', 'down'),
        ('images/pull2.png', 'down'),
        ('images/release.png', 'home'),
        ('images/release2.png', 'home'),
    ]

    for image, action in actions:
        conf = locateOnScreen(image, grayscale=True, region=REGION, confidence=CONFIDENCE)
        if conf is not None:
            if last_skill != action:
                keyboard.press_and_release(action)
                if action == 'up' or action == 'down':  # double press for these actions
                    keyboard.press_and_release(action)
                print(now, f"-> Performed action: {action}, image: {image[7:len(image)-4]}")
                time.sleep(0.1)
                last_skill = action
                break
