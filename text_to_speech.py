import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

def talk(msg):
    
    if engine._inLoop:
        print("engine will end the loop")
        engine.endLoop() 
        print("engine loop ended!")
    engine.say(msg)
    engine.runAndWait()
    

