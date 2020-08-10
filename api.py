from flask import Flask

from pylib import ir_play


app = Flask(__name__)

@app.route('/ir/<obj>/<command>')
def ir_controll(obj,command):
    ir_play.playback(f'{obj}:{command}')

## おまじない
if __name__ == "__main__":
    app.run(debug=True)
