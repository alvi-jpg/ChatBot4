from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import wikipedia

# create chatbot instance
chatbot = ChatBot('MyBot')

# train the chatbot using ChatterBotCorpusTrainer
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

# define a function to get wikipedia summaries
def get_summary(topic):
    try:
        summary = wikipedia.summary(topic, sentences=1)
    except wikipedia.exceptions.DisambiguationError as e:
        summary = wikipedia.summary(e.options[0], sentences=1)
    return summary

# define a function to get chatbot response
def get_response(query):
    response = chatbot.get_response(query)
    if response.confidence < 0.5:
        try:
            summary = get_summary(query)
            response = summary
        except wikipedia.exceptions.PageError:
            response = "I'm sorry, I don't know the answer to that."
    return response

# loop to get user input and chatbot response
while True:
    query = input("You: ")
    response = get_response(query)
    print("Bot:", response)
