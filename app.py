import json

from flask import Flask
from binance import Client
from binance.enums import *

client = Client("buraya api key",
                "buraya secret key")

order = client.create_order(
    symbol='BNBBUSD',
    side=SIDE_BUY,
    type=ORDER_TYPE_LIMIT,
    timeInForce=TIME_IN_FORCE_GTC,
    quantity=100,
    price='225')


class OrderInfo:
    order = client.get_order(
        symbol='BNBBUSD',
        orderId='buraya order id')


app = Flask(__name__)


@app.route("/")
def Definition():
    status = OrderInfo()
    print(json.dumps(status))
