import mpv
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
player = mpv.MPV(ytdl=True)

while True:  # Run forever
    if GPIO.input(10) == GPIO.HIGH:
        player.play('test.webm')
        player.wait_for_playback()
        command = "clear"


