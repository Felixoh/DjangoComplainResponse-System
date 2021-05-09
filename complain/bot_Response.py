"""
    All Automatic Complain Responses generated from this module
    The training data used at this point is minimal with few pre-trained responses
    The bot makes use of the inbuilt corpus.english word to train the Bot
    The bot is built based on few natural language processing Responses

"""

from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('ChatResponder')
trainer = ListTrainer(bot)
trainer.train(
["Thanks for your concern,we are working on it",
",We will be eager to Serve You,the county is on the problem to resolve as soon as possible",
"Just a little while your response will be generated ,thanks for your concern",
"Complain has been received we are on it",
"thanks for you information ,will be worked on sooner than you think",
"Will be resolved soon ",
"Humbled,your responses will be worked on sooner"
"There are several programmes underway please wait a little bit soon we are working on something",
])


def response_Generator(text):
    response =  bot.get_response(text)
    output = str(response)
    return output