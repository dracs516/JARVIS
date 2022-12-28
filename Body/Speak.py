# Windows Based

import pyttsx3


def Speak(Text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    engine.setProperty("voices", voices[0].id)
    engine.setProperty("rate", 170)
    print("")
    print(f"You said: {Text}")
    print("")
    engine.say(Text)
    # engine.save_to_file()
    engine.runAndWait()


Speak("My name is Abhay Jha")