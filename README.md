# Pi-Pico-Game-Boy
Code for the Raspberry Pi Pico Game Boy

* [YouTube video](https://youtu.be/IP3QVGmd_90)
* [Assembly instructions](https://www.youmaketech.com/raspberry-pi-pico-gameboy/)

# How to Use?
- Install MicroPython on the Raspberry Pi Pico
- Copy the files of this repository to the root directory of a Raspberry Pi Pico
- To automatically start a game when the Raspberry Pi Pico is powered on, rename the game (e.g. tetris.py) to main.py

# Available games
- tetris.py: Tetris
- GameOfLife.py: John Conway's Game of Life
- PicoFlappyBird.py: Flappy Bird, my son's favorite game! *** work in progress ***

# Other files
- st7789.py: MicroPython ST7789 OLED driver, SPI interface
- PicoGameBoy.py: A class to easily write games for the Raspberry Pi Pico Game Boy
