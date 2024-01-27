# File: main.py
# Description: Main script to run the PID ball balancing system with GUI and real-time plot.
# Author: Ahmed Bouras
# Date: 25/01/2024
# Version: 1.1
import tkinter as tk
from gui import BallBalanceGUI
from matlab_plotting import RealTimePlot
from serial_communication import SerialCommunication

def main():
    # Replace "x" in "COMx" with the actual port, e.g., "COM3"
    serial_comm = SerialCommunication("COM3", 9600)

    root = tk.Tk()
    
    # Create the real-time plot object
    real_time_plot = RealTimePlot(serial_comm, root)

    # Create the GUI
    app = BallBalanceGUI(root, serial_comm)
    
    # Start the Tkinter main loop
    root.mainloop()

if __name__ == "__main__":
    main()
