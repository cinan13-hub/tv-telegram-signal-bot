from flask import Flask, request
import requests
import os

BOT_TOKEN = os.environ["8370974747:AAEORpi5pPxeTWa7DZppw5R7z3PH5atfXug"]
CHAT_ID = os.environ["155587128"]

app = Flask(__app.py__)

def send(msg):
    url = f"https://api.telegram.org/bot{8370974747:AAEORpi5pPxeTWa7DZppw5R7z3PH5atfXug}/sendMessage"
    requests.post(url, json={
        "155587128": CHAT_ID,
        "text": msg
    })

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    msg = (
        f"📊 FOREX SIGNAL\n"
        f"Pair: {data['pair']}\n"
        f"TF: {data['timeframe']}\n"
        f"Signal: {data['signal']}\n"
        f"Price: {data['price']}"
    )

    send(msg)
    return "ok"

@app.route("/")
def home():
    return "Bot running ✅"

