import os
import storage
import digitalio
import busio as io
import board
import microcontroller
from time import sleep

# Use any pin that is not taken by SPI
SD_CS = board.GP13

# Connect to the card and mount the filesystem.
spi = io.SPI(0, sck=board.GP10, mosi=board.GP11, miso=board.GP12)
cs = digitalio.DigitalInOut(SD_CS)
sdcard = adafruit_sdcard.SDCard(spi, cs)
vfs = storage.VfsFat(sdcard)
storage.mount(vfs, "/sd")

with open("/sd/testfile.txt", "w") as writefile:
    writefile.write("First Line\n")
with open("/sd/testfile.txt", "a") as appendfile:
    appendfile.write("Second Line\n")
with open("/sd/testfile.txt", "r") as inputfile:
    for line in inputfile:
        print(line)
while True:
    with open("/sd/temphistory.txt", "a") as appendfile:
        appendfile.write(str(microcontroller.cpu.temperature) + "\n")
    sleep(5)
