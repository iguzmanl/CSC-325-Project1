from flask import Flask, render_template, make_response,request,session
# import json
import time
from datetime import date
from datetime import time
from datetime import datetime

app = Flask(__name__)
app.secret_key = "super secret key"

data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}
@app.route("/")
def home():
    write_to_file("home")
    if session.get('has visited') == True:
        print ('You have visited before')
        # resp = make_response(render_template("/"))
        # resp.set_cookie('somecookiename','iamcookie')
    else:
        print ('You have not visited')
        session['has visited'] = True
    # print(request.__dict__)


    return render_template("home.html")

@app.route("/about")
def about():
    write_to_file("about")
    return render_template("about.html")

@app.route("/kit")
def kit():
    write_to_file("kit")
    return render_template("kit.html")

@app.route("/pup")
def pup():
    write_to_file("pup")
    # our cookie attempt
    resp = make_response(render_template("pup.html"))
    resp.set_cookie('somecookiename','iamcookie')
    return resp
    # return render_template("pup.html")

@app.route("/kit2")
def kit2():
    write_to_file("kit2")

    return render_template("kit2.html")

@app.route("/pup2")
def pup2():
    write_to_file("pu2")

    return render_template("pup2.html")

@app.route("/kit3")
def kit3():
    write_to_file("kit3")

    return render_template("kit3.html")

@app.route("/pup3")
def pup3():
    write_to_file("pup3")

    return render_template("pup3.html")


@app.route('/get-cookie/')
def get_cookie():
    username = request.cookies.get('somecookiename')

def write_to_file(page_title):
    print("you went to :" + page_title)
    user_headers = request.headers
    t = str(datetime.now())
    with open("data_file_new1.csv", "a") as write_file:
        # has visited, page title, headers, time
        write_file.write(str(session.get('has visited')) + ", "  )
        for h in user_headers:
        	print (str(h[0]) + ": " + str(h[1]))
        	write_file.write(str(h[1]).replace(","," ")  + ", " )
        write_file.write(page_title  + ", " )
        write_file.write(t  + ", " )
        write_file.write("\n")


app.run(debug=True, host="127.0.0.1", port=5000)
