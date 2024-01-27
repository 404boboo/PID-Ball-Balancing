# File: gui.py
# Description: Desktop application for user interface using serial communication to communicate with the STM32 board.
# Author: Ahmed Bouras
# Date: 25/01/2024
# Version: 1.5
import tkinter as tk
from tkinter import ttk
from serial_communication import SerialCommunication

class BallBalanceGUI:
    def __init__(self, root, serial_comm):
        self.root = root
        self.serial_comm = serial_comm
        self.root.title("Ball Position Control App")
        self.root.geometry("800x600")

        self.notebook = ttk.Notebook(root)

        self.control_tab = ttk.Frame(self.notebook)
        self.matlab_tab = ttk.Frame(self.notebook)

        self.notebook.add(self.control_tab, text="Control")
        self.notebook.add(self.matlab_tab, text="Matlab Plot")

        self.notebook.pack(fill='both', expand=True)

        # Create control tab elements
        self.create_control_tab()

    def create_control_tab(self):
        # Label for position
        position_label = ttk.Label(self.control_tab, text="Position:")
        position_label.grid(row=0, column=0, padx=10, pady=10)

        # Entry for setting ball position
        position_entry = ttk.Entry(self.control_tab)
        position_entry.grid(row=0, column=1, padx=10, pady=10)

        # Button to set position
        set_position_button = ttk.Button(self.control_tab, text="Set Position", command=self.set_position)
        set_position_button.grid(row=0, column=2, padx=10, pady=10)

        # Canvas to draw the beam and ball
        self.canvas = tk.Canvas(self.control_tab, width=500, height=300, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        # Exit button
        exit_button = ttk.Button(self.control_tab, text="Exit", command=self.root.destroy)
        exit_button.grid(row=2, column=1, pady=10)

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

        # Clear the canvas
        self.canvas.delete("all")

        # Draw the beam
        beam_height = 20  # Adjust the beam height as needed
        self.canvas.create_rectangle(50, 150 - beam_height / 2, 550, 150 + beam_height / 2, fill="black")

        # Draw the ball at the updated position
        ball_radius = 15  # Adjust the ball radius as needed
        scaled_position = 50 + (position / 60) * 500  # Adjust the scaling factor as needed
        self.canvas.create_oval(scaled_position - ball_radius, 150 - ball_radius,
                                scaled_position + ball_radius, 150 + ball_radius,
                                fill="red")

        # Schedule the next update after 1000 milliseconds
        self.root.after(1000, self.update_position)

    def set_position(self):
        # Your set position logic goes here
        pass

if __name__ == "__main__":
    # Replace "x" in "COMx" port, e.g., "COM3"
    serial_comm = SerialCommunication("COM3", 9600)

    root = tk.Tk()
    app = BallBalanceGUI(root, serial_comm)
    root.mainloop()
