import telebot

from cons import API_KEYS

bot = telebot.TeleBot(API_KEYS,parse_mode=None)

@bot.message_handler(commands=["help", "start"])
def send_help_message(msg):
    bot.reply_to(msg, "Welcome to the help section! Here are the available command:"
                      "\n\n"
                      "\n/help - Show the help message"
                      "\n/advisory - Show advisory message"
                      "\n/with_address - Show advisory with exact area")

@bot.message_handler(commands=["advisory"])
def send_multi_message(msg):
    bot.reply_to(msg, "DCTECH ADVISORY \n\nDearest Client, \nKindly be informed that we are experiencing Intermittent to No Internet Connection on some areas of  due to a cause yet to be determined. Our engineers are already checking the issue. \n\nAffected Areas: \n\nWe sincerely apologise for any inconvenience this may cause you. Rest assured that our team is resolving this matter with urgency and we will update you of any resolution progress.\n\n\nThank you.")

@bot.message_handler(commands=['with_address'])
def send_welcome(message):
    bot.reply_to(message, 'Please input the area: ')

    # Register the next step handler
    bot.register_next_step_handler(message, insert_name)

def insert_name(message):
    name = message.text

    # Use the name in a message and send it to the user
    message_text = f"The affected area is {name}!"
    bot.send_message(message.chat.id, message_text)

bot.polling()
