from flask import Flask
import random

app = Flask(__name__)

memes = [
  'Wow. Many meme. Such funny. Very docker.',
  'Old man yells at container.',
  'One does not simply walk into Docker.',
  'Y U NO CONTAINERIZE!?',
  'back in my day we configured our application servers artisanally, by hand, AND WE LIKED IT.',
  'Brace yourselves, containerization is coming.'
]

@app.route('/')
def super_duper_meme():
    return '<h1>' + random.choice(memes) + '</h1>'
