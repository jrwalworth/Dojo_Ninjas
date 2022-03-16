from flask import render_template, request, redirect
from app.models.ninja import Ninja
from app.models.dojo import Dojo
from app import app

#Home route
# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route('/ninjas')
def all_ninjas():
    ninjas = Ninja.get_all()
    print(ninjas)
    return render_template('dojo_show.html', all_ninjas=ninjas)


#page to add new ninja
@app.route('/ninja/new')
def new_ninja():
    # data = {
    #     "first_name" : request.form["first_name"],
    #     "last_name" : request.form["last_name"],
    #     "age": request.form["age"],
    # }
    dojos = Dojo.get_all()
    return render_template('ninja.html', ndojos = dojos)

#hidden method to add new dojo
@app.route('/ninja/add', methods=["POST"])
def add_ninja():
    data = {
        "id": id
    }
    Ninja.save(data)
    return redirect('/')