# Allows for abrupt program termination.
import sys

# Allows the user to gauge their CPU usage.
import time
#------------------------------------------------------------------------------------------------------------------------


# This entire paragraphs helps to define what the program does. I suggest reading it all before going ahead and using
# my program. I am in the process of moving to an PyCharm, which is an IDE that is designed specifically for Python.
# My programs WILL STILL be runnable on IDLE.

print("-----------------------------------------------------------------------------------------------------------------------")
print("You've done so well with my other games, so I want to try something different.")
print("Instead of a game, I'm going to write a file with information YOU supply!")
print()

print("You don't need to create the file, I will for you. The file will be created and you should search for it using your computer's seek tool.")

print("On Windows and Mac's using IDLE, it SHOULD auto-save to the desktop. PyCharm will save it to the program's running folder OR the Desktop.")
print()

print("Let's get started!")

print("-----------------------------------------------------------------------------------------------------------------------")


#------------------------------------------------------------------------------------------------------------------------


# Set user attempts to zero (this is for the non-appending section of code).
attempts = 0

# Set total attempts to three (this is for the non-appending section of code).
totalAttempts = 3

# Set final attempts to zero (this is for the APPENDING section of code).
finalAttempts = 0

# Set total final attempts to zero (this is for the APPENDING section of code).
totalFinalAttempts = 3


#------------------------------------------------------------------------------------------------------------------------

# Ask the user for string input. This will be what your file is called. You can name it ANYTHING, but it will always
# become a .txt file as I have set the concatenation (binding of two strings) to ".txt").
fileNameInput = str(input("First, your file needs a name. Go ahead and give it one: "))
print("Please wait while I render the name. This will take three seconds.")


time.sleep(3) # Wait three seconds to allow for better CPU usage. This program will most likely use a lot of CPU energy.


# The concatenation of the two strings.
fullFile = str(fileNameInput + ".txt")
print("Your file will be called: " + fullFile) # Display what the file will be called, preparing it for verification.

# New line.
print()

confirmString = str(input("Please type (Yes) or (No) to confirm: ")) # Verify that you REALLY want your file named "filnameInput."
                                                                     # You will be able to change this in the following loop.


#------------------------------------------------------------------------------------------------------------------------
# If you like the name, type (Yes) and it will continue out of the while-loop. Don't like the name?
# Type (No) and it will continue through the loop until you are satisfied with the name of your
# file. Give an improper response? My program checks for that and returns its own error. Just pressing
# enter or random letters WON'T break the program. It will instead reduce the amount of attempts you have
# to continue further on in the code.


while (attempts != 2):

    # Did you type yes? You will go through this if-statement, then.
    if (confirmString == "Yes" or confirmString == "yes"):

        print("-----------------------------------------------------------------------------------------------------------------------")

        print("You typed " + confirmString + ". I'm glad you're happy with the name! Let's start putting this file together!!")
        break

    # Did you type no? You will go through this if-statement, then.
    if (confirmString == "No" or confirmString == "no"):

        print("-----------------------------------------------------------------------------------------------------------------------")

        print("Oh no! I got your file name wrong, let's fix that!!")
        print()

        fileNameInput = str(input("Enter a new file name here: "))

        print("Please wait while I render the name. This will take three seconds.")
        time.sleep(3)

        fullFile = str(fileNameInput + ".txt")

        print("Your file will be called: " + fullFile)
        print()

        confirmString = str(input("Please type (Yes) or (No) to confirm: "))

    # Did you type an invalid response? You will go through this if-statement, then.
    if (confirmString == "" or confirmString != "No" or confirmString != "no" or confirmString != "Yes" or confirmString != "yes"):

        attempts += 1 # Increase non-appending attempts by one.
        totalAttempts -= 1 # Reduce your amount of attempts remaining by one.

        print("-----------------------------------------------------------------------------------------------------------------------")
        print("That's not a proper response! Don't just press enter!")
        print("You have " + str(totalAttempts) + " attempt(s) remaining until program termination.")
        print()

        confirmString = str(input("Please type (Yes) or (No) to confirm: "))

        # Did you run out of attempts? You will go through this if-statement, then.
        if (attempts == 2):

            sys.exit("Number of attempts succeeded... Terminating program.") # sys.exit() will cause the program's prccess to
                                                                             # to immediately terminate making the program stop.

print("-----------------------------------------------------------------------------------------------------------------------")


#------------------------------------------------------------------------------------------------------------------------


# Creating and writing to the file.
# This section will not only CREATE your file, but it will write all content that you supply to the system.
# You will be instructed to periodically check your computer for the file. Note the differences between
# PyCharm and IDLE's interfaces.

print("Now that you're satisfied with the name of your file, we're going to create it.")
print("Please give the program five seconds to create and authenticate your file...")

time.sleep(5) # Once again, to control CPU usage.
openWriteFile = open(fullFile, "w+") # "w+" means we're putting it into "write" mode but allowing for reading, additionally.

print("-----------------------------------------------------------------------------------------------------------------------")

# Verifying successful creation of the file and prompting the user to check their computer to search for it.
print("Success! Please search for a file called " + fullFile + " on your computer. PyCharm won't show the file in the IDE until we're")
print("done writing to the file (that includes additional appended content as well).")
print()

# Importing user input to the newly created file. You will be able to append (add) more information to your file later.
print("Now let's give that file of yours some text. It's feeling rather empty right now!")
fileContents = str(input("Please type some content to insantiate into the file (it can be however long you'd like it to be): "))
print()

print("Please give the program ten seconds to create, authenticate, and append your contents to the newly created file.")
print("-----------------------------------------------------------------------------------------------------------------------")

time.sleep(10) # Once again, to control CPU usage.
openWriteFile.write(fileContents + "\n") # All lines will be stored on new lines for final output.

# Verifying successful appending of user input to the file and prompting the user to verify the first portion of the file is there.
print("Another success! Why don't you search and open a file called " + fullFile + " on your computer? It should have been created and possibly have text in it, now.")

#------------------------------------------------------------------------------------------------------------------------


# Appending MORE user input. NOTE that all the input has been string-based. You can use integers or floating-point as
# it will be converted to a string format.

finalConfirm = str(input("Would you like to add anything else to your file? Please type (Yes) or (No): "))

# Once again, while you have don't have more than three attempts.
while (finalAttempts != 2):

    # Did you type yes? You'll go through this if-statement, then.
    if (finalConfirm == "Yes" or finalConfirm == "yes"):

        print("-----------------------------------------------------------------------------------------------------------------------")

        openWriteFile = open(fullFile, "a+")

        fileContents = str(input("Please type some content to insantiate into the file (it can be however long you'd like it to be): "))
        print()

        print("Please give the program ten seconds to create, authenticate, and append your contents to the newly created file.")

        time.sleep(10)
        openWriteFile.write(fileContents + "\n")
        print("Contents appended to file, successfully.")

        print("-----------------------------------------------------------------------------------------------------------------------")
        finalConfirm = str(input("Would you like to add anything else to your file? Please type (Yes) or (No): "))
        continue # Returns the if-statement to the top of the while-loop again, allowing for infinite user input.

    # Did you type no? You'll go through this if-statement, then.
    if (finalConfirm == "No" or finalConfirm == "no"):

        print("-----------------------------------------------------------------------------------------------------------------------")

        print("I totally understand! Here's your full file contents:")
        print()

        openWriteFile = open(fullFile, "r")
        print(openWriteFile.read())

        print("Terminating program.")
        print("-----------------------------------------------------------------------------------------------------------------------")

        openWriteFile.close() # Close the file.
        break # Fall out of the while-loop, and end the program.

    # Did you type an invalid response? You will go through this if-statement, then.
    if (finalConfirm == "" or finalConfirm != "No" or finalConfirm != "no" or finalConfirm != "Yes" or finalConfirm != "yes"):

        finalAttempts += 1
        totalFinalAttempts -= 1

        print("-----------------------------------------------------------------------------------------------------------------------")

        print("That's not a proper response! Don't just press enter!")
        print("You have " + str(totalFinalAttempts) + " attempt(s) remaining until program termination.")
        print()

        confirmString = str(input("Please type (Yes) or (No) to confirm: "))

        # Did you run out of attempts? You will go through this if-statement, then.
        if (finalAttempts == 2):

            print()
            sys.exit("Number of attempts succeeded... Terminating program.")
            print("-----------------------------------------------------------------------------------------------------------------------")


#------------------------------------------------------------------------------------------------------------------------
