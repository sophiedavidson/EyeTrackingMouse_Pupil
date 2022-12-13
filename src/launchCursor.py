# Sophie Davidson, 2022 for IMT Atlantique

# Imports -----------------------------------------------------------------
import pyautogui
import keyboard
from pupilCaptureAccess import *


# Use the eyetracker gaze data to position mouse on the screen.
def startCursor(sub, surfaceName):

    # PyAutoGUI Parameters
    pyautogui.FAILSAFE = False
    pyautogui.PAUSE = 0.01

    # Determine the screen resolution
    (width, height) = pyautogui.size()

    # Until ESC is pressed, use the eye tracker to define mouse position
    loop = True
    while loop:
        if keyboard.is_pressed("esc"):
            break
        (x, y) = getGazePosition(sub, surfaceName)
        if x is not None:
            x = x*width
            y = height - y*height
            pyautogui.moveTo(x, y)
        if keyboard.is_pressed("space"):
            pyautogui.click(x, y)
