from flask_app import app
from flask import Flask, render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_bcrypt import Bcrypt 
bcrypt=Bcrypt(app)

@app.route("/")
def index():
    return render_template("open_account.html")

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

@app.route("/welcome")
def display_account():
    if 'user_id' not in session:
        return redirect("/")
    else:
        one_user=User.get_one(session)
        return render_template("logout.html", one_user=one_user)

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

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

