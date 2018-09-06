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

line_bot_api = LineBotApi('F8mn563Of+sJa2eVPm5ernIWzF1r+0ccoQ+iuoPbd5DTLz7s1LAKh8/Qiy1mteZ7BLIlJEPO//sX6s7A0dxzAOquUOYZoUtsL8ODyrmgRiQh+Bc8aGOmVODyVCs92FKynlBkoEG2RnSBk9gJUScL8QdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('30ff17e0f40dc914e828f249aa6a9c66')


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
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg=event.message.text
    r='我看不懂你說什麼'
    if msg in ['hi','Hi']:
        r='嗨'
    elif msg=='吃飯了ㄇ':
        r='還沒'
    elif msg=='你是誰':
        r='機器人就是我'
    elif '訂位'in msg:
        r='想訂位是吧'
    line_bot_api.reply_message(
        event.reply_token,
        StickerSendMessage(
    package_id='1',
    sticker_id='1'
))


if __name__ == "__main__":
    app.run()