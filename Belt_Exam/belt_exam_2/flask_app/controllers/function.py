from flask_app import app
from flask import Flask, render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_app.models.show import Show
from flask_bcrypt import Bcrypt
bcrypt=Bcrypt(app)

@app.route("/")
def index():
    return render_template("login_and_register.html")

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
    if 'user_id' not in session:
        return redirect("/")
    else:
        one_user=User.get_one(session)
        all_shows=Show.get_all()
        return render_template("user_shows.html", one_user=one_user, all_shows=all_shows)

@app.route('/create')
def create():
    if 'user_id' not in session:
        return redirect("/")
    else:
        return render_template("add_a_show.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


@app.route("/submit", methods=['POST'])
def submit_show():
    if 'user_id' not in session:
        return redirect("/")
    else:
        if not User.validate_input(request.form):
            return redirect("/create")
        data={
            "name":request.form['name'],
            "description":request.form['description'],
            "network":request.form['network'],
            "date":request.form['date'],
            "user_id":session['user_id']
        }
        new_show=Show.save(data)
        session['new_show']=new_show
        return redirect('/welcome')

@app.route("/edit/<int:show_id>")
def edit(show_id):
    if 'user_id' not in session:
        return redirect("/")
    else:
        data={
            "id":show_id
        }
        user_data={
            "user_id":session['user_id']
        }
        print('user_data')
        a_user=User.get_one(user_data)
        one_show=Show.get_show_by_user(data)
        if session['user_id']==one_show.user_id:
            return render_template("edit_show.html", one_show=one_show, a_user=a_user)
        else:
            return redirect("/welcome")

@app.route("/update", methods=['POST'])
def update():
    if 'user_id' not in session:
        return redirect("/")
    else:
        if not User.validate_input(request.form):
            return redirect(f"/edit/{request.form['id']}")
        data={
            "name":request.form['name'],
            "description":request.form['description'],
            "network":request.form['network'],
            "date":request.form['date'],
            "id":request.form['id']
        }
        Show.update_info(data)
        return redirect('/welcome')

@app.route("/delete/<int:show_id>")
def delete(show_id):
    data={
        "id":show_id
    }
    one_show=Show.get_show_by_user(data)
    if 'user_id' not in session:
        return redirect("/")
    else:
        if session['user_id']==one_show.user_id:
            Show.delete_info(data)
            return redirect("/welcome")
        else:
            return redirect("/welcome")

@app.route("/view/<int:show_id>")
def display_show(show_id):
    if 'user_id' not in session:
        return redirect("/")
    else:
        data={
            "id":show_id
        }
        user_data={
            "user_id":session['user_id']
        }
        a_user=User.get_one(user_data)
        one_show=Show.get_show_by_user(data)
        return render_template("show_selected.html", one_show=one_show, a_user=a_user)

        