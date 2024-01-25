import socket
import board
import logging
import time
import datetime
import subprocess

from adafruit_seesaw.seesaw import Seesaw
from datetime import datetime, date

i2c_bus = board.I2C()
ss = Seesaw(i2c_bus, addr=0x36)

from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

# Create the I2C interface
i2c = busio.I2C(SCL, SDA)

# Create the SSD1306 OLED class
# The first two parameters are the pixel width and pixel height.  Change these
# to the right size for your display!
disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

# Clear display
disp.fill(0)
disp.show()

# Create blank image for drawing
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new("1", (width, height))

# Get drawing object to draw on image
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=0)

# Draw some shapes
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Default font. Commented out while slkscr.ttf is in use
#font = ImageFont.load_default()

# Load silkscreen font.
font = ImageFont.truetype('/home/pi/Adafruit_CircuitPython_seesaw/font/slkscr.ttf', 8)

while True:

    # Draw a black filled box to clear the image
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    # System monitoring variables defined
    cmd = "hostname -I | cut -d' ' -f1"
    IP = subprocess.check_output(cmd, shell=True).decode("utf-8")

    # read moisture level through capacitive touch pad
    touch = ss.moisture_read()

    # read temperature from the temperature sensor
    temp = (ss.get_temp() * (9 / 5) + 32)

    current_time = datetime.now()

    #'hostname' variable defined
    hostname = socket.gethostname()

    # Write four lines of text
    draw.text((x, top + 0), "Host: " + str(hostname), font=font, fill=255)
    draw.text((x, top + 8), "IP: " + IP, font=font, fill=255)
    draw.text((x, top + 16), "Temperature: " + str('%.2f'%temp), font=font, fill=255)
    draw.text((x, top + 25), "Moisture: " + str('%.2f'%touch), font=font, fill=255)

    # Display image
    disp.image(image)
    disp.show()

    #log time and moisture readings to /varlog/soil.log
    logging.basicConfig(filename='/var/log/soil.log',level=logging.INFO, format='%(message)s')
    logging.info(current_time.strftime("%b") + " " + current_time.strftime("%-d") + " " + current_time.strftime("%H:%M:%S") + " " + "    Temp: " + str('Temperature: %.2f'%temp) + "    Moisture: " + str('%.2f'%touch))
    time.sleep(5)
