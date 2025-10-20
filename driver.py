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

    password_enabled = False   # Variable to see if password is set or not

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

                #The if state checks to make sure the result was correct
                if resp.startswith("RESULT"):
                    password_enabled = True #set it as true now

            # ENCRYPT/DECRYPT
            elif cmd in ["encrypt", "decrypt"]: # if command is either of these, go here

                if not password_enabled: #if this is still false, ask the user for a password first
                    print("Error: You must set a password first.")
                    log("ERROR", "Attempted encryption/decryption without password.") #give log the error
                    continue  # skip everything below

                mode = cmd.upper() # mode is encrypt or decrypt

                # If history has something, we can use previous results
                choice = input("Use history? (y/n): ").strip().lower() # case insensitive
                if choice == "y" and history: # if the choice is yes and we have history, go into this loop
                    for i, s in enumerate(history): # enumerate for indexes of history
                        print(f"{i+1}. {s}") # s is the value currently in history
                    idx = input("Select number or press Enter for new: ").strip()
                    if idx.isdigit() and 1 <= int(idx) <= len(history): # check if it's an index in history, and is a number
                        text = history[int(idx) - 1] # output the text there
                    else:
                        text = input("Enter new text: ").strip().upper() # input next text as
                else:
                    text = input("Enter new text: ").strip().upper() # base case

                if not text.isalpha(): # only allow letters
                    print("Error: only letters allowed.")
                    log("ERROR", "Non-letter input.")
                    continue

                # Send command to encryption
                encryption.stdin.write(f"{mode} {text}\n")
                encryption.stdin.flush()

                # Receive the output from encryption
                resp = encryption.stdout.readline().strip()
                print(resp)

                # Log the result
                log("COMMAND", f"{cmd} {text}")
                log("RESULT", resp)

                # Save to history (both input and result)
                if resp.startswith("RESULT "):
                    result = resp.split(" ", 1)[1]
                    history.append(text)
                    history.append(result)
                # History if we want it
            elif cmd == "history": #
                if not history: # no history
                    print("(empty)") # put as empty
                else:
                    for i, h in enumerate(history): # enumerate through history
                        print(f"{i+1}. {h}")
                log("COMMAND", "history") # command for history

            # back up case if something goes wrong
            else:
                print("Unknown command.")
                log("ERROR", f"Unknown command {cmd}")

    # Exit if something goes wrong in the terminal
    except KeyboardInterrupt:
        print("\nExiting...")
        encryption.stdin.write("QUIT\n"); encryption.stdin.flush()
        logger.stdin.write("QUIT\n"); logger.stdin.flush()
        encryption.wait()
        logger.wait()

if __name__ == "__main__":
    main()
