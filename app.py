from flask import Flask, render_template
import random
import string
import requests

app = Flask(__name__)

@app.route('/api/get_id')
def find_log():
    while True:
        log_id = ''.join(random.choice(string.lowercase + string.digits) for _ in range(7))
        resp = requests.get('http://logs.omegle.com/%s' % log_id)
        if 'Omegle chat log' in resp.text:
            return log_id
        else:
            pass

@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
