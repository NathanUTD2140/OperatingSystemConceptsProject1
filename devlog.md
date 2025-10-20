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

### 10:04pm, October 18th, 2025
Added in use cases for whenever the user inputs a command. It was interesting splitting apart the command terminal lines, as I've only done this previously in my UNIX class. This was also interesting, as it was more simple then I thought, as most of it was making the case if the password wasn't set, and then calling the previous functions. 

## 10:59pm, October 18th, 2025

I didn't encounter nearly as many difficulties as I thought I would. I believed the cipher to be more difficult, but there are plenty of resources that can help with it. The log file was a bit tricky, but even that was straightforward enough. I think I fulfilled my goals for this part, and tomorrow I will work on the driver. I will take the input from the user in driver, and use it to open encryption and logger. Then driver will keep hearing things from the user and pass it to encryption. Actions that happen in encryption will then transfer to the logger file, which will record what happens and then continue nowards. 

## 8:00pm, October 19th, 2025

Today's session will involve programming driver, and seeing how the program works together in the command terminal. The plan is for the pipe to hear input from the command terminal, and then driver reacts to the input. If password is selected, it will give the information to logger and encrtyption as a password. Encrypt and decrypt will both be given to encryption, which will have a stored password in the file, and encrypt/decrypt based on the information given. If quit is selected, then it will write a unique entry to the log and terminate the program. Each case will be determined on user input, so it will look similar to encrypt, where it changes based on what the user wants to do. Once the user declares what they want to do, it will pass the revelant information to the logger and encryption file. There will be a log function that will give it the specified action and the user input for that action. It will also keep a history of words, in an array. This will help for easier decryption for the most part, as the computer will simply decrypt old messages the user wants. 

### 9:23pm, October 19th, 2025

When I start the program, after inputting what I want to select, the command line simply freezes. I find this odd, as multiple lines should output after the user receives input. I believe this is happening currently in the encryption file. I will also add an exception to make sure that weird inputs or other inputs to exit the command line can smoothly close. 

### 9:48pm, October 19th, 2025

It turns whenever it outputs something from the console, the program needs to clean out what is their basically. Thus, I haved added sys.stdout.flush(). after almost every line in the encrypt file, as I do not know if it needed it for every case. This was a weird error, as I knew it existed for stdin, but not stdout. This was an oversight on my part. I also added an exception and try statement, in case something like this happens, I can exit out of the program smoothly. It seems to run fine now, but I will test more. 

### 9:53pm, October 19th, 2025

When no password is set, it still asks for the history when using encrypt or decrypt. I can try and program around this, but I'm not too confident I can get this done in time. 
