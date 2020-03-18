# ------------------------------------
# Utilities : utilities.py
# Classes to help interaction with M4 express and oled feather wing
# Olivier Boesch (c) 2019
# Licence : MIT
# ------------------------------------
#---- imports
# for everything
import board
# for notifications
import neopixel
import busio
import adafruit_ssd1306
# for buttons
from digitalio import DigitalInOut, Direction, Pull
# for audio
from audioio import AudioOut, WaveFile, RawSample
import array
import math
import time

# -------- colors
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
ORANGE = (255, 75, 0)
WHITE = (255,255,255)
OFF = (0, 0, 0)


# ---------- notification class
class Notification:
    """Notification class for led and oled screen"""
    def __init__(self, always_serial_output=False, always_led_on=False, led_brightness=0.1, print_data_tuple=False, lcd_width=128, lcd_height=32):
        """setup oled scrren if connected and builtin neopixel"""
        self._width = lcd_width    # width of screen in px
        self._height = lcd_height  # height of screen in px
        self._always_serial_output = always_serial_output  # True if print on serial should be done even if lcd is connected
        self._print_data_tuple = print_data_tuple
        self._always_led_on = always_led_on
        self._led_brightness = led_brightness
        # --builtin led (neopixel for m4)
        self.npx = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=self._led_brightness, auto_write=False)
        # --oled screen
        try:
            # connect to i2c bus
            self.i2c = busio.I2C(board.SCL, board.SDA)
            # -------- try to read devices (see if oled display is connected)
            # try to acquire i2c lock
            while not self.i2c.try_lock():
                pass
            # i2c scan for devices
            devices = self.i2c.scan()
            # release lock
            self.i2c.unlock()
            # check if oled display is connected (address 0x3C)
            if 0x3c in devices:
                # init oled display
                self.oled_display = adafruit_ssd1306.SSD1306_I2C(self._width, self._height, self.i2c)
            else:
                del self.i2c
                self.i2c = None
                # otherwise set to None
                self.oled_display = None
        except RuntimeError:
            # if we can't connect i2c -> nothing is connected
            self.oled_display = None
        if self.oled_display and not self._always_led_on:
            self.led(OFF, startup=True)

    def get_i2c(self):
        return self.i2c

    def intro(self):
        self.led(color=BLUE)
        self.oled_logo('media/logo_mep.bin')
        time.sleep(1)

    def notify(self, text='', color=OFF):
        self.oled_text(text)
        if self._print_data_tuple:
            self.print_data_tuple(text)
        self.led(color)

    def print_data_tuple(self,text=''):
        import re
        s = '('
        regexobj = re.compile(r"[-+]?\d*\.\d+|\d+")
        numbers_list = regexp.split(text)
        for number in numbers_list:
            s += str(number) + ','
        print(s[:-1] + ')')

    def oled_text(self, text='', invert=False):
        """display max 3 lines of text on oled display (separated by \\n)"""
        if not self.oled_display:
            # if no oled_display -> print to serial (newlines to tabs)
            print(text.replace('\n', '\t'))
            return
        lines = text.split('\n')
        self.oled_display.fill(0)
        i = 0
        for l in lines:
            self.oled_display.text(l, 0, i, 1)
            i += 10
        if invert:
            self.oled_display.invert()
        self.oled_display.show()
        if self._always_serial_output:
            print(text.replace('\n', '\t'))  # print to serial (newlines to tabs)

    def oled_bar(self, percent=0.0):
        """display an horizontal bar on oled display; percent = 0-100%"""
        # draw only if oled_display is running
        if self.oled_display:
            # constrain percent
            if percent > 100.0:
                percent = 100
            elif percent < 0.0:
                percent = 0
            # cal size for percent
            barwidth = int((percent * (self._width - 31)) / 100.0)
            # reset oled to black
            self.oled_display.fill(0)
            # draw bounds( width minus 21px for 4 characters)
            for i in range(self._width - 30):
                # draw upper bound
                self.oled_display.pixel(i, self._height // 2 - 2, 1)
                # draw lower bound
                self.oled_display.pixel(i, self._height // 2 + 2 - 1, 1)
            for i in range(self._height // 2 - 2, self._height // 2 + 2):
                # draw left bound
                self.oled_display.pixel(0, i, 1)
                # draw right bound
                self.oled_display.pixel(self._width - 31, i, 1)
            # fill bar
            for i in range(0, barwidth):
                for j in range(self._height // 2 - 1, self._height // 2 + 2):
                    self.oled_display.pixel(i, j, 1)
            # show text
            self.oled_display.text('{: >3d}%'.format(int(percent)), self._width - 25, self._height // 2 - 4, 1)
            # send to device
            self.oled_display.show()
            if self._always_serial_output:
                print('progress : ', percent)

    def oled_logo(self, filename):
        if self.oled_display:
            # try to open file and display it
            try:
                # open file
                f = open(filename, 'rb')
                # empty display (fill with black)
                self.oled_display.fill(0)
                # draw the file (1bit/px raw)
                x = 0
                y = 0
                for i in range((self._width * self._height) // 8):
                    c = f.read(1)
                    ci = int.from_bytes(c, 'little')
                    for j in range(8):
                        if ci & (1 << j) > 0:
                            self.oled_display.pixel(x, y, 1)
                        x += 1
                    if ((i + 1) * 8) % self._width == 0:
                        x = 0
                        y += 1
                # close file
                f.close()
                # send image to display
                self.oled_display.show()
                # tell if user asked to print to serial
                if self._always_serial_output:
                    print("logo displayed :", filename)
            # display an error if we can't open file
            except OSError as e:
                print("Erreur (", filename, "):", e)

    def led(self, color, startup=False):
        if not self.oled_display or startup or self._always_led_on:
            self.npx.fill(color)
            self.npx.show()


class Button:
    """Button: helper class to manage button"""
    def __init__(self, pin, name="", reverse=False):
        self._btn = DigitalInOut(pin)
        self._btn.direction = Direction.INPUT
        self._btn.pull = Pull.UP
        self._state = False
        self._reverse = reverse
        self._name = name

    def check(self):
        """check: update state of button"""
        self._state = self._btn.value
        return self.is_pushed()

    def is_pushed(self):
        """is_pushed: returns True if button is pushed( or not if reverse==True)"""
        if self._reverse:
            return not self._state
        else:
            return self._state

    def __repr__(self):
        """print button state"""
        return 'Button ' + self._name + '('+str(self.is_pushed())+')'


class SoundFile:
    """SoundFile: Helper class to play wav sound file (16kHz and 16bits max) on A0,A1
        paraleters:
            filename: name of the wav file"""
    def __init__(self, filename):
        self.data = open(filename,'rb')
        self.sound = WaveFile(self.data)
        # if the wav file is stereo then open in stereo otherwise open in mono
        if self.sound.channel_count == 2 :
            self.audiodevice = AudioOut(board.A0, right_channel=board.A1)
        else:
            self.audiodevice = AudioOut(board.A0)
        # exposing AudioOut functions
        self.stop = self.audiodevice.stop
        self.pause = self.audiodevice.pause
        self.resume = self.audiodevice.resume


    def play(self):
        self.audiodevice.play(self.sound)

    def playing(self):
        return self.audiodevice.playing

    def paused(self):
        return self.audiodevice.paused

    def __del__(self):
        self.data.close()


class SoundGenerator:
    """SoundGenerator: Helper class to create a sinusoidal sample of a given frequency and play it on A0 or A0,A1
        parameters:
            frequency: frequency of the sample
            sampling_frequency: sampling frequency of the device (max 22kHz - 22050)
            stereo: should the sample created and played in stereo (A0,A1) or mono (A0 only) """
    def __init__(self, frequency=440, sampling_frequency=16000, stereo=False):
        length = sampling_frequency // frequency
        if stereo:
            length *= 2
        self.sine_wave = array.array("H", [0] * length)
        if stereo:
            j=0
            for i in range(0,length,2):
                self.sine_wave[i] = int(math.sin(math.pi * 2 * j / (length/2)) * (2 ** 15 - 1) + 2 ** 15)
                self.sine_wave[i+1] = self.sine_wave[i]
                j += 1
        else:
            for i in range(length):
                self.sine_wave[i] = int(math.sin(math.pi * 2 * i / length) * (2 ** 15 - 1) + 2 ** 15)
        if stereo:
            self.audiodevice = AudioOut(board.A1, right_channel=board.A0)
        else:
            self.audiodevice = AudioOut(board.A0)
        self.sine_wave = RawSample(self.sine_wave, channel_count=2 if stereo else 1 , sample_rate=sampling_frequency)
        # exposing AudioOut functions
        self.stop = self.audiodevice.stop
        self.pause = self.audiodevice.pause
        self.resume = self.audiodevice.resume

    def play(self):
        """play: plays the generated sound"""
        self.audiodevice.play(self.sine_wave, loop=True)

    def bip(self, length=0.05):
        """bip: plays a bip of the given frequency
            parameters:
                length: length of bip in seconds (default: 50ms)"""
        self.play()
        time.sleep(length)
        self.stop()

    def playing(self):
        """playing: returns True if the generated sound is playing"""
        return self.audiodevice.playing

    def paused(self):
        """paused: returns True if the generated sound is paused"""
        return self.audiodevice.paused


# -------- end