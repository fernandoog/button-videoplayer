import mpv
import RPi.GPIO as GPIO
import os
import time
import tkinter as tk

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
os.system("clear")

while True:

    GPIO.wait_for_edge(10, GPIO.RISING)
    print('play')
    start = time.time()
    time.sleep(0.2)

    while GPIO.input(10) == GPIO.HIGH:
        time.sleep(0.1)
    lenght = time.time() - start

    if lenght > 5:
        os.system("sudo reboot")
    else:
        root = tk.Tk()
        player = mpv.MPV()
        player.play('video.mp4')
        player.wait_for_playback()
        del player
        tk.mainloop()
        os.system("clear")


