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
    
    def log(action, msg):
        """Helper to send messages to the logger process."""
        logger.stdin.write(f"{action} {msg}\n") # write what happened in log file with the action and messaged associated.
        logger.stdin.flush()

    # Log for specifically start, unique message
    log("START", "Driver started.")

    try:
        while True:
            # Ask the user for their input
            cmd = input("\nCommand (password/encrypt/decrypt/history/quit): ").strip().lower() # will continue to show up

            # QUIT
            if cmd == "quit":
                log("QUIT", "Driver exiting.")

                # Send quit commands to other process.
                encryption.stdin.write("QUIT\n")  # tell them what happened
                encryption.stdin.flush()
                logger.stdin.write("QUIT\n")
                logger.stdin.flush()

                # Waits on both processes to close
                encryption.wait()
                logger.wait()
                break # stop the loop

            # PASSWORD
            elif cmd == "password":
                password = input("Enter passkey (letters only): ").strip().upper() # gets rid of white space and converts to upper case (not case sensitive)
                if not password.isalpha():
                    print("Error: only letters allowed.") # only alphabet characters
                    log("ERROR", "Invalid passkey.") # write to log that it was an error with message
                    continue

                # give to encryption for it to know what to do
                encryption.stdin.write(f"PASS {password}\n")
                encryption.stdin.flush()

                # give result from encryption
                resp = encryption.stdout.readline().strip()
                print(resp)

                # Makes a log for this
                log("COMMAND", "password")
                log("RESULT", resp)

