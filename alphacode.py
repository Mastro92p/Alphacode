#from flask import Flask
#app = Flask(__name__)

from app import app

#from routes import test


#@app.route("/")
#def hello():
#    return "<h1 style='color:blue'>Hello There!</h1>"

@app.route("/hello2")
def hello2():
    return "<h1 style='color:blue'>Hello2 There! {}</h1>".format(3)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
