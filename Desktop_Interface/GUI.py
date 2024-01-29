# File: gui.py
# Description: Desktop application for user interface using serial communication to communicate with the STM32 board.
# Author: Ahmed Bouras
# Date: 25/01/2024
# Version: 1.7

import time
import tkinter as tk
from tkinter import ttk, messagebox
from queue import Queue
from threading import Thread, Event
from serial_communication import SerialCommunication 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from logger import Logger

class SerialThread(Thread):
    def __init__(self, serial_port, queue):
        super().__init__()
        self.serial_port = serial_port
        self.queue = queue
        self.connected = False  # Initialize connection status
        self._stop_event = Event()

    def run(self):
        
        while not self._stop_event.is_set():
            self.check_for_data()
            #print(f"Received position: {position}")
            time.sleep(0.1)

    def stop(self):
        self._stop_event.set()
        
    def check_for_data(self):
        position = self.serial_port.receive_data()
        if position:
            print(f"Received position: {position}")
            self.queue.put(position)

class BallBalanceGUI(tk.Tk):
    def __init__(self, serial_port):
        super().__init__()

        self.serial_port = serial_port
        self.current_position = tk.DoubleVar(value=0)
        self.queue = Queue()
        self.connected = False  # Track connection status
        self.serial_thread = None # Initialize the thread without starting it
        self.logger = Logger()

        self.title("Ball Balancing App")
        self.geometry("1200x750")  # Set the window size
        self.frame_Serial = None  # Instance variable for the frame

        self.create_widgets()


 

    def create_widgets(self):
        # Ball and Beam
        self.canvas = tk.Canvas(self, width=500, height=300, bg="white")
        self.ball = self.canvas.create_oval(0, 180, 40, 220, fill="red")
        self.canvas.grid(row=0, column=0, rowspan=3, pady=10, padx=10)

        # Serial Configuration Title
        serial_title_label = ttk.Label(self, text="Serial Configuration:", font=("Times New Roman", 16, "bold"))
        serial_title_label.grid(row=0, column=1, columnspan=2, pady=(50, 0), padx=10)

        # COM Port Configuration
        ttk.Label(self, text="COM Port:", font=("Times New Roman", 12)).grid(row=1, column=1, columnspan=1, padx=(55,0))
        ttk.Label(self, text="Baud Rate:", font=("Times New Roman", 12)).grid(row=2, column=1, columnspan=1, padx=(55,0))

        self.clicked_com = tk.StringVar()
        self.clicked_bd = tk.StringVar()
        com_options = ["COM1", "COM2", "COM3", "COM4"]  # available COM ports
        baud_options = ["9600", "115200", "38400"]  # available baud rates

        self.com_menu = ttk.Combobox(self, textvariable=self.clicked_com, values=com_options)
        self.bd_menu = ttk.Combobox(self, textvariable=self.clicked_bd, values=baud_options)

        self.com_menu.grid(row=1, column=2, padx=10)
        self.bd_menu.grid(row=2, column=2, padx=10)

        # Connect/Disconnect Button
        self.connect_button = ttk.Button(self, text="Connect", command=self.toggle_connection)
        self.connect_button.grid(row=2, column=3, pady=(0, 0), padx=5)

        # Refresh Button
        ttk.Button(self, text="Refresh", command=self.refresh).grid(row=1, column=3, columnspan = 1, pady=(0, 0), padx=5)

        # Current Position Label
        ttk.Label(self, text="Current Position:", font=("Helvetica", 12, "bold")).grid(row=3, column=3, pady=(0, 50), padx=10)
        ttk.Label(self, textvariable=self.current_position, font=("Helvetica", 12, "bold")).grid(row=3, column=4, pady=(0, 50), padx=10)

        # Setpoint Buttons
        ttk.Button(self, text="Set Point 20", command=lambda: self.set_setpoint(20)).grid(row=3, column=2, pady=5, padx=(70,0))
        ttk.Button(self, text="Set Point 30", command=lambda: self.set_setpoint(30)).grid(row=3, column=3, pady=5, padx=(0,5))
        ttk.Button(self, text="Set Point 40", command=lambda: self.set_setpoint(40)).grid(row=3, column=4, pady=5, padx=(0,5))

        # Logs Button
        ttk.Button(self, text="Logs", command=self.show_logs).grid(row=2, column=5, columnspan=1, pady=(0, 0))

        # Exit Button
        self.exit_button = ttk.Button(self, text="Exit", command=self.exit_application)
        self.exit_button.grid(row=1, column=5, columnspan=1, pady=(0, 10))

        # Real-time Plot
        self.fig, self.ax = plt.subplots(figsize=(7, 4.2))
        self.canvas_plot = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas_plot.get_tk_widget().grid(row=3, column=0, columnspan=2)

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

    def refresh(self):
        # refresh functionality
        pass

    def show_logs(self):
        result = messagebox.askyesno("Save Logs", "Do you want to save the logs?")
        if result:
          # Fix the method name to match the Logger class
         self.logger.save_log()  # Save the log to a CSV file
         self.logger.save_plot()  # Save the plot to an Image file
         messagebox.showinfo("Logs Saved", "Logs have been saved successfully.")



    def stop_serial_thread(self):
        if self.serial_thread is not None and self.serial_thread.is_alive():
            self.serial_thread.stop()
            self.serial_thread.join()  # Wait for the thread to finish
            
    def set_setpoint(self, setpoint):
        if not self.connected:  # Check if user is connected to serial port before set pointing
            messagebox.showwarning("Connection Warning", "Please connect to the serial port first.")
            return

        try:
            # Send the setpoint value to the serial port
            setpoint_str = f"{setpoint}\r\n"
            setpoint_bytes = setpoint_str.encode('utf-8')  # Encode as bytes
            self.serial_port.send_data(setpoint_bytes)
        except Exception as e:
            messagebox.showerror("Setpoint Error", f"Failed to set setpoint: {e}")

    def update_animation(self):
        # Check if the window has been destroyed
        
        if not self.winfo_exists():
            self.stop_serial_thread()
            return
        try:
            position = int(self.queue.get_nowait())
        except:
            position = 0

        # Update the current position variable
        self.current_position.set(position)

        # Draw the beam
        beam_width = 10
        beam_length = 400
        beam_center_x = 250 
        beam_left = beam_center_x - beam_length / 2

        # Create or update the beam elements
        beam_items = self.canvas.find_withtag("beam")
        if not beam_items:
         self.canvas.create_rectangle(beam_left, 150, beam_left + beam_length, 160 + beam_width, fill="black")
        else:
         self.canvas.coords(beam_items[0], beam_left, 150, beam_left + beam_length, 160 + beam_width)


        # Draw the ball at the current position
        ball_radius = 10
        ball_x = beam_left + position * (beam_length / 60) # Map the ball to the beam 0 to 60 cm. (Left to right)
        ball_y = 140  # Place the ball on top of the beam
        self.canvas.coords(self.ball, ball_x - ball_radius, ball_y - ball_radius, ball_x + ball_radius, ball_y + ball_radius)

        # CHeck if serial connection is established
        if self.connected:
        # Update Real-time Plot and Log
         self.logger.log_data(self.x_data[-1] + 0.1 if self.x_data else 0, position)
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
        self.after(100, self.update_animation)
    

    # Handle the EXIT button when pressed
    def exit_application(self):
        # Handle serial thread when EXIT button is pressed to not run on background.
        self.stop_serial_thread()
        self.destroy()

    # Toggle connection status
    def toggle_connection(self):
        if not self.connected:
            # Connect
            com_port = self.clicked_com.get()
            baud_rate = int(self.clicked_bd.get())

            if com_port and baud_rate:
                self.serial_port.set_com_port(com_port)
                self.serial_port.set_baud_rate(baud_rate)
                if self.serial_port.open_connection():
                    self.connected = True
                    self.connect_button.configure(text="Disconnect")
                    messagebox.showinfo("Connection Status", "Connected to {}".format(com_port))
                else:
                    messagebox.showerror("Connection Error", "Failed to connect. Check the port and try again.")
        else:
            # Disconnect
            self.serial_port.close_connection()
            self.connected = False
            self.connect_button.configure(text="Connect")
            messagebox.showinfo("Connection Status", "Disconnected")




if __name__ == "__main__":
    serial_comm = SerialCommunication()  
    app = BallBalanceGUI(serial_comm)
    app.mainloop()
