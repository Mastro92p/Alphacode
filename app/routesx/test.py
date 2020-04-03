import time

from alphacode import app

@app.route('/hello')
def test():
    return 'Hello, World'

def getNumber():
    return 2
