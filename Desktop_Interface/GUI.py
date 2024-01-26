# File: gui.py
# Description: Desktop application for user interface using serial communication to communicate with the STM32 board.
# Author: Ahmed Bouras
# Date: 25/01/2024
# Version: 1.4
import tkinter as tk
from tkinter import ttk
from serial_communication import SerialCommunication

class BallBalanceGUI:
    def __init__(self, root, serial_comm):
        self.root = root
        self.serial_comm = serial_comm
        self.root.title("Ball Position Control App")

        # Set the size of the GUI
        self.root.geometry("600x200")

        # Create a canvas for graphical representation
        self.canvas = tk.Canvas(root, width=500, height=100, bg="white")
        self.canvas.pack()

        # Draw the track
        self.canvas.create_line(50, 50, 550, 50, width=5, fill="gray")

        # Create the ball
        self.ball = self.canvas.create_oval(50, 40, 60, 60, fill="blue")

        # Position label
        self.position_label = ttk.Label(root, text="Position:")
        self.position_label.pack()

        # Entry for setting ball position
        self.position_entry = ttk.Entry(root)
        self.position_entry.pack()

        # Button to set position
        self.set_position_button = ttk.Button(root, text="Set Position", command=self.set_position)
        self.set_position_button.pack()

        # Exit button
        self.exit_button = ttk.Button(root, text="Exit", command=root.destroy)
        self.exit_button.pack()

        # Start updating the position every 1000 milliseconds (1 second)
        self.update_position()

    def update_position(self):
        # Receive and update position
        position = self.serial_comm.receive_data()
        self.position_label.config(text=f"Position: {position} cm")

        # Update the position of the ball on the canvas
        if position.isdigit():
            ball_x = 50 + int(position) * 5  # Adjust the scaling factor as needed
            self.canvas.coords(self.ball, ball_x, 40, ball_x + 10, 60)

        # Schedule the next update after 1000 milliseconds
        self.root.after(1000, self.update_position)

    def set_position(self):
        position = self.position_entry.get()
        self.serial_comm.send_command(f"SET_POSITION {position}")

if __name__ == "__main__":
    # Replace "COMx" with your actual port, e.g., "COM3"
    serial_comm = SerialCommunication("COM3", 9600)
    
    root = tk.Tk()
    app = BallBalanceGUI(root, serial_comm)
    root.mainloop()
