import telepot
import sys, time
from pprint import pprint



def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(chat_id, content_type, chat_type)

    if content_type == "text":
        bot.sendMessage(chat_id, msg["text"])

bot = telepot.Bot("1005610092:AAHU9mg1-_qb7VB0SJ8XPtUN4CUaIPDjLwM")
bot.message_loop(handle)
while 1:
    time.sleep(3)
