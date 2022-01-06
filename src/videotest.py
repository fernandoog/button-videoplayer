import mpv

player = mpv.MPV(ytdl=True)
player.play('video.mp4')
player.wait_for_playback()
