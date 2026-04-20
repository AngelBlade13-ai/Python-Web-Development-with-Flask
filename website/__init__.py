from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "Pineapples are the worst."

    return app