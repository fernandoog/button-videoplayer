import mpv

player = mpv.MPV(ytdl=True, input_default_bindings=True, input_vo_keyboard=True)
player.fullscreen = True
player.play('init.mp4')

