# STM32 Ball Balancing System with Desktop Interface

This repository contains the source code and documentation for an Ball Balancing System using STM32 microcontroller, including an interactive Desktop Interface.

## Features

- **Desktop Interface:**
  - User-friendly interface built with Python.
  - Real-time visualization of the ball's position using Matplotlib.
  - Serial communication for interaction with the STM32 microcontroller.

- **STM32 F746ZG Microcontroller:**
  - Custom firmware to control and monitor the ball's position.
  - Integration with sensors and a servo motor for precise ball control.

- **Sensor Integration:**
  - Use of two HCSR-04 ultrasonic sensors for accurate ball position measurement.
  - Timer-based configurations for efficient sensor data acquisition.
    
- **Keypad Control:**
  - The project includes a keypad interface allowing the user to set the position of the ball manually.
    
- **LCD Display:**
  - An LCD to provide feedback on the ball's position and display the user's setpoint input.

- **Logging:**
  - Data logging of ball position over time.
  - Exportable logs in CSV format for further analysis.
  - Real-time plotting for immediate visual feedback.

## Mechanical Structure

### 3D-Printed Components

 -- TO BE ADDED.

## Installation

### STM32CubeIDE
To develop and flash the firmware for the STM32 microcontroller, we recommend using STM32CubeIDE. Follow these steps to install STM32CubeIDE:

1. Download and install [STM32CubeIDE](https://www.st.com/en/development-tools/stm32cubeide.html).
2. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/stm32-ball-balancing.git
   cd stm32-ball-balancing
3. Open STM32CubeIDE and configure the project settings.

3. Build and flash the firmware to your STM32 board.

