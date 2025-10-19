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


def vigenere_decrypt(ciphertext, key):
    """Decrypt ciphertext using key (both expected as uppercase A-Z only)."""
    result = []                  # store decryption
    for i, c in enumerate(ciphertext): #similar concept, just using the decryption of the cipher now
        cval = ord(c) - 65       # convert ciphertext char to acsii
        kval = ord(key[i % len(key)]) - 65  # key char modification
        result.append(chr((cval - kval) % 26 + 65))  # reverse shift, conver to char again
    return "".join(result)  #put into the array

def main():
    passkey = None     # stores password from user when asked
    while True:
        input = sys.stdin.readline() # waits for the next command from the user
        if not input: #break if nothing
            break
        input = input.strip() #removes unnecessary space
        if not input:
            continue

# parse the input from the user into the first half as the instruction and the other as a part
        parts = input.split(" ", 1)   # split at the first space only, could be a cipher otherwise
        instruction = parts[0].upper()          # uppercase for normalization
        arg = parts[1].upper() if len(parts) > 1 else ""  # argument if present, uppercase

        # QUIT: terminate the process, simple and clean
        if instruction == "QUIT":
            break

        # PASS: set the key (only letters)
        elif instruction == "PASS":
            if not arg.isalpha():      # Make sure it's alphabet characters
                print("ERROR Passkey must contain only letters.") #error message for user
            else:
                passkey = arg          # store the password
                print("RESULT Passkey set.") #tell the user it has been set

        # ENCRYPT: encrypt userString using stored password
        elif instruction == "ENCRYPT":
            if password is None:       # if there is no password, return error
                print("ERROR Password not set.")
            elif not userString.isalpha():   # validate text (letters only) (think it's valid for this project)
                print("ERROR Input must contain only letters.")
            else:
                print(f"RESULT {vigenere_encrypt(userString, password)}")  # pass to function, output result
          

        # DECRYPT: decrypt userString using stored password
        elif instruction == "DECRYPT":
            if password is None:
                print("ERROR Password not set.") # if there is no password, return error
            elif not userString.isalpha():
                print("ERROR Input must contain only letters.")  # validate text (letters only) (think it's valid for this project)
            else:
                print(f"RESULT {vigenere_decrypt(userString, password)}")  # pass to function, output result
          

        # Not valid string, return error
        else:
            print("ERROR Unknown command.")
          

# Entry point guard so module can be imported without running main()
if __name__ == "__main__":
    main()

