import speech_recognition as sr
import webbrowser
import pyttsx3
import music


recognizer = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')

# for index, voice in enumerate(voices):
#     print(f"Voice {index}: {voice.name} ({voice.id})")
# engine.setProperty('voice', voices[0].id)
# engine.setProperty('rate', 150)
# engine.setProperty('volume', 1.0)


def speak(text):
    engine.say(text)
    engine.runAndWait()
def process(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
        speak("ok Aarayan")
    elif "open whatsapp" in c.lower():
        webbrowser.open("https://whatsapp.com")
        speak("ok Aarayan")
    
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
        speak("ok Aarayan")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
        speak("ok Aarayan")
    elif "open apex" in c.lower():
        webbrowser.open("https://apexnexon.tech")
        speak("ok Aarayan")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
        speak("ok Aarayan")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=music.music[song]
        webbrowser.open(link)
       
         

if __name__== "__main__":
    speak("Hey... Arayan How May I Help you ?")
    #listen for the wake word
    while True:
            r=sr.Recognizer()
       
            print("recognizing..")
            try:
                 with sr.Microphone() as source:
                   print("Say Something")
                   audio=r.listen(source,timeout=2,phrase_time_limit=1)
                 word=r.recognize_google(audio)
                 print(word)
                 if(word=="hello"):
                      speak("YA")
                      with sr.Microphone() as source:
                        print("Say Something")
                        audio=r.listen(source)
                        command=r.recognize_google(audio)

                        process(command)
                      #listen for command

                #  print(command)
                # print("Sphinx thinks you said "+ r.recognize_sphinx(audio))
    
            except Exception as e:
                print("Sphinx error : {0}".format(e))