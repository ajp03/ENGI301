"""
--------------------------------------------------------------------------
Pump Driver
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

Pump Driver

  This driver can support turns on and off a pump using a relay. It is modeled off the LED driver from class.

Software API:
    setup()
      - makes sure pump is off
      
    on()
      - Turn the pump on

    off()
      - Turn the pump off
"""
import Adafruit_BBIO.GPIO as GPIO

# ------------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------------

HIGH          = GPIO.HIGH
LOW           = GPIO.LOW

# ------------------------------------------------------------------------
# Global variables
# ------------------------------------------------------------------------

# None

# ------------------------------------------------------------------------
# Functions / Classes
# ------------------------------------------------------------------------
class Pump():
    """ Pump Class """
    pin             = None
    on_value        = None
    off_value       = None
    
    def __init__(self, pin=None, low_off=True):
        """ Initialize variables and set up the Pump """
        if (pin == None):
            raise ValueError("Pin not provided for Pump()")
        else:
            self.pin = pin
        
        # By default the "ON" value is "1" and the "OFF" value is "0".  
        # This is done to make it easier to change in the future
        if low_off:
            self.on_value  = HIGH
            self.off_value = LOW
        else:
            self.on_value  = LOW
            self.off_value = HIGH

        # Initialize the hardware components        
        self._setup()
    
    # End def
    
    
    def _setup(self):
        """ Setup the hardware components. """
        # Initialize LED
        GPIO.setup(self.pin, GPIO.OUT)
        self.off()

    # End def


    def is_on(self):
        """ Is the Pump on?
        
           Returns:  True  - Pump is ON
                     False - Pump is OFF
        """
        return GPIO.input(self.pin) == self.on_value

    # End def

    
    def on(self):
        """ Turn the Pump ON """
        GPIO.output(self.pin, self.on_value)
        
     # End def
    
    
    def off(self):
        """ Turn the pump OFF """
        GPIO.output(self.pin, self.off_value)
        
    # End def


    def cleanup(self):
        """ Cleanup the hardware components. """
        # Turn pump off 
        self.off()
        
    # End def
    
# End class

