# File: main.py
# Description: Main script to run the PID ball balancing system with GUI and real-time plot.
# Author: Ahmed Bouras
# Date: 25/01/2024
# Version: 1.3
import tkinter as tk
from gui import BallBalanceGUI
from serial_communication import SerialCommunication
from matlab_plotting import RealTimePlot

def main():
    # Replace "x" in "COMx" with the actual port, e.g., "COM3"
    serial_comm = SerialCommunication("COM3", 9600)

    root = tk.Tk()

    # Create the GUI
    app = BallBalanceGUI(root, serial_comm)

    # Start the Tkinter main loop
    root.after(100, app.update_matlab_tab)  # Call the update_matlab_tab method after 100 milliseconds
    root.mainloop()

if __name__ == "__main__":
    main()
