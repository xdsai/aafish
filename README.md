# aafish
An archeage autofishing script for windows

## How does it work?
It uses python to get screenshots of a small portion of your screen in quick succession, then uses cv2 magic to detect which action the fish wants you to take.
This only works on 1080p monitors, if you want to make it work on larger/smaller sized screens, you will have to adjust the region + offsets.
This script doesn't handle casting the bait, or picking up the fish.

### How do I use it?
First install python and add it to PATH during the installation (I recommend at least Python 3.8 for this)
Then download this repository either via cloning or as a zip, and open cmd in the newly created folder.
Then, install the requirements via
> python -m pip install -r requirements.txt

Then run it (you might have to run the cmd as admin):
> python fish.py

The script is made so that it detects how many screens you have (in case you want to fish on a screen different from your primary), and it makes you choose one on which it will look for the actions.
Input which screen you're looking to use, this will determine the offset for the screenshot area.
Then when archeage is open, select the window name in the list that pops up. This is so that you don't have to be tabbed on Archeage for the script to send it keystrokes to catch fish - you can do whatever you like in other windows.
Make sure your UI is reset to default (there is an option in the settings) and that you have the correct keybinds for this.

> Stand left - Left arrow

> Stand right - Right arrow

> Big reel in - Up arrow

> Reel in - Down arrow

> Release - "Home" button

After that, you're good to go! Press the "`" key on the keyboard to start the script, and "End" whenever you wish to end it.
