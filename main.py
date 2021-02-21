from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("Romie")

conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

#trainer object

trainer = ListTrainer(chatbot)

#now training bot with the help of trainer

trainer.train(conversation)

#checking bot response
response = chatbot.get_response("Good morning!")
print(response)

print("Talk to bot")
while True:
    query=input("User :")
    if query=='exit':
        break
    answer = Romie.getresponse(query)
    print("Romie :", answer)




