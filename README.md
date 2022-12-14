# EyeTrackingMouse_Pupil
 
 ## About the Project
 
 **Author**: Sophie Davidson     
 **Purpose**:  Generate a gaze controlled mouse cursor using Pupil Capture by Pupil Labs  
 
**Dependencies:** 
- pyglet 
- pyautogui 
- keyboard 
- zmq 
- psutil 
- AppOpener
- msgpack

 
**Requirements:**
- Pupil Capture Application
- Pupil Core Eyetracker with World Camera

        
## How to Install Dependencies


```
py -m pip install pyglet pyautogui keyboard zmq psutil AppOpener msgpack
```

To check that the packages have installed, use 
``` 
py -m pip freeze
```

## Setup
- Ensure that the surface tracker and network API plugins are activated
- Ensure both eye cameras are checked in General Settings
- Define a surface named "surface" in Pupil Capture using 4 x April Tags
- Connect the eyetracker via usb, and run the calibration process."""
