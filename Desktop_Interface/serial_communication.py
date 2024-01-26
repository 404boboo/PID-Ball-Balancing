# File: serial_communication.py
# Description: Serial communication for the distance control app.
# Author: Ahmed Bouras
# Date: 25/01/2024
# Version: 1.0
import serial

class SerialCommunication:
    def __init__(self, port, baudrate):
        self.serial_port = serial.Serial(port, baudrate, timeout=1)

    def send_command(self, command):
        self.serial_port.write(command.encode())

    def receive_data(self):
        return self.serial_port.readline().decode().strip()

    def close_connection(self):
        self.serial_port.close()
