from pyautogui import *
import time
import keyboard
from datetime import datetime

# Customizable Keybinds
START_KEY = '`'
STOP_KEY = 'end'

CONFIDENCE = 0.60
REGION=(778,66,67,34)

print(f"Press {START_KEY} to start and hold {STOP_KEY} to close.")
keyboard.wait(START_KEY)
last_skill = None
prev = time.time()
while not keyboard.is_pressed(STOP_KEY):
    nowstamp= datetime.now().time()

    # Define a list of images and their associated actions
    actions = [
        ('images/up_.png', 'up'),
        ('images/left_.png', 'left'),
        ('images/right_.png', 'right'),
        ('images/pull_.png', 'down'),
        ('images/release_.png', 'home'),
    ]
    for image, action in actions:
        conf = locateOnScreen(image, grayscale=False, region=REGION, confidence=CONFIDENCE)
        if conf is not None:
            now = time.time()
            if (last_skill != action) or (now - prev > 5 and last_skill == action):
                keyboard.press_and_release(action)
                if action == 'up' or action == 'down':
                    keyboard.press_and_release(action)
                print(nowstamp, f"-> Performed action: {action}, image: {image[7:len(image)-4]}")
                time.sleep(0.1)
                last_skill = action
                prev = now
                break
            