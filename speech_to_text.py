import pyttsx3
import speech_recognition as sr

recognise=sr.Recognizer()
gin = pyttsx3.init()

def speak(text):
    gin.say(text)
    gin.runAndWait()



if __name__ == "__main__":
    speak("Hey... Aryan speak that You want to convert in text?")
    #listen for the wake word
    # n=input("Enter Your siri name")
    # print(n)
    while True:
            r=sr.Recognizer()
       
            print("recognizing..")
            try:
                 
                 with sr.Microphone() as source:
                   print("Say Something")
                   audio=r.listen(source,timeout=2,phrase_time_limit=1)
                 word=r.recognize_google(audio)
                 print(word)
                 with open ("text.txt","w") as f:
                      f.write(word)
                      
                      
            except Exception as e:
                print("Sphinx error : {0}".format(e))