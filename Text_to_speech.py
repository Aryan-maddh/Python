import pyttsx3

sr = pyttsx3.init()

def speak(text):
    sr.say(text)
    sr.runAndWait()



with open("Project/speech/speech.txt","r") as f:
    text=f.readlines()


# text=input("Enter You want to listen")
speak(text)