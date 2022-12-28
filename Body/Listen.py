# Input - Command can be in Hindi oe English
# Output - English

import speech_recognition as sr
from googletrans import Translator


# Listen in Hindi or English
def Listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, 0, 8)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="hi")

    except:
        return ""

    query = str(query).lower()
    return query


# print(Listen())


def TranslationHindiToEnglish(Text):
    line = str(Text)
    translate = Translator()
    result = translate.translate(line)
    data = result.text
    print(f"Yoy said: {data}.")
    return data


# TranslationHindiToEnglish("मेरा नाम अभय झा हो")


# Mic
def MicExecution():
    query = Listen()
    data = TranslationHindiToEnglish(query)
    return data


MicExecution()
