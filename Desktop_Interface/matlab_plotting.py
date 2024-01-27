# File: matlab_plotting.py
# Description: Real-time Matlab plot animation for the distance control app.
# Author: Ahmed Bouras
# Date: 25/01/2024
# Version: 1.3
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from serial_communication import SerialCommunication

class RealTimePlot(tk.Frame):
    def __init__(self, serial_comm, master=None):
        super().__init__(master)
        self.master = master
        self.serial_comm = serial_comm
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

    def start_animation(self):
        self.animation = FuncAnimation(self.fig, self.update, interval=1000)
        self.after(100, self.update_animation)  # Schedule the first update

    def update_animation(self):
        self.animation.event_source.stop()
        data = self.serial_comm.receive_data()
        position = int(data) if data.isdigit() else 0
        self.x_data.append(len(self.x_data))
        self.y_data.append(position)
        self.line.set_data(self.x_data, self.y_data)
        self.canvas_widget.draw()
        self.animation.event_source.start()
        self.after(1000, self.update_animation)  # Schedule the next update

    def update(self, frame):
        # This method is not used in this version
        pass

if __name__ == "__main__":
    # Replace "x" in "COMx" with the actual port, e.g., "COM3"
    serial_comm = SerialCommunication("COM3", 9600)
    root = tk.Tk()
    real_time_plot = RealTimePlot(serial_comm, master=root)
    real_time_plot.pack(fill=tk.BOTH, expand=True)
    real_time_plot.start_animation()
    root.mainloop()
