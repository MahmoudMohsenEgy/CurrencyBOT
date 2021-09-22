from rivescript import RiveScript
import xlwt
import os.path
file = os.path.dirname(__file__)
Brain = os.path.join(file, 'brain')


bot = RiveScript(utf8=True)
bot.load_directory(Brain)
bot.sort_replies()
def chat(message):
    if message == "":
        return -1,"No message found"
    else:
        response = bot.reply("user",message)
    if response:
        return 0, response
    else:
        return -1,"No response found"
""" while True :
    msg = str(input("User: "))
    reply = str(bot.reply('localuser',msg))
    if msg == "quit":
        break
    else:
        print("Bot :" + reply) """
