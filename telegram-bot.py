import telebot
import requests


from additions_functions import print_exercise, create_voice_file


TELEGRAM_API_TOKEN = "*******************"
bot = telebot.TeleBot(TELEGRAM_API_TOKEN)


user = bot.get_me()
print(user)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "How is it going?")


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "How I can help you?")



@bot.message_handler(commands=['exercise'])
def send_exercise(message):
    try:
        if message.text == '/exercise':
            bot.reply_to(message, 'If you want to look certain exercise, please send me the message in as provide below format: "/exercise [exercise_name]"')
            var = print_exercise('/home/abalabay/telebot/exercises/Exercises.txt')
            bot.reply_to(message, 'Viewable exercises: \n{}'.format(var))
        else:
            try:
                command, num = message.text.split()
                if num:
                    var = print_exercise('/home/abalabay/telebot/exercises/Exercise_{}.txt'.format(num))
                    bot.reply_to(message, var)
                else:
                    bot.reply_to(message, 'I can\'t find this exercise... :(')
            except ValueError or FileNotFoundError:
                bot.reply_to(message, 'Bad news!')
    except ValueError or FileNotFoundError:
        bot.reply_to(message, 'Bad news!')


@bot.message_handler(commands=['Esenin'])
def send_Esenin(message):
    chat_id    = message.chat.id
    audio_file = open('/home/abalabay/telebot/audio/Esenin_voice.ogg', 'rb')
    bot.send_audio(chat_id, audio_file)
    audio_file.close()
    
@bot.message_handler(commands=['fairy_tail'])
def send_fairy_tail(message):
    if message.text == '/fairy_tail':
        bot.reply_to(message,'If you want listen to certain fairy tail, please send me the message in as provide below format: "/fairy_tail [fairy_tail_name]"')
        var = print_exercise('/home/abalabay/telebot/audio/fairy_tail/fairy_tail.txt')
        bot.reply_to(message, 'Viewable fairy tails: \n{}'.format(var))
    else:
        try:
            command, num = message.text.split()
            if num:
                chat_id    = message.chat.id
                audio_file = open('/home/abalabay/telebot/audio/fairy_tail/{}.mp3'.format(num), 'rb')
                bot.send_audio(chat_id, audio_file)
                audio_file.close()
            else:
                bot.reply_to(message, 'I can\'t find this fairy tail... :(')
        except ValueError:
                bot.reply_to(message, 'It is very difficult for me)')

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)



@bot.message_handler(content_types=['voice'])
def voice_processing(message):
    chat_id    = message.chat.id
    file_info  = bot.get_file(message.voice.file_id)
    file = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(TELEGRAM_API_TOKEN, file_info.file_path))
    create_voice_file(file.content)
    audio_file = open('/home/abalabay/telebot/audio/processed_voice.ogg', 'rb')
    bot.send_audio(chat_id, audio_file)


bot.polling()
