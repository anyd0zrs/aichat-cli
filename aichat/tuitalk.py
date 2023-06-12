import pyttsx3
import subprocess
import pyaudio
import time
import os


def main():
    os.system("cls")
    print("================================================================")
    print("|                        VOICE ASSISTANT                        |")
    print("================================================================")
    print("\nComputer: Ready")
    while True:
        # Get a command from the user
        print("\nEnter a command to get started:\n")
        command = input("> ").strip().lower()

        # Check if the user wants to exit
        if command == "exit":
            print("\nGoodbye!")
            return

        # Check if the user wants help
        if command == "help":
            print("\n----------------------------------------------------------------")
            print("| Commands:                                                     |")
            print("----------------------------------------------------------------")
            print("|   help    - show this help message                            |")
            print("|   exit    - exit the voice assistant                           |")
            print("----------------------------------------------------------------")
            continue

        # Call the gpt_cli.py script and capture its output
        output = subprocess.check_output(["python", "chatcli.py","-b","sage","-m",command])

        # Decode the output and pass it to pyttsx
        response = output.decode().strip()
        engine = pyttsx3.init()
        engine.say(response)
        engine.runAndWait()

        # Print the output for the user to see
        print("\n" + response + "\n")
		
if __name__ == "__main__":
    main()
