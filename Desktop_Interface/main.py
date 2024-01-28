# File: main.py
# Description: Main file for the PID Ball Balancing Desktop Interface.
# Author: Ahmed Bouras
# Date: 27/01/2024
# Version: 1.3



from GUI import BallBalanceGUI
from serial_communication import SerialCommunication

if __name__ == "__main__":
    serial_comm = SerialCommunication("COM3", 9600)
    app = BallBalanceGUI(serial_comm)
    app.mainloop()

