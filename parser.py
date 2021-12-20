import requests
import json

url = 'https://api.openweathermap.org/data/2.5/weather?q=Kyiv,ua&units=metric&APPID=b9e768fe75159a0c020507dc43b1a5d5'

response = requests.get(url)
json_data = json.dumps(json.loads(response.text))
decode_data = json.loads(json_data)
print(decode_data["name"], decode_data["main"]["temp"])

import telebot

bot = telebot.TeleBot('5081259300:AAFPcn1n5aVuL3iTVG17QNPK001qeMp0uSI')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
  if message.text == "Привет":
      bot.send_message(message.from_user.id, "Привет, сейчас я расскажу тебе погоду в Киеве, нажки ОК")
  elif message.text == "ОК":
      bot.send_message(message.from_user.id, str(decode_data["name"]) + " " + str(decode_data["main"]["temp"]) + " " + "\N{DEGREE SIGN}" + "C")





bot.polling(none_stop=True, interval=0)
