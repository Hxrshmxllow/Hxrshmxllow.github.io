from flask import Flask, render_template, request
from wbscraper import main

# Create an instance of the Flask class that is the WSGI application.
# The first argument is the name of the application module or package,
# typically __name__ when using a single module.
app = Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html")

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    global gpa1
    if(username == "3845811748" and password == "harshit@3126"):
        gpa1 = main("3845811748", "harshit@3126")
        return render_template("gpa.html", finalgpa = round(gpa1, 3))
    else:
        return render_template("index.html")


@app.route('/gpa', methods=['GET', 'POST'])    
def gpa():
    subject = request.form.get("subject")
    level = request.form.get("level")
    grade = request.form.get("grade")
    credits = request.form.get("credits")
    return render_template("gpa.html", finalgpa = gpa1)

    

if __name__ == "__main__":
    app.run('localhost', 8080) 