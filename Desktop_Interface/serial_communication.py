# File: serial_communication.py
# Description: Serial communication module for interfacing with the STM32 board.
# Author: Ahmed Bouras
# Date: 25/01/2024
# Version: 1.7

import serial
import time

class SerialCommunication:
    def __init__(self, port=None, baud_rate=None):
        self.port = port
        self.baud_rate = baud_rate
        self.serial_port = None

    def open_connection(self):
        if self.port is not None and self.baud_rate is not None:
            self.serial_port = serial.Serial(self.port, self.baud_rate, timeout=1)
            time.sleep(2)  # Allow some time for the connection to be established
            return True
        return False

    def close_connection(self):
        if self.serial_port is not None and self.serial_port.is_open:
            self.serial_port.close()

    def send_data(self, data):
        if self.serial_port is not None and self.serial_port.is_open:
            self.serial_port.write(data.encode())

    def receive_data(self):
        if self.serial_port is not None and self.serial_port.is_open:
            return self.serial_port.readline().decode().strip()

    def set_com_port(self, port):
        self.port = port

    def set_baud_rate(self, baud_rate):
        self.baud_rate = baud_rate

    def get_com_port(self):
        return self.port

    def get_baud_rate(self):
        return self.baud_rate


