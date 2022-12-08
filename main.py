import os
from dotenv import load_dotenv
import telebot
from MA_trader import get_image

load_dotenv()

API_KEY = os.environ.get("API_KEY")
bot = telebot.TeleBot(API_KEY)

PAIRS = ["BNBUSDT", "ETHUSDT", "BTCUSDT"]


def filter_correct_pair(message):
    request = message.text
    if request not in PAIRS:
        return False
    else:
        return True


def filter_wrong_pair(message):
    request = message.text
    if request in PAIRS:
        return False
    else:
        return True


@bot.message_handler(commands=["list"])
def send_current_list(message):
    bot.send_message(message.chat.id, f"Current list of pairs: {PAIRS}")


@bot.message_handler(func=filter_correct_pair)
def send_image(message):
    try:
        request = message.text.split()[-1]
        bot.send_message(message.chat.id, "Your result.")
        bot.send_photo(message.chat.id, get_image(request))
    except telebot.apihelper.ApiTelegramException:
        bot.send_message(
            message.chat.id,
            "Sorry, seems something go wrong, try one more time please.",
        )


@bot.message_handler(func=filter_wrong_pair)
def wrong_pair(message):
    bot.send_message(
        message.chat.id,
        "Please input correct value of trading pair, to see all current pairs input /list",
    )


bot.polling()
