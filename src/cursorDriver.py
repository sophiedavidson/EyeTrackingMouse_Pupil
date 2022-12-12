# Sophie Davidson 2022, for IMT Atlantique

"""     The following program will generate a gaze controlled mouse cursor using
        Pupil Capture by Pupil Labs.

        Requirements:
        - Pupil Capture
        - Pupil Core Eyetracker with World Camera


        Setup:
        - Define a surface named "surface" in Pupil Capture using 4 x April Tags
        - Connect the eyetracker via usb, and run the calibration process."""

# Imports ------------------------------------------------------------------
from pupilCaptureAccess import launchConnection, pupilOpen
from launchCursor import startCursor
from GUI import displayMessage


# Main Method --------------------------------------------------------------
def main():
    displayMessage("Eye Controlled Mouse")
    # Check is Pupil Capture is opened, and if not - open it
    pupilOpen()
    # Connect to the Pupil Capture Network API.
    sub = launchConnection()
    surfaceName = "surface"
    # Start the cursor
    startCursor(sub, surfaceName)


if __name__ == "__main__":
    main()
