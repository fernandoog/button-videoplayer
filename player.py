import mpv
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
player = mpv.MPV(ytdl=True, input_default_bindings=True, input_vo_keyboard=True)
player.fullscreen = True
player.play('init.mp4')

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
        player.play('init.mp4')
    else:
        print('short press, play video')
        player['loop'] = 'inf'
        player.play('test.webm')
