from flask_app import app
from flask import Flask, render_template, redirect, request, session, flash
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja
@app.route("/")
@app.route("/dojos")
def index():
    dojos=Dojo.get_all()
    print(dojos)
    return render_template("dojo.html", all_dojos=dojos)

@app.route("/create_dojo", methods=["POST"])
def create_dojo():
    data={
        "name":request.form["name"]
    }
    Dojo.save(data)
    return redirect("/")

@app.route("/show/<int:dojo_id>")
def show(dojo_id):
    data={
        "id":dojo_id
    }
    #trying to show info we already have
    one_dojo=Dojo.get_one(data)
    return render_template("display_dojo.html",one_dojo=one_dojo)#new html, get one dojo 

@app.route("/ninjas")
def create_ninja():
    dojos=Dojo.get_all()
    return render_template("ninja.html", all_dojos=dojos)

@app.route("/ninjas/create", methods=["POST"])#request.form = POST
def update_ninjas():
    data={
        "dojo_id":request.form["dojo"], #left matches mysql %()s, right matches html 'name'
        "fname":request.form["fname"],
        "lname":request.form["lname"],
        "age":request.form["age"]
    }
    Ninja.save(data)
    return redirect(f"/show/{request.form['dojo']}")

@app.route("/display")
def display():
    return render_template("display_dojo.html")