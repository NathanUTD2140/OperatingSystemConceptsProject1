import sys

# encryption/decryption using the Vigenère cipher. Connects to driver to recieve commands from the file driver
#   PASSWORD        Prompts user for a password
#   ENCRYPT <text>  encrypts based on a alphabet ket
#   DECRYPT <text>  decrypts a previous key
#   QUIT            stops the program
# Everything is sent back using stdout

def vigenere_encrypt(plaintext, key):
    """Encrypt plaintext using key (both expected as uppercase A-Z only)."""
    result = []                  # store the result of the encryption to display back to user
    for i, c in enumerate(plaintext):      # iterate with index (i) of each character(c)for thing we want to encrypt (key)
        p = ord(c) - 65          # Converstion to uppercase characters A-Z in ascii values
        k = ord(key[i % len(key)]) - 65  # repeat key by using modulo on index
        result.append(chr((p + k) % 26 + 65))  # shift it by the key, and convert from acsii value.
    return "".join(result)       # Put into the array

def main():
    passkey = None     # stores password from user when asked
    while True:
        input = sys.stdin.readline() # waits for the next command from the user
        if not input: #break if nothing
            break
        input = input.strip() #removes unnecessary space
        if not input:
            continue
