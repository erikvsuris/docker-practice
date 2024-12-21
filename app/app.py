import datetime
import os
from flask import Flask, render_template

app = Flask(__name__)

template = 'index.html'

@app.route('/')
def index():
    return render_template(template, content='Index, page!', utc_dt=datetime.datetime.utcnow())

@app.route('/hello')
def hello():
    return render_template(template, content='Hello, world!', utc_dt=datetime.datetime.utcnow())

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)