from os import path

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "pineapples are gross"
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"sqlite:///{path.join(path.dirname(__file__), DB_NAME)}"
    )

    db.init_app(app)

    from .auth import auth
    from .models import Note, User
    from .views import views

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.get(User, int(user_id))

    return app


def create_database(app):
    database_path = path.join(path.dirname(__file__), DB_NAME)
    if not path.exists(database_path):
        with app.app_context():
            db.create_all()
        print("Created Database!")
