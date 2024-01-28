# File: gui.py
# Description: Desktop application for user interface using serial communication to communicate with the STM32 board.
# Author: Ahmed Bouras
# Date: 25/01/2024
# Version: 1.6

import tkinter as tk
from tkinter import ttk
from queue import Queue
from threading import Thread, Event
from serial_communication import SerialCommunication 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

class SerialThread(Thread):
    def __init__(self, serial_port, queue):
        super().__init__()
        self.serial_port = serial_port
        self.queue = queue
        self._stop_event= Event()

    def run(self):
        while not self._stop_event.is_set():
            position = self.serial_port.receive_data()
            print(f"Received position: {position}")
            self.queue.put(position)

    def stop(self):
        self._stop_event.set()


class BallBalanceGUI(tk.Tk):
    def __init__(self, serial_port):
        super().__init__()

        self.serial_port = serial_port
        self.current_position = tk.DoubleVar(value=0)
        self.queue = Queue()

        self.title("Ball Balancing App")
        self.geometry("1000x750")  # Set the window size

        self.create_widgets()

    def create_widgets(self):
        # Ball and Beam
        self.canvas = tk.Canvas(self, width=500, height=300, bg="white")
        self.ball = self.canvas.create_oval(0, 180, 40, 220, fill="red")
        self.canvas.pack(pady=10)

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
        self.exit_button = ttk.Button(self, text="Exit", command=self.exit_application)
        self.exit_button.pack(pady=10)

        # Real-time Plot
        self.fig, self.ax = plt.subplots(figsize=(8, 4))
        self.canvas_plot = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas_plot.get_tk_widget().pack()

        # Initialize Real-time Plot
        self.x_data, self.y_data = [], []
        self.line, = self.ax.plot(self.x_data, self.y_data, 'r-', label='Ball Position')
        self.ax.set_ylim(0, 60)
        self.ax.set_xlabel('Time (s)')
        self.ax.set_ylabel('Ball Position (cm)')
        self.ax.legend()

        # Start the serial thread
        self.serial_thread = SerialThread(self.serial_port, self.queue)
        self.serial_thread.start()

        # Schedule the animation update
        self.update_animation()

    def set_setpoint(self, setpoint):
        # Send setpoint value to serial port
        pass

    def update_animation(self):
        # Check if the window has been destroyed
        if not self.winfo_exists():
            return
        try:
            position = float(self.queue.get_nowait())
        except:
            position = 0.0

        # Update the current position variable
        self.current_position.set(position)

        # Draw the beam
        beam_width = 10
        beam_length = 400
        beam_center_x = 250 
        beam_left = beam_center_x - beam_length / 2
        self.canvas.create_rectangle(beam_left, 150, beam_left + beam_length, 160 + beam_width, fill="black")

        # Draw the ball at the current position
        ball_radius = 10
        ball_x = beam_left + position * (beam_length / 120) 
        ball_y = 140  # Place the ball on top of the beam
        self.canvas.coords(self.ball, ball_x - ball_radius, ball_y - ball_radius, ball_x + ball_radius, ball_y + ball_radius)

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

        # Schedule the next update after 500 milliseconds
        self.after(500, self.update_animation)

        # Handle the EXIT button when pressed
    def exit_application(self):
        # Handle serial thread when EXIT button is pressed to not run on background.
        self.serial_thread.stop()
        self.destroy()

if __name__ == "__main__":
    # Replace "x" in "COMx" with the actual port, e.g., "COM3"
    serial_comm = SerialCommunication("COM3", 9600)
    app = BallBalanceGUI(serial_comm)
    app.mainloop()
