from flask_sqlalchemy import SQLAlchemy
import logging as lg
import enum

from .views import app

# Create database connection object
db = SQLAlchemy(app)


class Typo(enum.Enum):
    Recruter = 0
    Developper = 1
    other = 2


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200), nullable=False)
    typo = db.Column(db.Enum(Typo), nullable=False)
    content = db.Column(db.String(600), nullable=False)

    def __init__(self, email, typo, content):
        self.email = email
        self.typo = typo
        self.content = content


def init_db():
    db.drop_all()
    db.create_all()
    db.session.add(Contact("stan.bruyere01@gmail.com", 1, "Salut! tu va bien ?"))
    db.session.commit()
    lg.warning('Database initialized!')
