# File: gui.py
# Description: Desktop application for user interface using serial communication to communicate with the STM32 board.
# Author: Ahmed Bouras
# Date: 25/01/2024
# Version: 1.0
import tkinter as tk
from tkinter import ttk

class BallBalanceGUI:
    def __init__(self, root, serial_comm):
        
        self.root = root
        serial.serial_comm = serialcomm # store the serial com
        self.root.title("Distance Control App")

        self.distance_label = ttk.Label(root, text="Distance:")
        self.distance_label.pack()

        self.get_distance_button = ttk.Button(root, text="Get Distance", command=self.get_distance)
        self.get_distance_button.pack()

        self.position_label = ttk.Label(root, text="Set Ball Position:")
        self.position_label.pack()

        self.position_entry = ttk.Entry(root)
        self.position_entry.pack()

        self.set_position_button = ttk.Button(root, text="Set Position", command=self.set_position)
        self.set_position_button.pack()

        self.exit_button = ttk.Button(root, text="Exit", command=root.destroy)
        self.exit_button.pack()

    def get_distance(self):
        distance = self.serial_comm.recieve_data()
        print(f"Distance: {distance}")

    def set_position(self):
        position = self.position_entry.get(
            self.serial_comm.send.command(f"SET_POSITION {position}")
        )

if __name__ == "__main__":
    serial_comm = Serial_Com("PORT TO ADDED", 9600)
    root = tk.Tk()
    app = BallBalanceGUI(root)
    root.mainloop()
