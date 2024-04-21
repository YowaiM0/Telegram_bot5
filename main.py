import telebot  # импорт библиотеки для работы с Telegram API
import random  # импорт библиотеки для работы с рандомом
from telebot import types  # импорт подмодуля для работы с кнопками
from bot_token import TOKEN
bot = telebot.TeleBot(TOKEN)

    # обработчик команды start
@bot.message_handler(commands=['start'])
def start_command(message):
    # создаем экземпляр inline-клавиатуры
    inline_keyboard = types.InlineKeyboardMarkup()  
    buttons = []  
    
    # добавляем 5 кнопок
    for i in range(5):  
        buttons.append(types.InlineKeyboardButton(text="🍪", callback_data=str(i)))
     
    # добавляем их в клавиатуру
    inline_keyboard.row(*buttons) 
    bot.send_message(message.chat.id, 'Что выберешь?', reply_markup=inline_keyboard)
    

# обработчик событий кнопок
@bot.callback_query_handler(func=lambda call: True)  
def callback_query(call):
    if call.data == str(random.randint(0, 4)):  
        bot.send_message(call.message.chat.id, 'Поздравляю, ты победил! 🥳 ')  # отправить сообщение о выигрыше
    else: # отправить сообщение о проигрыше
        bot.send_message(call.message.chat.id, 'Увы, ты проиграл!😿') 


if __name__ == '__main__':
    bot.infinity_polling()  
 
