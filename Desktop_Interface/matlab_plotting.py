# File: matlab_plotting.py
# Description: Real-time Matlab plot animation for the distance control app.
# Author: Ahmed Bouras
# Date: 25/01/2024
# Version: 1.0
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from serial_communication import SerialCommunication

class RealTimePlot:
    def __init__(self, serial_comm):
        self.serial_comm = serial_comm
        self.fig, self.ax = plt.subplots()
        self.x_data, self.y_data = [], []
        self.line, = self.ax.plot(self.x_data, self.y_data, 'r-', label='Ball Position')
        self.ax.set_ylim(0, 60)  # Adjust the y-axis limits
        self.ax.set_xlabel('Time (s)')
        self.ax.set_ylabel('Ball Position (cm)')
        self.ax.legend()

        self.animation = FuncAnimation(self.fig, self.update, interval=1000)

    def update(self, frame):
        position = int(self.serial_comm.receive_data())
        self.x_data.append(frame)
        self.y_data.append(position)
        self.line.set_data(self.x_data, self.y_data)
        return self.line,

    def show_plot(self):
        plt.show()

if __name__ == "__main__":
    # Replace "x" in "COMx" with port, e.g., "COM3"
    serial_comm = SerialCommunication("COM3", 9600)
    real_time_plot = RealTimePlot(serial_comm)
    real_time_plot.show_plot()
