# Devlog for project 1

## 12:27pm, October 9th, 2025

There are three different programs, one that logs messages to a log file and keep track of the processes, an encryption program that will encrypt and also decrypt strings, and then the driver will call upon these two programs when it is responding to user input and output. The driver file will also manage communication between the driver and encryption program, and then the session history of the time spent for the logger. 
The logger will track date, time, action, and a message to occupy it. The program will accept a single input, the log file, and keep running until it sees the action quit. I imagine that I will simply parse in the information from the log file, running it through a loop, until the action part of it has quit, and then terminate the loop. Until that happens, simply format the time, date, action, and message so it is readable to a user. 
The encryption file needs to use the Vigenère cypher, which will pass a key from the user, and after a valid key is given, the user will need to use it to "login." Any phrase passed in with the key word will be encrypted or decrypted.  This will require me to read more about it, but I will design a function that will detect with just letters have been passed, and then encrypt it. Vice versa for the decrpyt method.
The driver program needs to accept the log file from the user first, but other then that, it will mainly respond to the needs of the user. It will create the needed processes for the logs and the encryption, and then it will pass user input to the encryption file and the logger file. 

## 5:15pm, October 17th, 2025

I have learnt about the Vigenère cypher. My plan is to first try and implement the encryption file, and then design everything else around it. The main thing I am worried about is passing around files, since I have not actually tried that before in python. My plan for this session is to implement the encryption and decryption file. I mainly want to make sure the cipher is able to transform text correctly first. I will simply have it as an input when I run the file, and if the cipher is correct, then I want to make sure that it can be read correctly later from the log file. The goal for this session is to make sure the encryption file is fine. 

## 8:28pm, October 18th, 2025
I forgot to write a devlog for last session, but the majority of the time was not spent actually programming the assignment. I installed a compatible IDE, using intellij Community edition as my selected choice. I was at first confused about why everything I typed showed up blame and syntax such as "import sys" was not working, and I found out that the program did not natively support Python. I then had to install a proper python library, which was at 3.8 at first, and then route it to the appriopiate place for intellij. That still did not work, so I had to delete the project library, and then make a new project once I redownloaded python as python 3.12, and everything could work properly there. I lightly programmed a bit of the encryption file, but I spent most of the time running through what the cipher was, and looking at examples that program it successfully. Consider this the devlog for the previous section, as I will start a new session soon. 

## 8:47pm, October 18th, 2025

Today, I will try and finish off the files of encryption and logger. The encryption file will take the input of the user from driver, and then it will swap what it does based on what the user inputs does. If it commands for a password, it will set the key for the encryption as the password for the cipher and perform functions based off that. Once the password is set, the user can try and encrypt and decrypt words that are based into the program. If no password is set, I will simply make it so they have to set a password first. This will be accomplished with a simple check if the variable that contains the password is full or not. The encryption will be handled by a for loop that uses the enumerate function for the length of the word to be encrypted. From there, we will use the cipher to transform the word into our desired cipher. The decryption process will be handled in a similar way to the encryption, except the final result will be converted back to the original characters. Finally, quit will simply the have a break statement to exit the entire process. For logger, it will write to a new text file or append to an old text file, as it will be given the name of the file to write to in driver. It will simply record user input using the stdin, with formatting each line. If it reads quit from the stdin line, it will know to stop and exit the log file for now. Each line will start with the date and time of the action taken, and then write to a new line afterwards. It will be simpler then encryption most likely. 

### Updates for this session
### 9:28pm, October 18th, 2025
Added encryption, there were good examples online, so this part was relatively straightforward. I find it interesting to use ascii math. 

### 9:40pm, October 18th, 2025
Added decryption, this was relatively simple, as it is very similar to encryption. 
