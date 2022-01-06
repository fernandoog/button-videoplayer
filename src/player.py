import mpv

player = mpv.MPV()
player.fullscreen = True
player.play('init.mp4')
player.wait_for_playback()

