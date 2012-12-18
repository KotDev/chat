from flask import Flask
from core.chat import chat

app = Flask(__name__)

@app.route('/')
def index():
    return chat().room()

@app.route('/say/')
@app.route('/say/<username>')
def say_user(username=None):
    return chat().say(username)
