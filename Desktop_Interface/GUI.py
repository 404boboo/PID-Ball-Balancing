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

        self.title("Ball Balancing App")
        self.geometry("800x600")

        self.create_widgets()

    def create_widgets(self):
        # Ball and Beam
        self.canvas = tk.Canvas(self, width=800, height=400, bg="white")
        self.beam = self.canvas.create_line(50, 200, 750, 200, width=10, capstyle=tk.ROUND)
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
        ttk.Button(self, text="Exit", command=self.destroy).pack(pady=10)

        # Real-time Plot
        self.fig, self.ax = plt.subplots()
        self.canvas_plot = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas_plot.get_tk_widget().pack()

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

    def update_animation(self):
        # Receive ball position from the serial port (you need to implement this part)
        position = 0.0
        try:
            position = float(self.serial_port.receive_data())
        except ValueError:
            pass

        # Update Ball Position
        self.current_position.set(position)
        canvas_x = (position / 60) * 700  # Scale ball position to canvas width
        self.canvas.coords(self.ball, canvas_x, 180, canvas_x + 40, 220)

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
