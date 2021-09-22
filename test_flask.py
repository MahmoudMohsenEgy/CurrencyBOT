#Importing the libraries
import eventlet
eventlet.monkey_patch(os=False,thread = False)
from flask import Flask, redirect, url_for, render_template
from flask_socketio import SocketIO, send,emit
import time

import bot
import speech_recognition_test
import text_to_speech

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app,cors_allowed_origins='*')



#Handle the message coming from the front end 
@socketio.on('message')
def handleMessage(msg):
    #get the user message
    print('Message: ' + msg)
    #emit('message',speech_recognition_test.listen(),broadcast=True)
    user_msg = "You: " + str(msg)
    send(user_msg, broadcast=True)
    #get the bot response
    status,response = bot.chat(msg)
    print(response)
    response_bot = "Bot: " + str(response)
    time.sleep(1)
    #send the bot response to the client
    emit('message',response_bot,broadcast=True)
    #eventlet.spawn(text_to_speech.talk,response)
    eventlet.sleep(0.2)
    text_to_speech.talk(response)
    eventlet.sleep(2)
    socketio.sleep(0.1)

   
    
    

#handle the voice messages from the client
@socketio.on('mic')
def handleVoice(data):
    #process the client speech to text
    mesg = speech_recognition_test.listen()
    eventlet.sleep(0.2)
    #send the user text to print it client view
    emit('mic',mesg)

@app.route("/")
def myBOT():
    return render_template("index.html")




if __name__ == "__main__":
    socketio.run(app,debug=True,port=5000)
