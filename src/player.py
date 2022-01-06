import RPi.GPIO as GPIO
import os
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

os.system("clear")

while True:
    time.sleep(1)
    GPIO.wait_for_edge(10, GPIO.RISING)
    print('play')
    start = time.time()
    time.sleep(0.2)

    while GPIO.input(10) == GPIO.HIGH:
        time.sleep(0.2)
    lenght = time.time() - start

    if lenght > 5:
        time.sleep(0.2)
        os.system("sudo reboot")
    else:
        time.sleep(0.2)
        os.system("mpv video.mp4")
        os.system("clear")
