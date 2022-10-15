from flask_app import app
from flask import Flask, render_template, redirect, request, session, flash 
from flask_app.models.thought import Thought
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
    data={
        'id':session['user_id']
    }
    one_user=User.get_one(data)
    all_thoughts=Thought.get_all()
    return render_template("welcome.html", one_user=one_user, all_thoughts=all_thoughts) 

@app.route("/logout")
def logout():
    return redirect("/")

@app.route("/submit", methods=['POST'])
def submit_recipe():
    if not Thought.validate_input(request.form):
        return redirect("/welcome")
    data={
        "content":request.form['content'],
        "user_id":session['user_id']
    }
    new_thought=Thought.save(data)
    session['new_thought']=new_thought
    return redirect('/welcome')

@app.route("/delete/<int:thought_id>")
def delete(thought_id):
    data={
        "id":thought_id
    }
    Thought.delete_info(data)
    return redirect("/welcome")

@app.route("/add_one")
def add_one():
    if 'email' not in session:
        return redirect("/")
    else: 
    if request.form['likes']=='None':
        likes=0
    else:
    # likes=0
    likes=int(Thought['likes']) +1
    data={
        "id":request.form['id'],
        "user_id":request.form['user_id'],
        "likes":request.form['likes']
    }
    Thought.update(data)
    return redirect("/welcome", likes=likes)

@app.route("/unlike", methods=["POST"])
def unlike():
    if 'id' not in session:
        return redirect("/")
    else:
        if int(request.form['likes'])-1<0:
            likes=0
        else:
            likes=int(request.form['likes'])-1
        
        data={
            "id":request.form['id'],
            "user_id":request.form['user_id'],
            "likes":request.form['likes']
        }
        Thought.update(data)
        return redirect("welcome")

#registration w/ validation- done
#login w/ validation- done 
#post a thought , thought validations
#delete function
#display all users thoughts when viewing an account 
#likes - add one and 
# subtract one
