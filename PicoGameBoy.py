# PicoGameBoy.py by YouMakeTech
# A class to easily write games for the Raspberry Pi Pico Game Boy
from machine import Pin, PWM, I2C, Timer
from st7789 import ST7789
from framebuf import FrameBuffer, RGB565
import time
import random

class PicoGameBoy(ST7789):
    def __init__(self):
        self.__up = Pin(2, Pin.IN, Pin.PULL_UP)
        self.__down = Pin(3, Pin.IN, Pin.PULL_UP)
        self.__left = Pin(4, Pin.IN, Pin.PULL_UP)
        self.__right = Pin(5, Pin.IN, Pin.PULL_UP)
        self.__button_A = Pin(6, Pin.IN, Pin.PULL_UP)
        self.__button_B = Pin(7, Pin.IN, Pin.PULL_UP)
        self.__buzzer = PWM(Pin(15))
        super().__init__(width=240, height=240, id_=0, sck=18, mosi=19,
                         dc=20, rst=21, cs=17, bl=22, baudrate=62500000)
        
        self.__fb=[] # Array of FrameBuffer objects for sprites
        self.__w=[]
        self.__h=[]
        
    def center_text(self, s, color = 1):
        x = int(self.width/2)- int(len(s)/2 * 8)
        y = int(self.height/2) - 8
        self.text(s, x, y, color)
        
    def top_right_corner_text(self, s, color = 1):
        x = self.width - int(len(s) * 8)
        y = 0
        self.text(s, x, y, color)
        
    def add_sprite(self, buffer, w, h):
        fb = FrameBuffer(buffer, w, h, RGB565)
        self.__fb.append(fb)
        self.__w.append(w)
        self.__h.append(h)
       
    def sprite(self, n, x, y):
        self.blit(self.__fb[n], x, y)
        
    def sprite_width(self,n):
        return self.__w[n]
    
    def sprite_height(self,n):
        return self.__h[n]
        
    def button_up(self):
        return self.__up.value()==0
    
    def button_down(self):
        return self.__down.value()==0
    
    def button_left(self):
        return self.__left.value()==0
    
    def button_right(self):
        return self.__right.value()==0
    
    def button_A(self):
        return self.__button_A.value()==0
    
    def button_B(self):
        return self.__button_B.value()==0
    
    def any_button(self):
        # returns True if any button is pressed
        button_pressed=False
        if self.button_up():
            button_pressed = True
        if self.button_down():
            button_pressed = True
        if self.button_left():
            button_pressed = True
        if self.button_right():
            button_pressed = True
        if self.button_A():
            button_pressed = True
        if self.button_B():
            button_pressed = True
        return button_pressed
    
    def sound(self, freq, duty_u16 = 2000):
        # Make a sound at the selected frequency in Hz
        if freq>0:
            self.__buzzer.freq(freq)
            self.__buzzer.duty_u16(duty_u16)
        else:
            self.__buzzer.duty_u16(0)
   