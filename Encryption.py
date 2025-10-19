import sys

# encryption/decryption using the Vigenère cipher. Connects to driver to recieve commands from the file driver
#   PASSWORD        Prompts user for a password
#   ENCRYPT <text>  encrypts based on a alphabet ket
#   DECRYPT <text>  decrypts a previous key
#   QUIT            stops the program
# Everything is sent back using stdout

def main():
    passkey = None     # stores password from user when asked
    while True:
        input = sys.stdin.readline() # waits for the next command from the user
        if not input: #break if nothing
            break
        input = input.strip() #removes unnecessary space
        if not input:
            continue
