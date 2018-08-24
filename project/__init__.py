from flask import Flask
from project import model
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/shape")
def shape():
    return str(model.get_data())
