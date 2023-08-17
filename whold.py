import keyboard
import time

time.sleep(3)
try:
    start_time = time.time()

    while True:
        # Holding down the 'W' key
        if not keyboard.is_pressed('w'):  # Check if 'w' is not already being pressed
            keyboard.press('w')

        # Pressing the 'E' key once every 14 seconds
        elapsed_time = time.time() - start_time
        if elapsed_time >= 14:
            keyboard.press('e')
            keyboard.release('e')
            start_time = time.time()  # Reset the timer

        time.sleep(0.1)  # Sleep for a short while to prevent overwhelming the system

except KeyboardInterrupt:
    # Release the 'W' key when you interrupt the script.
    keyboard.release('w')
