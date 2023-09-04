from pyautogui import *
import time
import keyboard
from datetime import datetime
import win32gui
import win32con
from screeninfo import get_monitors
import cv2
import numpy as np
import mss

def capture_region_with_offset(region):
    x, y, width, height = region
    with mss.mss() as sct:
        monitor = {"top": y, "left": x, "width": width, "height": height}
        screenshot = sct.grab(monitor)
    return screenshot

def find_image_location(main_image, template_image, method=cv2.TM_CCOEFF_NORMED):
    main_image_gray = cv2.cvtColor(np.array(main_image), cv2.COLOR_BGR2GRAY)
    template_image_gray = cv2.cvtColor(np.array(template_image), cv2.COLOR_BGR2GRAY)

    result = cv2.matchTemplate(main_image_gray, template_image_gray, method)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc

    threshold = 0.7
    if max_val > threshold:
        return top_left
    return None

def get_monitor_offset():
    monitors = get_monitors()
    for i, monitor in enumerate(monitors):
        print(f"Monitor {i+1}: {monitor.name}, Is primary: {monitor.is_primary}, Left: {monitor.x}")
    
    chosen_monitor = int(input("Choose the monitor you want to use (1/2/3/etc.): ")) - 1
    chosen_monitor = monitors[chosen_monitor]
    
    return chosen_monitor.x 

offset = get_monitor_offset()

REGION = (offset + 778, 66, 67, 34)
print(f"Region: {REGION}")

def window_enum_handler(hwnd, resultList):
    window_text = win32gui.GetWindowText(hwnd)
    if "arche" in window_text.lower():
        resultList.append((hwnd, window_text))

windows = []
win32gui.EnumWindows(window_enum_handler, windows)

count = 0
for hwnd, window_text in windows:
    print(f"{count}: Handle: {hwnd}, Text: {window_text}")
    count += 1

chosen_window = int(input("Choose a window: "))
hwnd = windows[chosen_window][0]

START_KEY = '`'
STOP_KEY = 'end'


print(f"Press {START_KEY} to start and hold {STOP_KEY} to close.")
keyboard.wait(START_KEY)
last_skill = None
prev = time.time()
while not keyboard.is_pressed(STOP_KEY):

    nowstamp= datetime.now().time()

    actions = [
        ('images/up_.png', win32con.VK_UP),
        ('images/left_.png', win32con.VK_LEFT),
        ('images/right_.png', win32con.VK_RIGHT),
        ('images/pull_.png', win32con.VK_DOWN),
        ('images/release_.png', win32con.VK_HOME),
    ]
    screenshot = capture_region_with_offset(REGION)
    for image, action in actions:
        template_image = cv2.imread(image)
        point = find_image_location(screenshot, template_image)
        
        if point is not None:
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
