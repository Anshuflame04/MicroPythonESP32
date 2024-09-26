from machine import Pin
import time

# Define pins
DIR_PIN = Pin(12, Pin.OUT)  # Direction pin
STEP_PIN = Pin(14, Pin.OUT)  # Step pin


#200 = 360degree 
#  as stepper motor has step angle of 1.8°, then:
      # 360/1.8=200 steps per revolution

# Set up stepper motor constants
steps_for_Clkwise = 200  
steps_for_AntClkwise = 50  

DELAY = 0.002  # Delay between steps (adjust for speed)

# Function to rotate the stepper motor
def step_motor(steps, direction):
    DIR_PIN.value(direction)  # Set motor direction
    for _ in range(steps):
        STEP_PIN.value(1)
        time.sleep(DELAY)
        STEP_PIN.value(0)
        time.sleep(DELAY)

# Main loop
while True:
    print("Rotating clockwise...")
    step_motor(steps_for_Clkwise, 1)  # Rotate 1 full revolution clockwise
    time.sleep(2)  # Pause for 2 seconds

    print("Rotating counterclockwise...")
    step_motor(steps_for_AntClkwise, 0)  # Rotate 1 full revolution counterclockwise
    time.sleep(1)  # Pause for 2 seconds
