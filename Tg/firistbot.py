import telebot
from telebot import types

import emoji
import config
sitee="https://www.google.com/search?q="
bot=telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=["start"])
def start_answer(message):

    markup=types.InlineKeyboardMarkup()
    btn1=types.InlineKeyboardButton("Найти это в гугле", callback_data="search")
    markup.row(btn1)
    bot.reply_to(message, f"Привет {message.from_user.first_name} {message.from_user.last_name}!", reply_markup=markup)
@bot.message_handler(commands=["info", "about"])
def about(message):
    bot.send_message(message.chat.id, "Это мой первый бот, пока функционал у него не большой"+ emoji.emojize(":brain:"))
@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, "Команды:\n/start\n/about\n/help")
@bot.callback_query_handler(func=lambda callback: True)
def callback(callback):
    if callback.data =='search':
        bot.send_message(callback.message.chat.id, "Напиши /search и свой запрос")
@bot.message_handler(commands=["search"])
def search(message):
    bot.send_message(message.chat.id, "Напиши свой запрс")
@bot.message_handler()
def search(message):
    text=
bot.polling(none_stop=True)
