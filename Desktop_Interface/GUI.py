# File: gui.py
# Description: Desktop application for user interface using serial communication to communicate with the STM32 board.
# Author: Ahmed Bouras
# Date: 25/01/2024
# Version: 1.3
import tkinter as tk
from tkinter import ttk
from serial_communication import SerialCommunication
from matlab_plotting import RealTimePlot

class BallBalanceGUI:
    def __init__(self, root, serial_comm):
        self.root = root
        self.serial_comm = serial_comm
        self.root.title("Ball Position Control App")

        # Create two frames for two tabs
        self.tab1 = ttk.Frame(self.root)
        self.tab2 = ttk.Frame(self.root)

        # Add tabs to the main window
        self.tabs = ttk.Notebook(self.root)
        self.tabs.add(self.tab1, text='Control Tab')
        self.tabs.add(self.tab2, text='Graph Tab')
        self.tabs.pack(expand=1, fill="both")

        # Initialize components for each tab
        self.init_tab1()
        self.init_tab2()

    def init_tab1(self):
        # Canvas to draw the beam and ball
        self.canvas = tk.Canvas(self.tab1, width=500, height=300, bg="white")
        self.canvas.pack()

        # Position label
        self.position_label = ttk.Label(self.tab1, text="Position:")
        self.position_label.pack()

        # Entry for setting ball position
        self.position_entry = ttk.Entry(self.tab1)
        self.position_entry.pack()

        # Button to set position
        self.set_position_button = ttk.Button(self.tab1, text="Set Position", command=self.set_position)
        self.set_position_button.pack()

        # Exit button
        self.exit_button = ttk.Button(self.tab1, text="Exit", command=self.root.destroy)
        self.exit_button.pack()

        # Start updating the position every 1000 milliseconds (1 second)
        self.update_position()

    def init_tab2(self):
        # Create a separate frame for the live MATLAB plot
        self.matlab_plot_frame = ttk.Frame(self.tab2)
        self.matlab_plot_frame.pack(fill=tk.BOTH, expand=True)

        # Initialize the live MATLAB plot
        self.real_time_plot = RealTimePlot(self.serial_comm, self.matlab_plot_frame)

    def update_position(self):
        position = self.serial_comm.receive_data()

        if position.isdigit():
            position = int(position)
        else:
            position = 0

        self.position_label.config(text=f"Position: {position} cm")

        # Clear previous drawings
        self.canvas.delete("all")

        # Draw the beam and ball at the current position
        beam_width = 10
        beam_length = 300
        beam_center_x = 250
        beam_left = beam_center_x - beam_length / 2
        self.canvas.create_rectangle(beam_left, 150, beam_left + beam_length, 160 + beam_width, fill="gray")

        ball_radius = 10
        ball_x = beam_left + position * (beam_length / 60)
        ball_y = 150 - ball_radius
        self.canvas.create_oval(ball_x - ball_radius, ball_y - ball_radius, ball_x + ball_radius,
                                ball_y + ball_radius, fill="blue")

        self.root.after(1000, self.update_position)

    def set_position(self):
        position = self.position_entry.get()
        self.serial_comm.send_command(f"SET_POSITION {position}")

if __name__ == "__main__":
    # Replace "x" in "COMx" port, e.g., "COM3"
    serial_comm = SerialCommunication("COM3", 9600)
    
    root = tk.Tk()
    app = BallBalanceGUI(root, serial_comm)
    root.mainloop()
