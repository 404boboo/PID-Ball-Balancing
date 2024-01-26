# File: gui.py
# Description: Desktop application for user interface using serial communication to communicate with the STM32 board.
# Author: Ahmed Bouras
# Date: 25/01/2024
# Version: 1.3
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

        # Start updating the position every 1000 milliseconds (1 second)
        self.update_position()

    def update_position(self):
        # Receive and update position
        position = self.serial_comm.receive_data()

        # Check if the position is a valid integer
        if position.isdigit():
            position = int(position)
        else:
            # Handle the case where position is not a valid integer
            position = 0

        self.position_label.config(text=f"Position: {position} cm")

        # Clear previous drawings
        self.canvas.delete("all")

        # Draw the beam
        beam_width = 10
        beam_length = 300  # Updated beam length
        beam_center_x = 250  # Updated beam center x-coordinate
        beam_left = beam_center_x - beam_length / 2
        self.canvas.create_rectangle(beam_left, 150, beam_left + beam_length, 160 + beam_width, fill="gray")

        # Draw the ball at the current position
        ball_radius = 10
        ball_x = beam_left + position * (beam_length / 60)  # Adjust the scaling factor as needed
        ball_y = 150 - ball_radius  # Place the ball on top of the beam
        self.canvas.create_oval(ball_x - ball_radius, ball_y - ball_radius, ball_x + ball_radius,
                                ball_y + ball_radius, fill="blue")

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
