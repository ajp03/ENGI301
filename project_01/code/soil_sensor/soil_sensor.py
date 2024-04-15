#from https://learn.adafruit.com/adafruit-stemma-soil-sensor-i2c-capacitive-moisture-sensor/python-circuitpython-test
#also from https://www.hackster.io/sagrawal96/plant-babysitter-a85198

import time
import board
from adafruit_seesaw.seesaw import Seesaw

i2c_bus = board.I2C()  # uses board.SCL and board.SDA
# i2c_bus = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller

ss = Seesaw(i2c_bus, addr=0x36)


def turn_off_moisture_sensor():
    """Turn off the moisture sensor 
    """
    gpio_set(GPIO_VAL, LOW)
# End def


def turn_on_moisture_sensor():
    """Turn on the moisture sensor
    """
    gpio_set(GPIO_VAL, HIGH)
# End def


def setup_sensor():
    """Setup all the pins for the reading.
    """
    gpio_setup(GPIO_VAL, OUT, LOW)
#End def


def read_moisture():
    """ set up and read moisture level"""
   
    touch = ss.moisture_read()
    if touch < 580:
        water = "low"
    else:
        water = "okay"
    print("  moisture: " + str(water))
    
    return(water)
    
#end def