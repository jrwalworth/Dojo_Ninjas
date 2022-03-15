from flask import render_template, request, redirect
from app.models.ninja import Ninja
from app import app

#Home route
# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route('/')
def all_ninjas():
    ninjas = Ninja.get_all()
    print(ninjas)
    return render_template('dojo_show.html', all_ninjas=ninjas)


#page to add new ninja
@app.route('/ninja/new')
def new_ninja():
    data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "age": request.form["age"],
    }
    return render_template('ninja.html')

#hidden method to add new dojo
@app.route('/ninja/add', methods=["POST"])
def add_ninja(id):
    data = {
        "id": id
    }
    
    Ninja.save(data)
    return redirect('/')