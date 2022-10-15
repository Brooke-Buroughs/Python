from flask_app import app
from flask import render_template,redirect,request,session,flash
from burger import Burger
# burgers.py...
from flask_app.models.burger import Burger
# gets all the burgers and returns them in a list of burger objects .
@app.route('/burgers')
def burgers():
	return render_template('results.html',burgers=Burger.get_all())
        


#have the controller call the model class methods
#update the burger import statement in the controller

# burgers.py...
from flask_app.models.burger import Burger
# gets all the burgers and returns them in a list of burger objects .
@app.route('/create/burger',methods=['POST'])
def create_burger():
    data = {
            "name" : request.form['name'],
            "bun" : request.form['bun'],
            "meat" : request.form['meat'],
            "calories" : request.form['calories']
    }
    Burger.save(data)
    return redirect('/burgers')
        


