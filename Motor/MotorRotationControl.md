# Stepper Motor Rotation Control with buttons

## Description

- **Pins Definition**: 
  - **Direction Pin**: Sets the rotation direction of the motor.
  - **Step Pin**: Triggers the motor to take a step.
  - **Switches**: Two switches allow the user to control the motor direction: one for clockwise and one for counterclockwise rotation.

- **Stepper Motor Constants**:
  - `steps_per_revolution`: Number of steps required to complete a full revolution (200 steps for a 1.8° step angle).
  - `DELAY`: Delay between each step to control the speed of rotation.

- **Functionality**:
  - The `step_motor` function accepts the number of steps and the desired direction, setting the motor's direction and stepping it the specified number of times.
  
- **Main Loop**:
  - Continuously checks the state of the switches:
    - If the clockwise switch is pressed, the motor rotates one full revolution clockwise.
    - If the counterclockwise switch is pressed, the motor rotates one full revolution counterclockwise.
    - If no switch is pressed, it prints "No button pressed."
  
- **Debouncing**: Debounce refers to a technique used to prevent false triggering of a switch or button
- 
## Notes

- Adjust the `DELAY` value to control the speed of the motor.
- br
https://wokwi.com/projects/410664921070528513
