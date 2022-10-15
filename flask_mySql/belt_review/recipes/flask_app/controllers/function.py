from flask_app import app
from flask import Flask, render_template, redirect, request, session, flash
from flask_app.models.user import User 
from flask_app.models.recipe import Recipe
from flask_bcrypt import Bcrypt
bcrypt=Bcrypt(app)

@app.route("/")
def index():
    return render_template("recipe_share.html")

@app.route("/create_account", methods=["POST"])
def create_account():
    if not User.validate_user(request.form):
        return redirect("/")
    pw_hash=bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data={
        "fname":request.form["fname"],
        "lname":request.form["lname"],
        "email":request.form["email"],
        "password":pw_hash
    }
    one_user=User.save(data)
    session['user_id']=one_user
    return redirect("/welcome")

@app.route('/login', methods=['POST'])
def login():
    data = { "email" : request.form["email"] }
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash("Invalid Email/Password", 'login')
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Email/Password", 'login')
        return redirect('/')
    session['user_id'] = user_in_db.id
    return redirect("/welcome")

@app.route('/welcome')
def display_account():
    one_user=User.get_one(session)
    all_recipes=Recipe.get_all()
    return render_template("user_recipes.html", one_user=one_user, all_recipes=all_recipes)

@app.route('/create')
def create():
    return render_template("add_a_recipe.html")

@app.route("/logout")
def logout():
    return redirect("/")


@app.route("/submit", methods=['POST'])
def submit_recipe():
    if not User.validate_input(request.form):
        return redirect("/create")
    data={
        "name":request.form['name'],
        "description":request.form['description'],
        "instruction":request.form['instruction'],
        "date":request.form['date'],
        "time":request.form['time'],
        "user_id":session['user_id']
    }
    new_recipe=Recipe.save(data)
    session['new_recipe']=new_recipe
    return redirect('/welcome')

@app.route("/edit/<int:recipe_id>")
def edit(recipe_id):
    data={
        "id":recipe_id
    }
    user_data={
        "user_id":session['user_id']
    }
    print('user_data')
    a_user=User.get_one(user_data)
    one_recipe=Recipe.get_recipe_by_user(data)
    return render_template("edit_recipe.html", one_recipe=one_recipe, a_user=a_user)

@app.route("/update", methods=['POST'])
def update():
    if not User.validate_input(request.form):
        return redirect(f"/edit/{request.form['id']}")
    data={
        "name":request.form['name'],
        "description":request.form['description'],
        "instruction":request.form['instruction'],
        "date":request.form['date'],
        "time":request.form['time'],
        "id":request.form['id']
    }
    Recipe.update_info(data)
    return redirect('/welcome')

@app.route("/delete/<int:recipe_id>")
def delete(recipe_id):
    data={
        "id":recipe_id
    }
    Recipe.delete_info(data)
    return redirect("/welcome")

@app.route("/view/<int:recipe_id>")
def display_recipe(recipe_id):
    data={
        "id":recipe_id
    }
    user_data={
        "user_id":session['user_id']
    }
    a_user=User.get_one(user_data)
    one_recipe=Recipe.get_recipe_by_user(data)
    return render_template("recipe_selected.html", one_recipe=one_recipe, a_user=a_user)