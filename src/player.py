import mpv

GPIO.setwarnings(False)  # Ignore warning for now
GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering
GPIO.setup(10, GPIO.IN,
           pull_up_down=GPIO.PUD_DOWN)  # Set pin 10 to be an input pin and set initial value to be pulled low (off)
player = mpv.MPV(ytdl=True)

while True:  # Run forever
    if GPIO.input(10) == GPIO.HIGH:
        player.play('test.webm')
        player.wait_for_playback()
        command = "clear"


