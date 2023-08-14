import telebot
from config import keys, TOKEN
from extensions import ConvertionException, CryptoConverter

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Привет! Чтобы начать работу введи в одну строку команду боту в формате:\n<имя волюты>\n \
<в какую валюту перевести>\n \
<количество валюты>\nЧтобы увидеть список всех доступных валют отправь команду: /values \n \
для повторного получения подсказки отправь команду: /help \n \
P.S. будь внимателен, данному боту нельзя отправлять войсы и фоточки =P'

    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def help(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ConvertionException('Не корректные параметры запроса!')

        quote, base, amount = values
        total_base = CryptoConverter.convert(quote, base, amount)
    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {amount} {quote} в {base} = {total_base}'
        bot.send_message(message.chat.id, text)

@bot.message_handler(content_types=['photo', ])
def say_lmao(message: telebot.types.Message):
    bot.reply_to(message, 'Nice meme XDD')

@bot.message_handler(content_types=['voice', ])
def say_lmao(message: telebot.types.Message):
    bot.reply_to(message, 'Я бы поговорил с тобой, но мне некогда, я занят конвертацией =(')

bot.polling(none_stop=True)