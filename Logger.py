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

    # Open the new log file in append mode; create if its new, or append to a new file.
    # Use encoding='utf-8' for consistency
    with open(log_file, "a", encoding="utf-8") as file:
        # Read lines with stdin and covert them into formatted log entry
        while True:
            inputAction = sys.stdin.readline()   # blocking read from pipeline
            if not inputAction :                  # Pipe closed, break out
                break
            inputAction  = inputAction.strip()           # remove any unnecessary space
            if inputAction  == "QUIT":            # stop the sequence, make one special last line and break out
                log_line("QUIT", "Logger exiting.", file)
                break

            # Try to split the input into an action and the remainder of the message.
            # If there's no space, treat it like an info case
            if " " in inputAction :
                action, logged = inputAction.split(" ", 1)
            else:
                action, logged = "INFO", inputAction  #base case

            # Write the new log entry to the file with the function
            log_line(action, logged, file)

# Run main when executed directly
if __name__ == "__main__":
    main()
