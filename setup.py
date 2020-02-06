import telepot
import sys, time
from pprint import pprint



def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    
    if content_type == "text" && msg["text"] == "/start":
        bot.sendMessage(chat_id, "Benvenuto, qui puoi calcolare il tuo metabolismo basale!\n") 

bot = telepot.Bot("1005610092:AAHU9mg1-_qb7VB0SJ8XPtUN4CUaIPDjLwM")
bot.message_loop(handle).run_as_thread()
print("ok")

while 1:
    time.sleep(3)
