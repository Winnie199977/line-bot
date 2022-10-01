#架設伺服器
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage,
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
    #使用者傳來的訊息
    s = "收到"
    msg = event.message.text

    if 's' in msg:
        sticker_message = StickerSendMessage(
            package_id='1',
            sticker_id='1'
        )

        line_bot_api.reply_message(
        event.reply_token,
        sticker_message)

        return #function結束

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=s))


if __name__ == "__main__":
    app.run()