# SPDX-FileCopyrightText: 2018 Brent Rubell for Adafruit Industries
#                         2022 Kris Keillor
#
# SPDX-License-Identifier: MIT

"""
DERT Demo Controller

Author: Brent Rubell for Adafruit Industries
        Kris Keillor
"""
import time
import busio
import serial
import re
from digitalio import DigitalInOut, Direction, Pull
import board
# Import the SSD1306 module.
import adafruit_ssd1306
# Import the RFM9x radio module.
import adafruit_rfm9x

# Button A
btnA = DigitalInOut(board.D5)
btnA.direction = Direction.INPUT
btnA.pull = Pull.UP

# Button B
btnB = DigitalInOut(board.D6)
btnB.direction = Direction.INPUT
btnB.pull = Pull.UP

# Button C
btnC = DigitalInOut(board.D12)
btnC.direction = Direction.INPUT
btnC.pull = Pull.UP

# Output A
outA = DigitalInOut(board.D19)
outA.direction = Direction.OUTPUT
outA.value = False

# Output B
outB = DigitalInOut(board.D20)
outB.direction = Direction.OUTPUT
outB.value = False

# Output C
outC = DigitalInOut(board.D21)
outC.direction = Direction.OUTPUT
outC.value = False

# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)

# 128x32 OLED Display
reset_pin = DigitalInOut(board.D4)
display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c, reset=reset_pin)
# Clear the display.
display.fill(0)
display.show()
width = display.width
height = display.height

# Create the UART interface
serPrt = serial.Serial("/dev/ttyAMA0",
    baudrate=115200,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    timeout=0,
    xonxoff=False,
    rtscts=False,
    write_timeout=None,
    dsrdtr=False,
    inter_byte_timeout=None,
    exclusive=True);

# Configure RFM9x LoRa Radio
CS = DigitalInOut(board.CE1)
RESET = DigitalInOut(board.D25)
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

# Environmental Variables
ARH = 0 # Air Relative Humidity
ATF = 0 # Air Temp F
LUX = 0 # Luminous Flux
SWC = 0 # Soil Water Content
STF = 0 # Soil Temp F
# Display Values
luxStr = ""

# User Input Variables
RunLights = False;
RunPump1 = False;
RunPump2 = False;

# Regexes to search for a numerical value
decRegex = "\d+\.\d+"
intRegex = "\d+"

display.fill(0)
try:
    rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, 915.0)
    display.text("RFM9x Detected", 0, 8, 1)
    display.show()
    time.sleep(3)
except RuntimeError as error:
    # Thrown on ver mismatch
    display.text("RFM9x: ERROR", 0, 8, 1)
    print("RFM9x Error: ", error)
    display.show()
    time.sleep(3)

while True:
    # Clear the image
    display.fill(0)

    # Attempt to set up the RFM9x Module
    display.text("DERT Demo Mode", 29, 0, 1)

    # Check buttons
    if not btnA.value:
        outA.value = True
        display.text("A", 108, 8, 1)
    else:
        outA.value = False

    if not btnB.value:
        outB.value = True
        display.text("B", 113, 8, 1)
    else:
        outB.value = False

    if not btnC.value:
        outC.value = True
        display.text("C", 121, 8, 1)
    else:
        outC.value = False

    # Check UART
    if (serPrt.inWaiting() > 0):
        data_str = serPrt.read(serPrt.in_waiting).decode("ascii");
        # Print rx data to term and notification to OLED
        print(data_str)
        display.text("Data read", 0, 8, 1)
        # Check if an error is reported
        if "! Error" in data_str:
            print("^ Error reported by DERT ^")
        else:
            # Check for Relative Humidity data
            if "+ARH" in data_str:
                data_num = re.findall(decRegex, data_str)
                if (len(data_num)>0):
                    ARH = round(float(data_num[0]), 1)
            # Check for Air Temperature data
            if "+ATF" in data_str:
                data_num = re.findall(decRegex, data_str)
                if (len(data_num)>0):
                    ATF = round(float(data_num[0]), 1)
            # Check for Lux data
            if "+LUX" in data_str:
                data_num = re.findall(intRegex, data_str)
                if (len(data_num)>0):
                    LUX = int(data_num[0])

    # Display Relative Humidity
    display.text(str(ARH)+"%RH", 0, 16, 1)

    # Display Air Temp
    display.text(str(ATF)+"F", 0, 24, 1)

    # Display Lux
    if (LUX < 1000):
        luxStr = str(LUX) + "lx"
        display.text(luxStr, 50, 16, 1)
    else:
        if (LUX > 10000):
            luxStr = str(round(LUX/1000, 1)) + "klx"
        else:
            luxStr = str(round(LUX/1000, 2)) + "klx"
        display.text(luxStr, 50, 16, 1)

    display.show()
    time.sleep(0.1)
