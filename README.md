# calcolametabolismo_bot
This Python code defines a Telegram bot that acts as a calculator for estimating Basal Metabolic Rate (BMR) based on age, gender, height, and weight provided by the user. It utilizes the Telepot library to interact with the Telegram Bot API.

The Calculator class inherits from telepot.helper.ChatHandler, which is a Telepot handler for handling chat messages. The class includes methods for calculating BMR (calcolaMet) based on gender and age, and for interacting with the user via Telegram messages (on_chat_message and on_callback_query).

Upon receiving a chat message, the bot prompts the user to input their age, height, and weight. It validates each input and prompts for the next piece of information. After receiving all necessary information, it presents the user with a keyboard to select their gender. Upon gender selection, the BMR is calculated and sent to the user via a Telegram message.

The bot continuously runs using MessageLoop to listen for incoming messages. It utilizes time.sleep(10) to prevent excessive CPU usage by waiting 10 seconds between iterations.
