from flask import Flask, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "do*not*tell"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

debug = DebugToolbarExtension(app)

########## BEGIN Routes ##########

@app.route('/')
def root():
    """ Lists the pets available for adoption. """
    pets = Pet.query.all()
    return render_template('pet-list.html', pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    """ Shows form to add a pet and handles form submission. """
    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        age = form.age.data
        notes = form.notes.data
        if form.photo_url.data:
            photo_url = form.photo_url.data
            new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        else:
            new_pet = Pet(name=name, species=species, age=age, notes=notes)
        db.session.add(new_pet)
        db.session.commit()

        return redirect("/")
    
    else:
        return render_template('pet-add-form.html', form=form)

@app.route('/<int:pet_id_number>', methods=['GET', 'POST'])
def pet_details_and_edit(pet_id_number):
    """ Shows pet details with edit form. Handles edit form when submitted. """

    pet = Pet.query.get_or_404(pet_id_number)
    form = AddPetForm(obj=pet)

    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        pet.photo_url = form.photo_url.data
        db.session.add(pet)
        db.session.commit()

        return redirect(f"/{pet.id}")

    else:
        return render_template('pet-display.html', pet=pet, form=form)