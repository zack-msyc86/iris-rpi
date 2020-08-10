from flask import Flask, request
from pylib import ir_play
import json


app = Flask(__name__)

@app.route('/')
def root():
    return 'success'

@app.route('/ir', methods=['POST'])
def ir():
    ir_play.playback(f"{request.json[obj]}:{request.json[command]}")
    return ""

## おまじない
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=50160)
