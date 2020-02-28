from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DevConfig

db = SQLAlchemy()


def create_app(config_class=DevConfig):

    app = Flask(__name__)

    app.config.from_object(config_class)

    db.init_app(app)

    from langbridge.models import Teacher, User, LanguageUser, Lesson, Language, LessonReview, Wallet
    with app.app_context():
        db.create_all()

    from langbridge.main.routes import bp_main
    app.register_blueprint(bp_main)

    return app
