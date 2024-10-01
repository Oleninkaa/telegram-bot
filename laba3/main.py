import telebot
from telebot import  types


bot = telebot.TeleBot('7024788733:AAGsyXgJXBJ2fftgl1wqe3IhZ9JWdScoSoU')


class Command:
  def __init__(self, title, text):
    self.title = title
    self.text = text

commands_count = 4

Student = Command("student", 'студентка групи ІС-13 <b><u>Росновська Ольга</u></b>')
Technologies = Command("it-technologies", "<b>IT-технології:</b> Front-end Back-end WEB-технології")
Contacts = Command("contacts", "Контакти\n"
                               "• телефон: 050-332-45-20\n"
                               "• пошта: rosnovska.olha@lll.kpi.ua")

GPT = Command("chat gpt", "fgfgfg")


@bot.message_handler(commands=['start'])
def main(message):
    welcome = 'Ласкаво просимо у чаті! Оберіть команду:'
    commands_list = [Student, Technologies, Contacts, GPT]

    markup = types.InlineKeyboardMarkup()
    for element in commands_list:
        markup.add(types.InlineKeyboardButton(element.title, callback_data=element.title))
    bot.send_message(message.chat.id, welcome, reply_markup=markup)


@bot.callback_query_handler(func=lambda callback:True)
def callback_message(callback):
    if callback.data == Student.title:
        bot.send_message(callback.message.chat.id, Student.text, parse_mode='html')
    elif callback.data == Technologies.title:
        bot.send_message(callback.message.chat.id, Technologies.text,  parse_mode='html')
    elif callback.data == Contacts.title:
        bot.send_message(callback.message.chat.id, Contacts.text,  parse_mode='html')

bot.polling(none_stop=True)