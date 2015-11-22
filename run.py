import os
from flask import request, Flask, render_template
import json

ASSETS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), './app')

app = Flask(__name__, template_folder=ASSETS_DIR, static_folder=ASSETS_DIR)

@app.route('/uploadData/', methods=['GET', 'POST'])
def upload_data():
    if request.method == 'POST':
        print(json.loads(request.data.decode("utf8")))
        return "upload ok"


@app.route('/clearRfid/', methods=['GET', 'POST'])
def clear_rfid():
    if request.method == 'GET':
        return "clear ok"


@app.route('/')
def root():
    return render_template('index.html')

def run():
    app.run(debug = True)

run()

