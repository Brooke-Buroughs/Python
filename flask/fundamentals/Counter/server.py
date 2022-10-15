from flask import Flask, session, render_template, redirect
app=Flask(__name__)
app.secret_key='3pinkittens'

@app.route('/')
def index():
    if 'count' not in session:
        session['count']=0
    session['count']+=1
    return render_template("index.html", count=session['count'])

@app.route('/destroy_session')
def reset():
    session['count']=0
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)
