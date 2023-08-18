import time
import random
from pynput.keyboard import Controller, Key

keyboard = Controller()

while True:
    # Sleep for a random interval between 10 to 20 seconds
    time_to_sleep = random.uniform(10, 20)
    print(f"Sleeping for {time_to_sleep} seconds")
    time.sleep(time_to_sleep)
    
    keyboard.press('t')
    keyboard.release('t')
