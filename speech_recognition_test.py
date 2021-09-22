
import speech_recognition as sr
r = sr.Recognizer()
""" while True:
    with sr.Microphone() as source:
        print("Say anything :")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("you said : {}".format(text))
        except:
            print("Sorry cant recognize say it again")
        if text == 'exit':
            break """
def listen():
    print("Say anything :")
    
    with sr.Microphone() as source:
        print("A")
        audio = r.listen(source)
        print("N")
        try:
            print("D1")
            text = r.recognize_google(audio)
            print("D2")
            print("You said : "+ text)
            return text
        except:
            return "I can't hear your message !"
def listen2():
    print("Say anything :")
    with sr.Microphone() as source:
        r = sr.Recognizer()
        r.adjust_for_ambient_noise(source)
        print("A")
        audio = r.listen(source)
        print("N")
        try:
            text = r.recognize_google(audio)
            print("returning audio "+text)
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
      
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
