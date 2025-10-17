# Devlog for project 1

## 12:27pm, October 9th, 2025

There are three different programs, one that logs messages to a log file and keep track of the processes, an encryption program that will encrypt and also decrypt strings, and then the driver will call upon these two programs when it is responding to user input and output. The driver file will also manage communication between the driver and encryption program, and then the session history of the time spent for the logger. 
The logger will track date, time, action, and a message to occupy it. The program will accept a single input, the log file, and keep running until it sees the action quit. I imagine that I will simply parse in the information from the log file, running it through a loop, until the action part of it has quit, and then terminate the loop. Until that happens, simply format the time, date, action, and message so it is readable to a user. 
The encryption file needs to use the Vigenère cypher, which will pass a key from the user, and after a valid key is given, the user will need to use it to "login." Any phrase passed in with the key word will be encrypted or decrypted.  This will require me to read more about it, but I will design a function that will detect with just letters have been passed, and then encrypt it. Vice versa for the decrpyt method.
The driver program needs to accept the log file from the user first, but other then that, it will mainly respond to the needs of the user. It will create the needed processes for the logs and the encryption, and then it will pass user input to the encryption file and the logger file. 

## 5:15pm, October 17th, 2025

I have learnt about the Vigenère cypher. My plan is to first try and implement the encryption file, and then design everything else around it. The main thing I am worried about is passing around files, since I have not actually tried that before in python. My plan for this session is to implement the encryption and decryption file. I mainly want to make sure the cipher is able to transform text correctly first. I will simply have it as an input when I run the file, and if the cipher is correct, then I want to make sure that it can be read correctly later from the log file. The goal for this session is to make sure the encryption file is fine. 
