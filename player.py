import mpv
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
player = mpv.MPV(ytdl=True, input_default_bindings=True, input_vo_keyboard=True)
player.fullscreen = True

while True:     

    GPIO.wait_for_edge(4, GPIO.RISING)
    start = time.time()
    time.sleep(0.2)
    
    while GPIO.input(4) == GPIO.HIGH:
        time.sleep(0.1)
    lenght = time.time() - start
    
    if lenght > 5:
        player.play('init.mp4')
    else:
        player.play('test.webm')
