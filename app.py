from flask import Flask, render_template
app = Flask(__name__)

@app.route("/DK/home")
def hello():

    return render_template('home.html')

@app.route("/DK")



def harry():
    return "Hello!"
app.run(debug=True)
