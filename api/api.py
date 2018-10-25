from flask import Flask, jsonify, request
from flask_restplus import Api, Resource
import random

app = Flask(__name__)
api = Api(app)

memes = [
  'Wow. Many meme. Such funny. Very docker.',
  'Old man yells at container.',
  'One does not simply walk into Docker.',
  'Y U NO CONTAINERIZE!?',
  'back in my day we configured our application servers artisanally, by hand, AND WE LIKED IT.',
  'Brace yourselves, containerization is coming.'
]

@api.route('/v1/meme')
class Meme(Resource):
  def get(self):
    return { 'content': random.choice(memes) }

if __name__ == "__main__":
  app.run()
