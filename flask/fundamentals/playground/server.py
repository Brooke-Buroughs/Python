from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/play')#Displays index1.html 
def play_box():
    return render_template('index1.html')

@app.route('/play/<x>')#displays index2.html with x amount of boxes 
def box_num(x):
    repeat=int(x)#variable set to 'int'(integer)x(input by user)
    return render_template('index2.html', repeat=repeat)#repeat=repeat sets variable and allows it to be used in the index file.

@app.route('/play/<x>/<color>')#displays index3.html with x amount of boxes and a given color
def build_a_box(x,color):#passing in of both variables through parameters
    repeat=(int(x))#same as before
    newColor=color#set newColor = to the color given by the user
    return render_template('index3.html', repeat=repeat, newColor=newColor)

if __name__=="__main__":
    app.run(debug=True)