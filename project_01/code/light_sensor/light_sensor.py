# SPDX-FileCopyrightText: 2020 Bryan Siepert, written for Adafruit Industries

# SPDX-License-Identifier: Unlicense
import time
import board
import adafruit_bh1750

i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
sensor = adafruit_bh1750.BH1750(i2c)

def turn_off_light_sensor():
    """Turn off the moisture sensor 
    """
    gpio_set(GPIO_VAL, LOW)
# End def


def turn_on_light_sensor():
    """Turn on the moisture sensor
    """
    gpio_set(GPIO_VAL, HIGH)
# End def

def setup_sensor():
    """Setup all the pins for the reading.
    """
    gpio_setup(GPIO_VAL, OUT, LOW)
#End def


def read_light():
    """ set up and read moisture level"""
   
    touch = sesnor.lux
    if touch < 580: #chose a threshold value
        light = "bad"
    else:
        light = "good"
    print("  light: " + str(light))
    
    return(light)
    
#End def