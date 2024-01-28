# File: serial_communication.py
# Description: Serial communication file for the PID Ball Balancing Desktop Interface.
# Author: Ahmed Bouras
# Date: 27/01/2024
# Version: 1.6


import serial

class SerialCommunication:
    def __init__(self, port, baud_rate):
        self.serial_port = serial.Serial(port, baud_rate, timeout=1)

    def send_command(self, command):
        self.serial_port.write(command.encode())

    def receive_data(self):
        return self.serial_port.readline().decode().strip()

    def close(self):
        self._stop_event.set()