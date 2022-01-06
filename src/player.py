import mpv
import RPi.GPIO as GPIO
import os
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
os.system("clear")

while True:  # Run forever
    time.sleep(2)
    if GPIO.input(10) == GPIO.HIGH:
        player = mpv.MPV(ytdl=True)
        player.play('test.webm')
        player.wait_for_playback()
        del player
        os.system("clear")


