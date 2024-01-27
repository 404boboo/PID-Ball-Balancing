# File: matlab_plotting.py
# Description: Real-time Matlab plot animation for the distance control app.
# Author: Ahmed Bouras
# Date: 25/01/2024
# Version: 1.5
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from serial_communication import SerialCommunication

class RealTimePlot(tk.Frame):
    MAX_FRAMES = 100  # Set a maximum number of frames

    def __init__(self, gui, master=None):
        super().__init__(master)
        self.gui = gui  # Reference to the BallBalanceGUI object
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.fig, self.ax = plt.subplots()
        self.canvas_widget = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas_widget.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.canvas_widget.draw()

        self.x_data, self.y_data = [], []
        self.line, = self.ax.plot(self.x_data, self.y_data, 'r-', label='Ball Position')
        self.ax.set_ylim(0, 60)
        self.ax.set_xlabel('Time (s)')
        self.ax.set_ylabel('Ball Position (cm)')
        self.ax.legend()

        # Start the animation
        self.start_animation()

    def start_animation(self):
        self.animation = FuncAnimation(self.fig, self.update, interval=1000, save_count=self.MAX_FRAMES)

    def update(self, frame):
        position = self.gui.serial_comm.receive_data()
        try:
            position = float(position)
        except ValueError:
            position = 0

        # Append current time to x_data
        self.x_data.append(self.x_data[-1] + 1 if self.x_data else 0)
        self.y_data.append(position)

        # Trim data if it exceeds MAX_FRAMES
        if len(self.x_data) > self.MAX_FRAMES:
            self.x_data.pop(0)
            self.y_data.pop(0)

        # Update the line data
        self.line.set_data(self.x_data, self.y_data)
        self.ax.relim()  # Update limits
        self.ax.autoscale_view()  # Autoscale the view
        self.canvas_widget.draw()
