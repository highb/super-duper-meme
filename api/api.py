from flask import Flask, jsonify, request
from flask_restplus import Api, Resource
import random
import redis
import time

app = Flask(__name__)
api = Api(app)
cache = redis.Redis(host='redis', port=6379)

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
  def get_hits(self):
      retries = 5
      while True:
          try:
              return cache.incr('hits')
          except redis.exceptions.ConnectionError as exc:
              if retries == 0:
                  raise exc
              retries -= 1
              time.sleep(0.5)
              
  def get(self):
    return { 'content': random.choice(memes), 'hits': self.get_hits() }

if __name__ == "__main__":
  app.run()
