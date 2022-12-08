from random import randint, choice
import requests

PAPER_TRADE_URL = "https://paper-trader.frwd.one/"
timeframe = ["5m", "15m", "1h", "4h", "1d", "1w", "1M"]


def stock_request(message):
    data = {
        "pair": message,
        "timeframe": choice(timeframe),
        "candles": randint(0, 1000),
        "ma": randint(0, 100),
        "tp": randint(0, 100),
        "sl": randint(0, 100),
    }
    return data


def get_image(message):
    response = requests.post(PAPER_TRADE_URL, stock_request(message))
    start = response.text.find("images")
    end = response.text.find(".png") + 4
    image_url = PAPER_TRADE_URL + response.text[start:end]
    return image_url
