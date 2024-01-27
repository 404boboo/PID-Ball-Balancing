# File: matlab_plotting.py
# Description: MATLAB plotting file for the PID Ball Balancing Desktop Interface.
# Author: Ahmed Bouras
# Date: 27/01/2024

import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation

class RealTimePlot(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        # Your existing MATLAB plotting logic here
        # For example, a simple plot with random data
        import matplotlib.pyplot as plt
        import numpy as np

        self.fig, self.ax = plt.subplots()
        self.line, = self.ax.plot([], [], lw=2)

        self.ax.set_xlim(0, 60)
        self.ax.set_ylim(0, 1)

        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.canvas.draw()

    def update_animation(self, position):
        # Your existing animation update logic here
        self.line.set_data([position, position], [0, 1])
        return self.line,
