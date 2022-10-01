#架設伺服器
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('lSo0H3LWajaXRbK7tQIQZ0cdtcBFkHhUBqGdLq1l8XWShOgA9EXIGeGp7GD1017RUPJDmcajMTpdIZz+kE9YnUbJ2pH/oyPkn66SJMu4agpmDupYjRd8KEGjCwq1acklcrMo3slsy8Qe58dQw28QLAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('3626cc2c5c80f5c7c811f3b0dcd00118')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()