import RPi.GPIO as GPIO
import time
import os
import subprocess
from subprocess import Popen

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

img = Popen(['cvlc', '-f', '--loop', '--no-video-title-show', '--no-audio', 'black.png'])

while True:
    GPIO.wait_for_edge(4, GPIO.RISING)
    print('pressed')
    start = time.time()
    time.sleep(0.2)

    while GPIO.input(4) == GPIO.HIGH:
        time.sleep(0.1)
    lenght = time.time() - start

    if lenght > 5:
        print('long press, exit')
        command = "sudo killall -s 9 omxplayer.bin"
        os.system(command)
    else:
        print('short press, play video')
        omxp = Popen(['omxplayer', '-s', '-o', 'hdmi', '2nightflightFinalfinal.mp4'])
