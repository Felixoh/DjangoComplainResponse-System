from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot #creating chatBot and trying to test with data
bot = ChatBot('Test')
#bot.set_trainer(ListTrainer) #now setup your trainer.Arithmmetic
trainer = ListTrainer(bot)

with open('chats.txt','r') as chat:
    chats = chat.readlines()
    trainer.train(chats)
while True:
    request = input('You: ')
    response = bot.get_response(request)
    print('Bot',response)
