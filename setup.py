import telepot
import sys, time
from pprint import pprint
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from telepot.delegate import per_chat_id, create_open, pave_event_space, include_callback_query_chat_id



class Calculator(telepot.helper.ChatHandler):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[
                   InlineKeyboardButton(text='Uomo', callback_data='uomo'),
                   InlineKeyboardButton(text='Donna', callback_data='donna'),
                ]])

    
    def __init__(self, *args, **kwargs):
        super(Calculator, self).__init__(*args, **kwargs)
        self._anni = 0
        self._peso = 0
        self._altezza = 0
        self._gender = None
        self._meta = 0
        self._count = -2


    def calcolaMet(self):
        if self._gender == "uomo":
            if self._anni <= 9:
                self._meta = 22.7*self._peso + 504
                self.sender.sendMessage("Il tuo metabolismo basale è di "+str(self._meta)+" kcal")
            if self._anni <= 17 and self._anni > 9:
                self._meta = 17.7*self._peso + 650
                self.sender.sendMessage("Il tuo metabolismo basale è di "+str(self._meta)+" kcal")
            if self._anni <= 29 and self._anni > 17:
                self._meta = 15.3*self._peso + 679
                self.sender.sendMessage("Il tuo metabolismo basale è di "+str(self._meta)+" kcal")
            if self._anni <= 59 and self._anni > 29:
                self._meta = 11.6*self._peso + 879
                self.sender.sendMessage("Il tuo metabolismo basale è di "+str(self._meta)+" kcal")
            if self._anni <= 74 and self._anni > 59:
                self._meta = 11.9*self._peso + 700
                self.sender.sendMessage("Il tuo metabolismo basale è di "+str(self._meta)+" kcal")
            if self._anni > 75:
                self._meta = 8.4*self._peso + 819
                self.sender.sendMessage("Il tuo metabolismo basale è di "+str(self._meta)+" kcal")
        if self._gender == "donna":
            if self._anni < 9:
                self._meta = 20.3*self._peso + 485
                self.sender.sendMessage("Il tuo metabolismo basale è di "+str(self._meta)+" kcal")
            if self._anni <= 17 and self._anni > 9:
                self._meta = 13.4*self._peso + 693
                self.sender.sendMessage("Il tuo metabolismo basale è di "+str(self._meta)+" kcal")
            if self._anni <= 29 and self._anni > 17:
                self._meta = 14.7*self._peso + 496
                self.sender.sendMessage("Il tuo metabolismo basale è di "+str(self._meta)+" kcal")
            if self._anni <= 59 and self._anni > 29:
                self._meta = 8.7*self._peso + 829
                self.sender.sendMessage("Il tuo metabolismo basale è di "+str(self._meta)+" kcal")
            if self._anni <= 74 and self._anni > 59:
                self._meta = 9.2*self._peso + 688
                self.sender.sendMessage("Il tuo metabolismo basale è di "+str(self._meta)+" kcal")
            if self._anni > 75:
                self._meta = 9.8*self._peso + 624
                self.sender.sendMessage("Il tuo metabolismo basale è di "+str(self._meta)+" kcal")               
                

        self.close()
                
            

    def on_chat_message(self, msg):
        self._count += 1
        content_type, chat_type, chat_id = telepot.glance(msg)
        if self._count == -1:
            self.sender.sendMessage('Inserisci la tua età..')
        if self._count == 0:
            try:
                self._anni=int(msg["text"])
                self.sender.sendMessage("Inserisci la tua altezza in cm..")
            except ValueError:
                self.sender.sendMessage("Formato età non corretto")
                self.sender.sendMessage('Inserisci la tua età.. (ho bisogno di un numero. Esempio: 33, 20, 17 ...anni)')
                self._count -= 1
        if self._count == 1:
            try:
                self._altezza = float(msg["text"])
                self.sender.sendMessage("Inserisci il tuo peso in kg..")
            except ValueError:
                self.sender.sendMessage("Formato altezza non corretto")
                self.sender.sendMessage("Inserisci la tua altezza in cm (esempio: 160.3, 185, 172 ...cm)..")
                self._count -= 1
        if self._count == 2:
            try:
                self._peso = int(msg["text"])
                
                self.sender.sendMessage("Quale è il tuo sesso?", reply_markup=self.keyboard);
            except ValueError:
                self.sender.sendMessage("Formato peso non corretto")
                self.sender.sendMessage("Inserisci il tuo peso in kg (esempio: 75.4, 80, 90 ...kg)..")
                self._count -= 1
            

    def on_callback_query(self, msg):
        query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
        if query_data == 'uomo':
            self._gender = "uomo"
        if query_data == "donna":
            self._gender = "donna"
        self.calcolaMet()



#"1005610092:AAHU9mg1-_qb7VB0SJ8XPtUN4CUaIPDjLwM"
        

bot = telepot.DelegatorBot("1005610092:AAHU9mg1-_qb7VB0SJ8XPtUN4CUaIPDjLwM", [
    include_callback_query_chat_id(
        pave_event_space())(
            per_chat_id(types=['private']), create_open, Calculator, timeout=20),
])
MessageLoop(bot).run_as_thread()

while 1:
    time.sleep(10)
