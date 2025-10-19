# Read messages from stdin and timestamp the line to a file
# format: ACTION MESSAGE
# Example: "COMMAND encrypt HELLO"
# The logger writes lines formatted as:
#   YYYY-MM-DD HH:MM [ACTION] MESSAGE

import sys
from datetime import datetime     # for timestamps

def log_line(action, message, file):
    """
    Writes a single timestamped line for each command given.
    This function flushes the file so the output appears on disk immediately.
    Writes to a text file given by the original argument passed.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")  # format like 2025-10-18 10:15, like the example
    file.write(f"{timestamp} [{action}] {message}\n")   # Formats the with the brackets and message for the it
    file.flush()   # ensure the data is written to instantly. 

def main():
    # Expect exactly two arguments: start in driver and the file to make the logs appear. 
    if len(sys.argv) != 2:
        print("Usage: driver.py <file>", file=sys.stderr)
        sys.exit(1) #it failed, back out

    log_file = sys.argv[1] #set the log file name as the second argument
