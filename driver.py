import sys
from subprocess import Popen, PIPE

# Main control program.
#  Uses logger.py to record activity to a log file
#  Uses encryption.py to handle encryption/decryption logic
# Communication through pipes, and maintains a history list of things done by user.
# --------------------------------------------------------------

def main():
    if len(sys.argv) != 2:
        print("Usage: driver.py logfilename.text")
        sys.exit(1)
        # simply stop if the user does not pass the two wanted files

    logFile = sys.argv[1] # set logfile as the new argument

    # sys.executable for cross-platform reliability
    python_exec = sys.executable

    # The logger process to write to a file
    logger = Popen([python_exec, "logger.py", logFile],
                   stdin=PIPE, text=True, encoding="utf-8")
    # opens the pipe, writes to the logfile

    # Open encryption, so we can actually encrypt and decrypt
    encryption = Popen([python_exec, "encryption.py"],
                      stdin=PIPE, stdout=PIPE, text=True, encoding="utf-8")
    # includes stdout in the pipe, to output to user.

    # List to store session history of inputs/results
    history = [] # history is a blank array full of user inputs for encryption and decryption


