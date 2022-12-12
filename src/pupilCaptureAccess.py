# Sophie Davidson, 2022  for IMT Atlantique

# Imports --------------------------------------------------------------------------------------------
import zmq
import psutil
from AppOpener import run
from msgpack import loads
from GUI import displayMessage


# Connect to the Network API using the predefined ports and address
def launchConnection():
    context = zmq.Context()
    # open a req port to talk to pupil
    address = "127.0.0.1"  # remote ip or localhost
    req_port = "50020"  # Check in Pupil Capture Network API settings
    req = context.socket(zmq.REQ)
    req.connect("tcp://{}:{}".format(address, req_port))
    # ask for the sub port
    req.send_string("SUB_PORT")
    sub_port = req.recv_string()

    # open a sub port to listen to pupil
    sub = context.socket(zmq.SUB)
    sub.connect("tcp://{}:{}".format(address, sub_port))
    sub.setsockopt_string(zmq.SUBSCRIBE, "surface")

    return sub


# Get the most recent gaze position, and return as (x,y)
def getGazePosition(sub, surfaceName):
    norm_gp_x = 0
    norm_gp_y = 0

    try:
        topic = sub.recv_string()
        msg = sub.recv()  # bytes
        surfaces = loads(msg, raw=False)
        filtered_surface = {
            k: v for k, v in surfaces.items() if surfaces["name"] == surfaceName
        }
        try:
            # note that we may have more than one gaze position data point (this is expected behavior)
            gaze_positions = filtered_surface["gaze_on_surfaces"]
            for gaze_pos in gaze_positions:
                norm_gp_x, norm_gp_y = gaze_pos["norm_pos"]

        except:
            displayMessage("No Gaze Data Found: Ensure a surface is defined 1 ")

    except:
        displayMessage("No Gaze Data Found: Ensure a surface is defined ")

    return norm_gp_x, norm_gp_y


# Check if Pupil Capture is open, if not, open it
def pupilOpen():
    connected = False
    while not connected:
        connected = "pupil_capture.exe" in (i.name() for i in psutil.process_iter())
        if not connected:
            run("pupil capture v")
