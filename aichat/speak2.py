import pyttsx3
import subprocess
import vosk
import pyaudio
import time
import os

model = vosk.Model("vosk-model-small-en-us-0.15")
recognizer = vosk.KaldiRecognizer(model, 16000)
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)

def listen():
    # Listen for a command
    while True:
        data = stream.read(8000)
        if recognizer.AcceptWaveform(data):
            # When a command is recognized, return it
            result = recognizer.Result()
            return result.strip()

def main():
    # Wait for the wake word
    print("Computer: Ready")
    while True:
        data = stream.read(8000)
        if recognizer.AcceptWaveform(data):
            # When the wake word is detected, beep to indicate readiness
            if "computer" in recognizer.Result():
                # play(beep)
                print("Wake word detected! Listening!")
                while True:
                    command = listen()
                    print(f"You said: {command}")
                    # Call the gpt_cli.py script and capture its output
                    output = subprocess.check_output(["python", "chatcli.py","-b","sage","-m",command])
                    # Decode the output and pass it to pyttsx
                    response = output.decode().strip()
                    engine = pyttsx3.init()
                    engine.say(response)
                    engine.runAndWait()
                    print("\n")
                    print(response)
                    print("\n")
                break
            else:
                continue

if __name__ == "__main__":
    main()
