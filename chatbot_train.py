from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot = ChatBot('Bot')
bot.set_trainer(ListTrainer)
langs = ['hindi','english']

#(For training the different languages)

# for lang in langs:
#     for files in os.listdir('/home/rohit/Music/chatterbot-corpus-master/chatterbot_corpus/data/'+lang):
#         data = open("/home/rohit/Music/chatterbot-corpus-master/chatterbot_corpus/data/"+lang+"/" + files,
#                     'r').readlines()
#         bot.train(data)

while True:
    message = input('You:')
    if message.strip() != 'Bye':
        reply = bot.get_response(message)
        print('ChatBot :', reply)
    else:
        print("exiting")
        break
#first , the response time.!