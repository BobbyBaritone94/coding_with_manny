import speech_recognition as sr
import subprocess



recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak something...")
    # Optional: adjust for ambient noise levels
    recognizer.adjust_for_ambient_noise(source)
    # Listen for audio and store it in the audio_data variable
    audio_data = recognizer.listen(source)
    print("Time over, thanks.")

def process_words(list_of_words):
    if "echo" in list_of_words:
        index_of_echo = list_of_words.index("echo")
        cmd = " ".join((["echo"] + list_of_words[index_of_echo:]))
        print(cmd)
        subprocess.run(cmd,shell=True)
    elif "play" in list_of_words:
        if "raiders" in list_of_words or "ark" in list_of_words:
            subprocess.run("E:\SteamLibrary\steamapps\common\Arc Raiders\PioneerGame.exe")

    

# Convert speech to text
try:
    # Use Google Web Speech API for transcription
    text = recognizer.recognize_google(audio_data)
    text = text.lower()
    
    print(text)
    list_of_words = text.split()
    process_words(list_of_words)
except sr.UnknownValueError:
    # Handle cases where the speech was unintelligible
    print("Sorry, I did not get that.")
except sr.RequestError:
    # Handle API request errors (e.g., network issues)
    print("Could not connect to Google API.")

# if __name__ == "__main__":
#     pass