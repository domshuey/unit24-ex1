from flask import Flask, redirect, render_template, session, request
from flask_debugtoolbar import DebugToolbarExtension
from psycopg2 import connect
from flask_sqlalchemy import SQLAlchemy
from models import Pet, connect_db, db
from forms import AddPet

app = Flask(__name__)
app.config['SECRET_KEY'] = 'abc123' 
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pets'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)
connect_db(app)

@app.route('/')
def show_home():
    pets = Pet.query.all()
    return render_template('home.html', pets=pets)

@app.route('/add', methods=['get', 'post'])
def show_new_pet_form():
    form = AddPet()
    choices = [(True, True),(False, False)]
    form.available.choices = choices

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        notes = form.notes.data
        age = form.age.data
        photo_url = form.photo_url.data
        available = bool(form.available.data)

        newPet = Pet(name=name, species=species, notes=notes, age=age, photo_url=photo_url, available=available)
        db.session.add(newPet)
        db.session.commit()
        return redirect ('/')
    else:
        return render_template('newPetForm.html', form = form)

@app.route('/pets/<int:id>')
def show_pet_details(id):
    pet = Pet.query.get_or_404(id)

    return render_template('details.html', pet=pet)

@app.route('/pets/<int:id>/edit', methods=['get', 'post'])
def show_edit_form(id):
    pet = Pet.query.get_or_404(id)
    form = AddPet(obj=pet)

    choices = [(True, True),(False, False)]
    form.available.choices = choices

    if form.validate_on_submit():
        pet.name = form.name.data
        pet.age = form.age.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = bool(form.available.data)

        db.session.commit()
        return redirect('/')
    else:
        return render_template('editPet.html', form=form, pet=pet)

