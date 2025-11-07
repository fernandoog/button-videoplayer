# Button Video Player

A simple video player for Raspberry Pi controlled by a physical button connected via GPIO.

## Description

This project implements a video player that runs on Raspberry Pi and is controlled by a physical push button. The player uses GPIO pin 10 to detect button presses and plays a video file when the button is pressed. A long press (more than 5 seconds) will reboot the Raspberry Pi.

## Features

- Physical button control via GPIO
- Video playback using MPV player
- Long press detection for system reboot
- Simple and lightweight implementation

## Requirements

- Raspberry Pi (any model with GPIO)
- Python 3
- Physical push button
- Jumper wires for GPIO connection

## Installation

1. Install system dependencies:
```bash
sudo apt install python3-mpv python3-tk
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Connect a push button to GPIO pin 10 (physical pin 19) and GND

## Usage

1. Place your video file as `video.mp4` in the `src/` directory
2. Run the player:
```bash
python3 src/player.py
```

3. Press the button to play the video
4. Long press (5+ seconds) to reboot the system

## Project Structure

```
button-videoplayer/
├── src/
│   ├── player.py          # Main player script
│   └── video.mp4          # Video file to play
├── ejemplos/              # Example scripts
├── doc/                   # Documentation
├── requirements.txt       # Python dependencies
└── README.md
```

## Hardware Setup

Connect a push button between:
- GPIO pin 10 (physical pin 19) 
- GND (any ground pin)

The button uses a pull-down resistor configuration.

## Author

Fernando Ortega Gorrita (@fernandoog)

## License

See LICENSE file for details.
