# File: gui.py
# Description: Desktop application for user interface using serial communication to communicate with the STM32 board.
# Author: Ahmed Bouras
# Date: 25/01/2024
# Version: 1.9
import tkinter as tk
from tkinter import ttk
from serial_communication import SerialCommunication

class BallBalanceGUI:
    def __init__(self, root, serial_comm):
        self.root = root
        self.serial_comm = serial_comm
        self.root.title("Ball Position Control App")

        # Set the size of the GUI
        self.root.geometry("600x400")

        # Canvas to draw the beam and ball
        self.canvas = tk.Canvas(root, width=500, height=300, bg="white")
        self.canvas.pack()

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

        # Start updating the position every 100 milliseconds
        self.update_position()

    def update_position(self):
        # Receive and update position
        position = self.serial_comm.receive_data()

        # Check if the position is a valid integer
        try:
            position_value = int(position)
        except ValueError:
            position_value = 0

        self.position_label.config(text=f"Position: {position_value} cm")

        # Clear previous drawings
        self.canvas.delete("all")

        # Draw the beam
        beam_width = 20
        beam_length = 500  # Map the beam to be from 0 to 60
        beam_top_y = 150
        beam_bottom_y = beam_top_y + beam_width
        self.canvas.create_rectangle(
            0, beam_top_y,
            beam_length, beam_bottom_y,
            fill="gray"
        )

        # Draw the ball at the current position with a more roundy shape
        ball_radius = 15
        ball_aspect_ratio = 0.7  # Adjust the aspect ratio for a more circular appearance

        # Adjust the x-coordinate to center the ball
        ball_x = (position_value / 60) * (beam_length - 2 * ball_radius) + ball_radius
        ball_y = beam_top_y + beam_width / 2

        self.canvas.create_oval(
            ball_x - ball_radius, ball_y - ball_radius,
            ball_x + ball_radius, ball_y + ball_radius,
            fill="blue"
        )

        # Schedule the next update after 100 milliseconds
        self.root.after(100, self.update_position)

    def set_position(self):
        position = self.position_entry.get()
        self.serial_comm.send_command(f"SET_POSITION {position}")

if __name__ == "__main__":
    # Replace "x" in "COMx" with port, e.g., "COM3"
    serial_comm = SerialCommunication("COM3", 9600)
    
    root = tk.Tk()
    app = BallBalanceGUI(root, serial_comm)
    root.mainloop()
