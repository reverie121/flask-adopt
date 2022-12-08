"""Seed file to make sample data for pets db."""

from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Pet.query.delete()

# Create new pets
p1 = Pet(name='Brina', species='Bigfoot', age=26, notes='Likes going on new adventures.', available=1, photo_url='https://static.wikia.nocookie.net/squishmallowsquad/images/5/56/Brina.jpg')
p2 = Pet(name='Regina', species='Dog', age=7, notes='Dresses as an avocado.', available=1, photo_url='https://static.wikia.nocookie.net/squishmallowsquad/images/a/a4/Regina_Official.png')
p3 = Pet(name='Avery', species='Duck', age=30, notes='He is a wingman for a rugby team but wants to be the coach.', available=1, photo_url='https://static.wikia.nocookie.net/squishmallowsquad/images/1/1a/Avery.jpg')
p4 = Pet(name='Nic', species='Squirrel', age=101, notes='Loves music.', available=1, photo_url='https://static.wikia.nocookie.net/squishmallowsquad/images/3/32/Nic.jpg')
p5 = Pet(name='Prince', species='Dog', age=2, notes='Likes doing flips and tricks on the playground.', available=1, photo_url='https://static.wikia.nocookie.net/squishmallowsquad/images/e/ea/Prince.jpg')

# Add pets to session and commit
db.session.add(p1)
db.session.add(p2)
db.session.add(p3)
db.session.add(p4)
db.session.add(p5)

db.session.commit()