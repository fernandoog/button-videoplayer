import mpv

player = mpv.MPV(ytdl=True)
player.play('test.webm')
player.wait_for_playback()

