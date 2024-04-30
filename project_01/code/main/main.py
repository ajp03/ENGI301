"""
--------------------------------------------------------------------------
Pocket Plant
--------------------------------------------------------------------------
License:   
Copyright 2024 Amelia Pillar

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

Use the following hardware components to make Pocket Plant:  
  - HT16K33 Display
  - Soil Moisture Sensor
  - Button
  - Pump (and relay)
  - Green LED
  - Red LED
  - Light Sensor

Requirements:
  - Hardware:
    - Default State: Needs to be able to take user input from button to increment display, pump off,
    green led on, red led off, light and moisture sensor monitoring
    - Watering State: Pump on, green led flashing, red led off, display WATR
    - Poor Light Conditions State: Pump off, red led on, display POOR
    - User interaction:
      - Needs to be able to increment the counter using the button
        - press button to increase by 1
      - Needs to be able to reset counter 
        - press and hold button for 2 seconds
    

Uses:
  - HT16K33 display library developed in class
    - Library updated to add "set_digit_raw()", "set_colon()"
  - Button 

"""
import time

import button        as button
import ht16k33       as HT16K33
import soil_sensor   as SOIL
import light_sesnor  as LIGHT
import pump          as PUMP
import tricolor_led  as TRILED
import led           as LED

# ------------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------------

#None

# ------------------------------------------------------------------------
# Global variables
# ------------------------------------------------------------------------

# None

# ------------------------------------------------------------------------
# Functions / Classes
# ------------------------------------------------------------------------

class PocketPlant():
    """ PocketPlant """
    reset_time     = None
    soil_sensor    = None
    light_sensor   = None
    pump           = None
    button         = None
    red_led        = None
    green_led      = None
    display        = None
    debug          = None
    
    def __init__(self, reset_time=2.0, button="P2_2", 
                       red_led="P2_6", green_led="P2_4",
                       pump="P2_36", soil_sensor="P1_21"
                       i2c_bus1=1, i2c_address1=0x70, i2c_bus2=2, i2c_address2=0x23, debug=False):
        """ Initialize variables and set up display """

        self.reset_time     = reset_time
        self.soil_sensor    = SOIL.soil_sensor(soil_sensor)
        self.light_sensor   = LIGHT.light_sensor(i2c_bus2, i2c_address2) 
        self.green_led      = LED.LED(green_led)
        self.red_led        = LED.LED(red_led)
        self.pump           = PUMP.pump(pump) #what goes in here
        self.display        = HT16K33.HT16K33(i2c_bus1, i2c_address1)
        self.button         = BUTTON.button(button)
        self.debug          = debug
        self._setup()
    
    # End def
    
    
    def _setup(self):
        """Setup the hardware components."""

        # Initialize Display
        self.set_display_dash()
        
        #set up soil sensor (does this have to go here)
        self.soil_sensor.setup_sensor()
        
        self.light_sensor.setup_sensor()

        # Button / LEDs / Servo 
        #   - All initialized by libraries when instanitated

    # End def
    
    def default(self)
    """Set up default state."""
    # End def

    
    def count(self)
    """ Increment display to count harvests
            - change display by 1 when button is pressed 
            - reset display when press and hold button
    
    """
        harvest_count                = 0        # Number of harvests to be displayed
        button_press_time            = 0.0      # Time button was pressed (in seconds)
        
        while(1):
            # Wait for button press and get the press time
            self.button.wait_for_press()
            button_press_time = self.button.get_last_press_duration()            
    
            # Compare time to increment or reset harvest_count
            if (button_press_time < self.reset_time):
                if harvest_count < HT16K33.HT16K33_MAX_VALUE:
                    harvest_count = harvest_count + 1
                else:
                    harvest_count = 0
            else:
                harvest_count = 0
            
            # Update the display
            self.display.update(people_count)

    # End def

   
   #do i need the start and stop watering
    def start_watering(self):
        """Water plant.
            - red LED on
            - turn pump on
        """
        #turn on pump
        self.pump.on()
        
        #turn on red LED
        self.red_led.on()
        
        #turn off green LED
        self.green_led.on()
       
    # End def
    
    def stop_watering(self):
        """Stop watering plant.
            - red LED off
            - pump off
        """
        #turn off pump
        self.pump.on()
        
        #turn off red led
        self.red_led.on()
        
    # End def
    
    
    def light_monitor(self):
        """Check light quality.
            - if below threshold, red LED on
            - if above threshold, green LED on 
        """
        if self.light_check > threshold:
            self.green_led.on
            self.red_led.off
        else:
            self.green_led.off
            self.red_led.on
    # End def


    def run(self):
        """Execute the main program."""
       
        self.default()        
        time.sleep(1)
                
        while(1):
            # Set Display to 0000
            self.set_display_default()

            # Wait for button press (do nothing)
            self.button.wait_for_button
                
            # Monitor light
            self.light_monitor()
            
            #Track harvests
            self.count()
            
            #Monitor water and water if needed
            if self.soil_sensor.read_moisture < 500 #choose some threshold
                self.pump.on
                self.green_led.off
                while self.soil_sensor.read_moisture < 500:
                    self.red_led.on
                    time.sleep(.1)
                    self.red_led.off
                    time.sleep(.1)
            time.sleep(1)

    # End def


    def set_display_default(self):
        """Set display to word "0000" """
        self.display.text("0000")

    # End def


    def set_display_input(self, number):
        """Set display to word "in: #" """
        self.display.text("in {0}".format(number))

    # End def


    def set_display_dash(self):
        """Set display to word "----" """
        self.display.text("----")

    # End def


    def cleanup(self):
        """Cleanup the hardware components."""
        
        # Set Display to show program is complete
        self.display.text("done")

        # Clean up hardware
        self.button.cleanup()
        self.red_led.cleanup()
        self.green_led.cleanup()

    # End def

# End class



# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------

if __name__ == '__main__':

    print("Program Start")

    # Create instantiation of the lock
    combo_lock = CombinationLock(debug=True)

    try:
        # Run the lock
        combo_lock.run()

    except KeyboardInterrupt:
        # Clean up hardware when exiting
        combo_lock.cleanup()

    print("Program Complete")

