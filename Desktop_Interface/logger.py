# File: gui.py
# Description: Desktop applicatio Logger. Logs the values of position and the matlab plot.
# Author: Ahmed Bouras
# Date: 25/01/2024
# Version: 1.0
import csv
import matplotlib.pyplot as plt

class Logger:
    def __init__(self, log_filename='log.csv', plot_filename='plot.png'):
        self.log_filename = log_filename
        self.plot_filename = plot_filename
        self.x_data = []
        self.y_data = []

    def log_data(self, x, y):
        self.x_data.append(x)
        self.y_data.append(y)

    def save_log(self):
        with open(self.log_filename, 'w', newline='') as csvfile:
            fieldnames = ['Time', 'Position']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for time, position in zip(self.x_data, self.y_data):
                writer.writerow({'Time': time, 'Position': position})

    def save_plot(self):
        plt.plot(self.x_data, self.y_data, label='Ball Position')
        plt.xlabel('Time (s)')
        plt.ylabel('Ball Position (cm)')
        plt.legend()
        plt.savefig(self.plot_filename)
        plt.close()  # Close the plot to prevent it from being displayed


