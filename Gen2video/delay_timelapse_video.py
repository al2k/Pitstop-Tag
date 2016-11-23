#!/usr/bin/python
# Pitstop Gen 2 open Sea Turtle Tag | v1.01 
# Enables delayed startup timelapse video recording using the Pitstop Gen 2 enclosure with optical lens.

# Suitable for use on the Raspberry Pi Zero
# See README.md for more information & payload pre-requisites
# Ensure you run sudo apt-get update and then sudo apt-get dist-upgrade to confirm you have the latest firmware

import picamera
from os import system
import time

# Set the resolution of the video you intend to capture.
camera = picamera.PiCamera(resolution=(1920, 1080))

print "Starting up!"
time.sleep(18000)
print "Waiting 18000 seconds (5 hours)"
# Change the time.sleep value to delay the startup. I have set 5 hours by default so the tag can be turned 
# on, closed and transported to the beach. The trip is 45 mins in my case, followed by ~ 1 hour scouting for a 
# suitable turtle, then possibly up to 1 hour waiting for the turtle to start laying her clutch. 
# The tag would begin recording on the 5th hour.

x = 1
y = 1
while True:
     print "Taking a video. This is video %d " % (x)
     camera.start_recording('%d.h264' % y)
     camera.wait_recording(120)
	 # Record for 2 mins
     camera.stop_recording()
     print "Sleeping for 10 seconds before recording again"
     time.sleep(1800)
	 # Waiting for 30 mins before continuing
     y += 1
     print "Done. Preparing to record next video."
     x += 1

