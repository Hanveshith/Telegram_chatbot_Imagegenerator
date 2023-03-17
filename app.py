import os
import openai
import telegram.ext


openai.api_key = os.getenv("OPENAI_API_KEY")


updater = telegram.ext.Updater("TELEGRAMBOT_TOKEN", use_context=True)
dispatcher = updater.dispatcher

def start(update,context):
    update.message.reply_text("Hello")

message_text = None
def message(update,context):
    global message_text
    message_text = update.message.text
    


def getimage(update,context):
    print(message_text)
    if(message_text == "/getimage"):
        update.message.reply_text("Enter the text")
    else:
        res = openai.Image.create(
        prompt = message_text,
        n = 1,
        size = "1024x1024")
        photo_url = res['data'][0]['url']
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=photo_url)

def chat(update,context):    
    print(message_text)
    if(message_text == "/chat"):
        update.message.reply_text("Enter the text")
    else:
        completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": message_text}
        ])
        update.message.reply_text(completion.choices[0].message['content'])

print(message_text)
dispatcher.add_handler(telegram.ext.CommandHandler('start',start))
dispatcher.add_handler(telegram.ext.CommandHandler('getimage',getimage))
dispatcher.add_handler(telegram.ext.CommandHandler('chat',chat))
dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, message))
# dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, chat))

updater.start_polling()
updater.idle()
