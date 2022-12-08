from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

default_img_url = 'static/default_dog.png'

class Pet(db.Model):
    """ Pet. """

    __tablename__ = "pets"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, default=default_img_url)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=1)

    def __repr__(self):
        return f'<Pet {self.id} {self.name} the {self.species}>'


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
