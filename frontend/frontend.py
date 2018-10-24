from flask import Flask, request
import requests
import json
app = Flask(__name__)

@app.route('/')
def index():
  api_meme_req = requests.get('http://localhost:9001/v1/meme')
  if api_meme_req.status_code == 200:
    api_meme = api_meme_req.json()
    return '<h1>' + api_meme['content'] + '</h1>'
  else:
    return 'API is down'

if __name__ == "__main__":
  app.run()
