import telebot
import random
bot = telebot.TeleBot('1682063637:AAFABXs7jHTk-2_u-IXw1RXeD2cJjR6XCfI')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Все разряды', '1СП', '2СП', '3СП', '1ЮН', '2ЮН', '3ЮН')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_sticker(message.chat.id, 'CAACAgQAAxkBAALQ7mAlGEtITFceNnZgY9UG0HhifROSAAIQCAAC3kD4B6dTmKf1ol1iHgQ', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == '1сп':
        bot.send_message(message.chat.id, '1.'+str(random.randint(1, 2)))
        bot.send_message(message.chat.id, '2')
    elif message.text.lower() == '2сп':
        bot.send_message(message.chat.id, '3.'+str(random.randint(1, 2)))
        bot.send_message(message.chat.id, '4.' + str(random.randint(1, 2)))
        bot.send_message(message.chat.id, str(random.randint(5, 6)))
    elif message.text.lower() == '3сп':
        bot.send_message(message.chat.id, '7.' + str(random.randint(1, 2)))
        bot.send_message(message.chat.id, '8.' + str(random.randint(1, 3)))
        bot.send_message(message.chat.id, '9.' + str(random.randint(1, 2)))
        bot.send_message(message.chat.id, '10')
    elif message.text.lower() == '1юн':
        bot.send_message(message.chat.id, str(random.randint(11, 12)))
        bot.send_message(message.chat.id, '13')
        bot.send_message(message.chat.id, '14.' + str(random.randint(1, 2)))
    elif message.text.lower() == '2юн':
        bot.send_message(message.chat.id, str(random.randint(15, 16)))
        bot.send_message(message.chat.id, str(random.randint(17, 18)))
        bot.send_message(message.chat.id, str(random.randint(19, 20)))
        bot.send_message(message.chat.id, '21')
    elif message.text.lower() == '3юн':
        bot.send_message(message.chat.id, str(random.randint(22, 23)))
        bot.send_message(message.chat.id, str(random.randint(24, 25)))
        bot.send_message(message.chat.id, str(random.randint(26, 27)))
        bot.send_message(message.chat.id, str(random.randint(28, 29)))
    elif message.text.lower() == 'все разряды':
        bot.send_message(message.chat.id, '1СП')
        bot.send_message(message.chat.id, '1.' + str(random.randint(1, 2)))
        bot.send_message(message.chat.id, '2')
        bot.send_message(message.chat.id, '2СП')
        bot.send_message(message.chat.id, '3.' + str(random.randint(1, 2)))
        bot.send_message(message.chat.id, '4.' + str(random.randint(1, 2)))
        bot.send_message(message.chat.id, str(random.randint(5, 6)))
        bot.send_message(message.chat.id, '3СП')
        bot.send_message(message.chat.id, '7.' + str(random.randint(1, 2)))
        bot.send_message(message.chat.id, '8.' + str(random.randint(1, 3)))
        bot.send_message(message.chat.id, '9.' + str(random.randint(1, 2)))
        bot.send_message(message.chat.id, '10')
        bot.send_message(message.chat.id, '1ЮН')
        bot.send_message(message.chat.id, str(random.randint(11, 12)))
        bot.send_message(message.chat.id, '13')
        bot.send_message(message.chat.id, '14.' + str(random.randint(1, 2)))
        bot.send_message(message.chat.id, '2ЮН')
        bot.send_message(message.chat.id, str(random.randint(15, 16)))
        bot.send_message(message.chat.id, str(random.randint(17, 18)))
        bot.send_message(message.chat.id, str(random.randint(19, 20)))
        bot.send_message(message.chat.id, '21')
        bot.send_message(message.chat.id, '3ЮН')
        bot.send_message(message.chat.id, str(random.randint(22, 23)))
        bot.send_message(message.chat.id, str(random.randint(24, 25)))
        bot.send_message(message.chat.id, str(random.randint(26, 27)))
        bot.send_message(message.chat.id, str(random.randint(28, 29)))

bot.polling()