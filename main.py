from flask import Flask, render_template, make_response,request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/kit")
def kit():
    return render_template("kit.html")

@app.route("/pup")
def pup():
    # our cookie attempt
    resp = make_response(render_template("pup.html"))
    resp.set_cookie('somecookiename','iamcookie')
    return resp
    # return render_template("pup.html")

@app.route("/kit2")
def kit2():
    return render_template("kit2.html")

@app.route("/pup2")
def pup2():
    return render_template("pup2.html")

@app.route("/kit3")
def kit3():
    return render_template("kit3.html")

@app.route("/pup3")
def pup3():
    return render_template("pup3.html")
@app.route('/get-cookie/')
def get_cookie():
    username = request.cookies.get('somecookiename')

if __name__ == "__main__":
    app.run(debug=True)
