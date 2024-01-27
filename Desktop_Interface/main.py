from gui import BallBalanceGUI
from serial_communication import SerialCommunication

if __name__ == "__main__":
    # Replace "x" in "COMx" with the actual port, e.g., "COM3"
    serial_comm = SerialCommunication("COM3", 9600)
    app = BallBalanceGUI(serial_comm)
    app.mainloop()
