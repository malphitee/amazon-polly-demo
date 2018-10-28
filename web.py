from flask import Flask
import speech

app = Flask(__name__)

@app.route('/say/<sentence>')
def hello_world(sentence):
    speech.say(sentence)
    return 'finished!'