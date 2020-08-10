from flask import Flask

from pylib import ir_play


app = Flask(__name__)

@app.route('/ir/<obj>/<command>')
def ir_controll(obj,command):
    ir_play.playback([f"{obj}:{command}"])
    return None

## おまじない
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=3080)
