from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

app = Flask(__name__)
 
bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ListTrainer(bot)
trainer.train([
	"How are you?",
	"I am good.",
	"That is good to hear.",
	"Thank you",
	"You are welcome.",
])

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(bot.get_response(userText))
