from os import environ, path
from flask import Flask, request, jsonify
import requests

BOT_TOKEN = environ['TELEGRAM_BOT_TOKEN']
WEBHOOK_URL = environ['TELEGRAM_WEBHOOK_URL']
SEND_MESSAGE_URL = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?POST'


def set_webhook():
    set_webhook_url = f'https://api.telegram.org/bot{BOT_TOKEN}/setWebHook?url={WEBHOOK_URL}'
    webhook_response = requests.get(set_webhook_url)
    print(webhook_response.text)
    return webhook_response

def post_status(request_json):
    post_json = {'chat_id': CHAT_ID, 'text': request_json}
    resp = requests.post(SEND_MESSAGE_URL,  json=post_json)
    print(resp.text)
    return jsonify(resp.json()), resp.status_code

  
app = Flask(__name__)

@app.route('/', methods=['POST'])
def telegram():
  return post_status(request.get_json())
    
