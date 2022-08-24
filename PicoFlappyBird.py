# PicoFlappyBird.py by Matthieu Mistler
# Flappy Bird game for the Raspberry Pi Pico Game Boy

from PicoGameBoy import PicoGameBoy
import time
from random import randint

# Color scheme
BLACK = PicoGameBoy.color(0,0,0)
WHITE = PicoGameBoy.color(255,255,255)
BACKGROUND_COLOR = PicoGameBoy.color(112,197,206)
TEXT_COLOR = BLACK
TEXT_BACKGROUND_COLOR = WHITE


pgb = PicoGameBoy()

sprite1_34x24=bytearray(b'v9v9v9v9v9v9v9v9v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16Q\xc8Q\xc8\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16Q\xc8Q\xc8\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9v9v9v9v9v9v9v9v9v9v9Q\xc8Q\xc8\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9v9v9v9v9v9v9v9v9Q\xc8Q\xc8\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9v9v9v9v9v9v9Q\xc8Q\xc8\xdf\x16\xdf\x16\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xce\x18\xce\x18\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9v9v9v9v9Q\xc8Q\xc8\xdf\x16\xdf\x16\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xce\x18\xce\x18\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9v9v9Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xce\x18\xce\x18\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9v9v9Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xce\x18\xce\x18\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9v9v9Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xce\x18\xce\x18\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9v9v9Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xce\x18\xce\x18\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88Q\xc8Q\xc8Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88Q\xc8Q\xc8Q\xc8Q\xc8\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16Q\xc8Q\xc8\xe4\x02\xe4\x02\xe4\x02\xe4\x02Q\xc8Q\xc8\xea\x88\xea\x88Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9Q\xc8Q\xc8\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16Q\xc8Q\xc8\xe4\x02\xe4\x02\xe4\x02\xe4\x02Q\xc8Q\xc8\xea\x88\xea\x88Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9Q\xc8Q\xc8\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02Q\xc8Q\xc8\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88Q\xc8Q\xc8v9v9Q\xc8Q\xc8\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02Q\xc8Q\xc8\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9v9v9v9v9v9v9v9v9v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9v9v9v9v9v9v9v9v9v9v9v9v9')

sprite2_34x24=bytearray(b'v9v9v9v9v9v9v9v9v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16Q\xc8Q\xc8\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16Q\xc8Q\xc8\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9v9v9v9v9v9v9v9v9v9v9Q\xc8Q\xc8\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9v9v9v9v9v9v9v9v9Q\xc8Q\xc8\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9v9v9v9v9v9v9Q\xc8Q\xc8\xdf\x16\xdf\x16\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xce\x18\xce\x18\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9v9v9v9v9Q\xc8Q\xc8\xdf\x16\xdf\x16\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xce\x18\xce\x18\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9v9v9Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xce\x18\xce\x18\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9v9v9Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xce\x18\xce\x18\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xce\x18\xce\x18\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xce\x18\xce\x18\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9Q\xc8Q\xc8\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88Q\xc8Q\xc8Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88Q\xc8Q\xc8v9v9Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8\xe4\x02\xe4\x02\xe4\x02\xe4\x02Q\xc8Q\xc8\xea\x88\xea\x88Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8\xe4\x02\xe4\x02\xe4\x02\xe4\x02Q\xc8Q\xc8\xea\x88\xea\x88Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9v9v9v9v9Q\xc8Q\xc8\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02Q\xc8Q\xc8\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88Q\xc8Q\xc8v9v9v9v9v9v9Q\xc8Q\xc8\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02Q\xc8Q\xc8\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88Q\xc8Q\xc8v9v9v9v9v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9v9v9v9v9v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9v9v9v9v9v9v9v9v9v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9v9v9v9v9v9v9v9v9v9v9v9v9')

sprite3_34x24=bytearray(b'v9v9v9v9v9v9v9v9v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16Q\xc8Q\xc8\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16Q\xc8Q\xc8\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9v9v9v9v9v9v9v9v9v9v9Q\xc8Q\xc8\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9v9v9v9v9v9v9v9v9Q\xc8Q\xc8\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xce\x18\xce\x18\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xce\x18\xce\x18\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xce\x18\xce\x18\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xce\x18\xce\x18\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xce\x18\xce\x18\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xce\x18\xce\x18\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfb\xef\xfbQ\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xdf\x16\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88Q\xc8Q\xc8v9v9Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4\xd5\xe4Q\xc8Q\xc8\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88Q\xc8Q\xc8v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02Q\xc8Q\xc8\xea\x88\xea\x88Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02Q\xc8Q\xc8\xea\x88\xea\x88Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9v9v9v9v9Q\xc8Q\xc8\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02Q\xc8Q\xc8\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88Q\xc8Q\xc8v9v9v9v9v9v9Q\xc8Q\xc8\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02Q\xc8Q\xc8\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88\xea\x88Q\xc8Q\xc8v9v9v9v9v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9v9v9v9v9v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02\xe4\x02Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9v9v9v9v9v9v9v9v9v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9v9Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9v9v9v9v9v9v9v9v9v9v9v9v9v9')

pipe_26x26=bytearray(b'v9Q\xc8\x9f+\xe7\xf1\x9f+\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8v9v9Q\xc8\x9f+\xe7\xf1\x9f+\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8v9v9Q\xc8\x9f+\xe7\xf1\x9f+\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8v9v9Q\xc8\x9f+\xe7\xf1\x9f+\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8v9v9Q\xc8\x9f+\xe7\xf1\x9f+\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8v9v9Q\xc8\x9f+\xe7\xf1\x9f+\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8v9v9Q\xc8\x9f+\xe7\xf1\x9f+\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8v9v9Q\xc8\x9f+\xe7\xf1\x9f+\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8v9v9Q\xc8\x9f+\xe7\xf1\x9f+\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8v9v9Q\xc8\x9f+\xe7\xf1\x9f+\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8v9v9Q\xc8\x9f+\xe7\xf1\x9f+\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8v9v9Q\xc8\x9f+\xe7\xf1\x9f+\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8v9v9Q\xc8\x9f+\xe7\xf1\x9f+\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8v9v9Q\xc8\x9f+\xe7\xf1\x9f+\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8v9v9Q\xc8\x9f+\xe7\xf1\x9f+\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8v9v9Q\xc8\x9f+\xe7\xf1\x9f+\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8v9v9Q\xc8\x9f+\xe7\xf1\x9f+\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8v9v9Q\xc8\x9f+\xe7\xf1\x9f+\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8v9v9Q\xc8\x9f+\xe7\xf1\x9f+\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8v9v9Q\xc8\x9f+\xe7\xf1\x9f+\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8v9v9Q\xc8\x9f+\xe7\xf1\x9f+\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8v9v9Q\xc8\x9f+\xe7\xf1\x9f+\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8v9v9Q\xc8\x9f+\xe7\xf1\x9f+\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8v9v9Q\xc8\x9f+\xe7\xf1\x9f+\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8v9v9Q\xc8\x9f+\xe7\xf1\x9f+\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8v9v9Q\xc8\x9f+\xe7\xf1\x9f+\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8v9')

pipe_bot_26x26=bytearray(b'v9Q\xc8\x9f+\xe7\xf1\x9f+\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8v9v9Q\xc8\x9f+\xe7\xf1\x9f+\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8v9v9Q\xc8\x9f+\xe7\xf1\x9f+\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8v9v9Q\xc8\x9f+\xe7\xf1\x9f+\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8v9v9Q\xc8\x9f+\xe7\xf1\x9f+\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8v9v9Q\xc8\x9f+\xe7\xf1\x9f+\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8v9v9Q\xc8\x9f+\xe7\xf1\x9f+\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8v9v9Q\xc8\x9f+\xe7\xf1\x9f+\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8v9v9Q\xc8\x9f+\xe7\xf1\x9f+\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8v9v9Q\xc8\x9f+\xe7\xf1\x9f+\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8v9v9Q\xc8\x9f+\xe7\xf1\x9f+\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8v9v9Q\xc8\x9f+\xe7\xf1\x9f+\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8v9v9Q\xc8\x9f+\xe7\xf1\x9f+\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8v9v9Q\xc8\x9f+\xe7\xf1\x9f+\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8v9Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04Q\xc8Q\xc8\x9f+\xe7\xf1\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8Q\xc8\x9f+\xe7\xf1\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8Q\xc8\x9f+\xe7\xf1\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8Q\xc8\x9f+\xe7\xf1\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8Q\xc8\x9f+\xe7\xf1\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8Q\xc8\x9f+\xe7\xf1\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8Q\xc8\x9f+\xe7\xf1\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8Q\xc8\x9f+\xe7\xf1\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8Q\xc8u\xe5\x9f+\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\x9f+\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5T\x04Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8')

pipe_top_26x26=bytearray(b'Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8u\xe5\x9f+\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\xe7\xf1\x9f+\xe7\xf1\x9f+\x9f+\x9f+\x9f+\x9f+\x9f+u\xe5T\x04Q\xc8Q\xc8\x9f+\xe7\xf1\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8Q\xc8\x9f+\xe7\xf1\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8Q\xc8\x9f+\xe7\xf1\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8Q\xc8\x9f+\xe7\xf1\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8Q\xc8\x9f+\xe7\xf1\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8Q\xc8\x9f+\xe7\xf1\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8Q\xc8\x9f+\xe7\xf1\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8Q\xc8\x9f+\xe7\xf1\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8Q\xc8T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04T\x04Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8Q\xc8v9Q\xc8\x9f+\xe7\xf1\x9f+\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8v9v9Q\xc8\x9f+\xe7\xf1\x9f+\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8v9v9Q\xc8\x9f+\xe7\xf1\x9f+\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8v9v9Q\xc8\x9f+\xe7\xf1\x9f+\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8v9v9Q\xc8\x9f+\xe7\xf1\x9f+\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8v9v9Q\xc8\x9f+\xe7\xf1\x9f+\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8v9v9Q\xc8\x9f+\xe7\xf1\x9f+\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8v9v9Q\xc8\x9f+\xe7\xf1\x9f+\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8v9v9Q\xc8\x9f+\xe7\xf1\x9f+\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8v9v9Q\xc8\x9f+\xe7\xf1\x9f+\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8v9v9Q\xc8\x9f+\xe7\xf1\x9f+\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8v9v9Q\xc8\x9f+\xe7\xf1\x9f+\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8v9v9Q\xc8\x9f+\xe7\xf1\x9f+\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8v9v9Q\xc8\x9f+\xe7\xf1\x9f+\x9f+\x9f+u\xe5\x9f+u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5u\xe5T\x04u\xe5T\x04T\x04Q\xc8v9')

pgb.add_sprite(sprite1_34x24,34,24) # sprite #0
pgb.add_sprite(sprite2_34x24,34,24) # sprite #1
pgb.add_sprite(sprite3_34x24,34,24) # sprite #2
pgb.add_sprite(pipe_26x26,26,26) # sprite #3
pgb.add_sprite(pipe_bot_26x26,26,26) # sprite #4
pgb.add_sprite(pipe_top_26x26,26,26) # sprite #5

x = 0.0
y = 0.0
vy = 0.0
sprite = 0
button_pressed = False
prev_button_pressed = False
frame_counter = 0

# game loop
while True:
    frame_counter = frame_counter + 1
    if frame_counter > 10:
        frame_counter = 0
        sprite = sprite + 1
        if sprite>2:
            sprite = 0
    
    vy = vy + 0.05
    y = y + vy
    
    if y<0:
        y = 0
        
    if y>239:
        y = 239
         
    prev_button_pressed = button_pressed
    if pgb.button_A() or pgb.button_B():
        button_pressed = True
    else:
        button_pressed = False
        
    if prev_button_pressed==False and button_pressed==True:
        vy = -2.0
    
    
    pgb.fill(BACKGROUND_COLOR)
    pgb.sprite(sprite, int(x), int(y))
    pgb.show()

