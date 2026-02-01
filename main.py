import telebot, os, random, images

bot = telebot.Telebot("TOKEN")

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}!')


@bot.message_handler(commands=['eco'])
def send_eco(message):
    random_images =random.choice(os.listdir("images"))
    with open(f'images/{random_images}', 'rb') as f:  
        bot.send_photo(message.chat.id, f) 

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")
    bot.register_next_step_handler(message, send_password)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)



bot.polling()
