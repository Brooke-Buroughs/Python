from flask import Flask, render_template, session, redirect, request
app=Flask(__name__)
app.secret_key='keep it secret, keep it safe'

@app.route('/')#displays input.html
def display_form():
    return render_template("input.html")

@app.route('/process', methods=['POST'])#method to post the info, carries it over
def submit_form():
    session['name']=request.form['name']
    session['location']=request.form['location']
    session['language']=request.form['language']
    session['comment']=request.form['comment']#session is a dictionary we can use and set equal to form info
    return redirect('/result')


@app.route('/result')#displays output.html
def display_submit():
    return render_template("output.html")


if __name__=="__main__":
    app.run(debug=True)