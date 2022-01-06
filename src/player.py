import mpv
import RPi.GPIO as GPIO
import os
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
def my_log(loglevel, component, message):
    print('[{}] {}: {}'.format(loglevel, component, message))
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
        player = mpv.MPV(log_handler=my_log, ytdl=True, input_default_bindings=True, input_vo_keyboard=True)
        player.play('video.mp4')
        player.wait_for_playback()
        del player
        os.system("clear")


