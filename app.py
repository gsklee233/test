from flask import *
import time
import threading
import json
import hmac
import os


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    print('pull')
    if (request.headers.get('X-GitHub-Event', '') == 'push'):
        os.startfile('./pull.bat')
    return ''


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
