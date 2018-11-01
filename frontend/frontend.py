from flask import Flask, request
import requests
import json
app = Flask(__name__)

@app.route('/')
def index():
  api_url = 'http://localhost:9001/v1/meme'
  try: 
    api_meme_req = requests.get(api_url, timeout=1)
    if api_meme_req.status_code == 200:
      api_meme = api_meme_req.json()
      return '<h1>' + api_meme['content'] + '</h1>'
    else:
      return 'API at ' + api_url + ' returned error code: ' + api_meme_req.status_code
  except requests.exceptions.ConnectionError:
    return 'API at ' + api_url + ' failed to connect.'

if __name__ == "__main__":
  app.run()
