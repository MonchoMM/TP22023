from flask import Flask

app = Flask(__name__)

@app.get("/")
def home():
    return "<p>Te damos la bienvenida a MacoWins</p>"