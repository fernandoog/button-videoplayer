import mpv

player = mpv.MPV(ytdl=True)
player.play('vid/test.webm')
player.wait_for_playback()
