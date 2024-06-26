"""
--------------------------------------------------------------------------
Light Sensor Driver
--------------------------------------------------------------------------
License:   
Copyright 2024 - Amelia Pillar

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this 
list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE 
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------

Light Sensor Driver

  This driver can support the Adafruit STEMMA Soil Sensor - I2C Capacitive Moisture Sensor. It combines code from 
  https://learn.adafruit.com/adafruit-stemma-soil-sensor-i2c-capacitive-moisture-sensor/python-circuitpython-test and
  https://www.hackster.io/sagrawal96/plant-babysitter-a85198.

Software API:

    turn_on_light_sensor()
      - turns on sensor
        
    turn_off_light_sensor()
      - turns off sensor
    
    setup_sensor()
      - sets up sensor

    read_light()
      - reads value from sensor and returns "water" as either "low" or "okay"
"""

# SPDX-FileCopyrightText: 2020 Bryan Siepert, written for Adafruit Industries

# SPDX-License-Identifier: Unlicense
import time
import board
import adafruit_bh1750

i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
sensor = adafruit_bh1750.BH1750(i2c)

class soil_sensor():
    """ soil_sensor Class """
    pin             = None

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
        return touch
        
    #End def