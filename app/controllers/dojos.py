from flask import render_template, request, redirect
from app.models.dojo import Dojo
from app import app

#Home route
@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def all_dojos():
    dojos = Dojo.get_all()
    #print(dojos)
    return render_template('index.html', all_dojos=dojos)

#page to view single dojo and all ninjas
@app.route('/dojo/show/<int:id>')
def dojo(id):
    data = {
        "id": id,
    }
    dojo = Dojo.get_all_ninjas_from_dojo(data)
    return render_template('dojo_show.html', one_dojo=dojo)

#hidden method to add new dojo
@app.route('/dojo/new', methods=["POST"])
def new_dojo():
    data = {
        "name" : request.form["name"]
    }
    Dojo.save(data)
    return redirect('/')