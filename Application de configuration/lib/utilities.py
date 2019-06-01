import time
import board
import neopixel
import busio
import adafruit_ssd1306

# -------- colors
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
ORANGE = (255, 75, 0)
OFF = (0, 0, 0)


# ---------- notification class
class Notification:
    """Notification class for led and oled screen"""

    def __init__(self, print_data_tuple=False, always_serial_output=False, lcd_width=128, lcd_height=32):
        """setup oled scrren if connected and builtin neopixel"""
        self._width = lcd_width    # width of screen in px
        self._height = lcd_height  # height of screen in px
        self._always_serial_output = always_serial_output  # True if print on serial should be done even if lcd is connected
        self._print_data_tuple = print_data_tuple
        # --builtin led (neopixel for m4)
        self.npx = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.02, auto_write=False)
        # --oled screen
        try:
            # connect to i2c bus
            i2c = busio.I2C(board.SCL, board.SDA)
            # -------- try to read devices (see if oled display is connected)
            # acquire lock
            if i2c.try_lock():
                # i2c scan for devices
                devices = i2c.scan()
                # release lock
                i2c.unlock()
                # check if oled display is connected (address 0x3C)
                if 0x3c in devices:
                    # init oled display
                    self.oled_display = adafruit_ssd1306.SSD1306_I2C(self._width, self._height, i2c)
                else:
                    # otherwise set to None
                    self.oled_display = None
            else:
                # otherwise set to None
                self.oled_display = None
        except RuntimeError:
            # if we can't connect i2c -> nothing is connected
            self.oled_display = None
        if self.oled_display:
            self.led(OFF, startup=True)

    def notify(self, text='', color=OFF):
        self.led(color)
        self.oled_text(text)
        if self._print_data_tuple:
            self.print_data_tuple(text)

    def print_data_tuple(self,text=''):
        import re
        s = '('
        numbers_list = re.findall(r"\d+", text)
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
        self.oled_display.fill(0)
        f = open(filename, 'rb')
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
        f.close()
        self.oled_display.show()

    def show_logo_bin(self):
        # display logo for 1s if oled is connected
        if self.oled_display:
            self.oled_logo('logo.bin')
            time.sleep(1)

    def led(self, color, startup=False):
        if not self.oled_display or startup:
            self.npx.fill(color)
            self.npx.show()

# -------- end
