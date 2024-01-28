# File: serial_communication.py
# Description: Serial communication file for the PID Ball Balancing Desktop Interface.
# Author: Ahmed Bouras
# Date: 27/01/2024

import serial

class SerialCommunication:
    def __init__(self, port, baudrate):
        self.serial_port = serial.Serial(port, baudrate, timeout=1)

    def send_command(self, command):
        self.serial_port.write(command.encode())

    def receive_data(self):
        try:
            if self.serial_port.in_waiting > 0:
                return self.serial_port.readline().decode().strip()
        except Exception as e:
            print(f"Error in receive_data: {e}")
        return ""

    def close_connection(self):
        self.serial_port.close()