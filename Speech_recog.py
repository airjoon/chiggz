#import library
import speech_recognition as sr

r = sr.Recognizer()
# Reading Audio file as source
with sr.AudioFile(r"C:\Users\somes\OneDrive\Desktop\Speech bro\phonerec.wav") as source:
    audio_text = r.listen(source)
    try:
        # using google speech recognition
        text = r.recognize_google(audio_text)
        print(text)
    except:
         print('Sorry.. run again...')