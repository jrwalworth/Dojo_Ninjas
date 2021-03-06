from flask import render_template, request, redirect
from app.models.ninja import Ninja
from app.models.dojo import Dojo
from app import app


@app.route('/ninjas')
def all_ninjas():
    ninjas = Ninja.get_all()
    return render_template('ninja.html', all_ninjas = ninjas)


#page to add new ninja
@app.route('/ninja/new')
def new_ninja():
    return render_template('ninja.html', ndojos = Dojo.get_all())


#hidden method to add new dojo
@app.route('/ninja/add', methods=["POST"])
def add_ninja():
    data = {
        "dojo_id" : request.form["dojo"],
        "first_name" : request.form["fname"],
        "last_name" : request.form["lname"],
        "age": request.form["age"],
    }
    # id = request.form['dojo']
    Ninja.save(data)
    return redirect(f'/dojo/show/{data["dojo_id"]}')