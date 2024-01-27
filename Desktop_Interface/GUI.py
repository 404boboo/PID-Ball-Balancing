# File: GUI.py
# Description: GUI file for the PID Ball Balancing Desktop Interface.
# Author: Ahmed Bouras
# Date: 27/01/2024

import tkinter as tk
from tkinter import ttk
from serial_communication import SerialCommunication
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

class BallBalanceGUI(tk.Tk):
    def __init__(self, serial_port):
        super().__init__()

        self.serial_port = serial_port
        self.current_position = tk.DoubleVar(value=0)
        self.destroyed = False  # Flag to track destruction

        self.title("Ball Balancing App")
        self.geometry("1000x700")  # Increased window size

        self.create_widgets()

    def create_widgets(self):
        # Ball and Beam
        canvas_width, canvas_height = 600, 200  # Decreased canvas size
        self.canvas = tk.Canvas(self, width=canvas_width, height=canvas_height, bg="white")
        beam_width, beam_height = 10, canvas_height // 2  # Decreased beam size
        self.beam = self.canvas.create_line(50, beam_height, canvas_width - 50, beam_height, width=beam_width, capstyle=tk.ROUND)
        ball_size = 20  # Decreased ball size
        self.ball = self.canvas.create_oval(0, 0, ball_size, ball_size, fill="red")
        self.canvas.pack(pady=10, expand=False)  # Disable canvas expansion

        # Setpoint Buttons
        setpoint_frame = ttk.Frame(self)
        ttk.Button(setpoint_frame, text="Set Point 30", command=lambda: self.set_setpoint(30)).grid(row=0, column=0, padx=10)
        ttk.Button(setpoint_frame, text="Set Point 20", command=lambda: self.set_setpoint(20)).grid(row=0, column=1, padx=10)
        ttk.Button(setpoint_frame, text="Set Point 40", command=lambda: self.set_setpoint(40)).grid(row=0, column=2, padx=10)
        setpoint_frame.pack()

        # Current Position Label
        ttk.Label(self, text="Current Position:").pack()
        ttk.Label(self, textvariable=self.current_position).pack()

        # Exit Button
        ttk.Button(self, text="Exit", command=self.destroy).pack(pady=10)

        # Real-time Plot
        fig_width, fig_height = 8, 4  # Increased figure size
        self.fig, self.ax = plt.subplots(figsize=(fig_width, fig_height))  # Set a fixed size for the figure
        self.canvas_plot = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas_plot.get_tk_widget().pack(expand=False)  # Disable figure expansion

        # Initialize Real-time Plot
        self.x_data, self.y_data = [], []
        self.line, = self.ax.plot(self.x_data, self.y_data, 'r-', label='Ball Position')
        self.ax.set_ylim(0, 60)
        self.ax.set_xlabel('Time (s)')
        self.ax.set_ylabel('Ball Position (cm)')
        self.ax.legend()

        # Schedule the animation update
        self.update_animation()

    def set_setpoint(self, setpoint):
        # Send setpoint value to Arduino (you need to implement this part)
        pass

    def destroy(self):
        self.destroyed = True  # Set the flag before destroying
        super().destroy()  # Call the original destroy method

    def update_animation(self):
        if not self.destroyed:  # Check if the application is still open
            # Receive ball position from the serial port (you need to implement this part)
            position = 0.0
            try:
                position = float(self.serial_port.receive_data())
            except ValueError:
                pass

            # Update Ball Position
            self.current_position.set(position)
            canvas_x = (position / 60) * 500  # Scale ball position to canvas width
            canvas_y = self.canvas.winfo_height() // 2  # Center vertically
            self.canvas.coords(self.ball, canvas_x, canvas_y, canvas_x + 20, canvas_y + 20)  # Adjusted ball size

            # Update Real-time Plot
            self.x_data.append(self.x_data[-1] + 0.1 if self.x_data else 0)
            self.y_data.append(position)

            # Trim data if it exceeds MAX_FRAMES
            if len(self.x_data) > 100:
                self.x_data.pop(0)
                self.y_data.pop(0)

            # Update the line data
            self.line.set_data(self.x_data, self.y_data)
            self.ax.relim()  # Update limits
            self.ax.autoscale_view()  # Autoscale the view
            self.canvas_plot.draw()

            # Schedule the next update after 50 milliseconds
            self.after(50, self.update_animation)

if __name__ == "__main__":
    # Replace "x" in "COMx" with the actual port, e.g., "COM3"
    serial_comm = SerialCommunication("COM3", 9600)
    app = BallBalanceGUI(serial_comm)
    app.mainloop()


