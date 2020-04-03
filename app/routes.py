from flask import render_template
from app import app
from datetime import datetime
from flask import request


@app.route('/')
@app.route('/index')
def index():

    user = {'username': 'Alpha', 'user_ip': request.remote_addr}
    return render_template('index.html', title='Home', user = user)


@app.route('/test')
def test():
    return "This is a Test. hi there 2"

