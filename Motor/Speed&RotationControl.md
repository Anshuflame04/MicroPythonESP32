## Stepper Motor Speed and Rotation Control


- **Motor Movement**: The code allows control of a stepper motor's movement, enabling it to rotate forward or backward based on user input through switches.

- **Speed Control**: Users can increase or decrease the motor's speed by adjusting the delay between steps. This is managed through dedicated switches that modify the `current_delay` variable, allowing for smooth adjustments.

- **Functionality**:
  - **Step Execution**: The `step_motor` function executes the motor steps in the specified direction, with delays determining the speed.
  - **Dynamic Speed Printing**: The `print_speed` function outputs the current speed in steps per second and RPM, providing real-time feedback.
  - **Direction Handling**: The `forward_motion` and `backward_motion` functions encapsulate the logic for moving the motor in either direction while printing the speed after each action.

https://wokwi.com/projects/410838311265556481
