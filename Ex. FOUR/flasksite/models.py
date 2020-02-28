from flasksite import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return f"User('{self.name}', '{self.email}')"

class Forecast(db.Model):
    __tablename__ = 'forecast'
    forecast_id = db.Column(db.Integer, primary_key=True)
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    datetime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    forecast = db.Column(db.String(250), nullable=False)
    comment = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return f"Forecast('{self.forecast}', '{self.comment}')"