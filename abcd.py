from pyautogui import *
import time
import keyboard
from datetime import datetime
import win32gui
import win32con

def window_enum_handler(hwnd, resultList):
    '''Pass to win32gui.EnumWindows() to generate list of window handle,
    window text tuples.'''
    window_text = win32gui.GetWindowText(hwnd)
    if "arche" in window_text.lower():  # substring check; make it case insensitive
        resultList.append((hwnd, window_text))

windows = []
win32gui.EnumWindows(window_enum_handler, windows)

count = 0
for hwnd, window_text in windows:
    print(f"{count}: Handle: {hwnd}, Text: {window_text}")
    count += 1

chosen_window = int(input("Choose a window: "))
hwnd = windows[chosen_window][0]

    # Uncomment the line below to send a "W" key to each matching window
    # win32gui.SendMessage(hwnd, win32con.WM_CHAR, ord('W'), 0)


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
        ('images/up_.png', win32con.VK_UP),
        ('images/left_.png', win32con.VK_LEFT),
        ('images/right_.png', win32con.VK_RIGHT),
        ('images/pull_.png', win32con.VK_DOWN),
        ('images/release_.png', win32con.VK_HOME),
    ]

    for image, action in actions:
        conf = locateOnScreen(image, grayscale=False, region=REGION, confidence=CONFIDENCE)
        if conf is not None:
            now = time.time()
            if (last_skill != action) or (now - prev > 5 and last_skill == action):
                win32gui.SendMessage(hwnd, win32con.WM_KEYDOWN, action, 0)
                win32gui.SendMessage(hwnd, win32con.WM_KEYUP, action, 0)
                if action == 'up' or action == 'down':
                    win32gui.SendMessage(hwnd, win32con.WM_KEYDOWN, action, 0)
                    win32gui.SendMessage(hwnd, win32con.WM_KEYUP, action, 0)
                print(nowstamp, f"-> Performed action: {action}, image: {image[7:len(image)-4]}")
                time.sleep(0.1)
                last_skill = action
                prev = now
                break
            
