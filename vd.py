import requests
import json

from telegram.bot import Bot

bot = Bot(token=6187904430:AAHRxXjkXSlFmcT8OrvZyWGF7suVZBiJfww)

@bot.message_handler(commands=['video'])
def download_video(message):
    video_url = message.text

    response = requests.get(video_url)

    if response.status_code == 200:
        video_file = response.content

        bot.send_document(message.chat.id, video_file)

    else:
        bot.send_message(message.chat.id, 'Error downloading video.')

bot.polling()