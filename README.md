# AFL LED Scoreboard for Raspberry Pi Zero

A lightweight AFL scoreboard for 64x32 RGB LED Matrix using the free Squiggle API.

Displays live/upcoming games in classic **goals.behinds (points)** format with team colors.

## Features
- Live scores, quarters, and status
- Team colors and short names
- Auto refresh
- Optimized for Pi Zero + 64x32 panel

## Hardware Required
- Raspberry Pi Zero (2W preferred)
- 64x32 HUB75 RGB LED Matrix
- 5V power supply (≥3A recommended)

## Setup

1. Install the RGB Matrix library first:
   ```bash
   git clone --recursive https://github.com/hzeller/rpi-rgb-led-matrix.git
   # Follow the official installation instructions
