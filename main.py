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

@app.route("/img/kitten1")
def kitten1():
    write_to_file("kitten1")
    return render_template("/img/kitten1.html")

@app.route("/img/puppy1")
def puppy1():
    write_to_file("puppy1")
    # our cookie attempt
    resp = make_response(render_template("/img/puppy1.html"))
    resp.set_cookie('somecookiename','iamcookie')
    return resp
    # return render_template("/img/puppy1.html")

@app.route("/img/kitten2")
def kitten2():
    write_to_file("kitten2")

    return render_template("/img/kitten2.html")

@app.route("/img/puppy2")
def puppy2():
    write_to_file("puppy2")

    return render_template("/img/puppy2.html")

@app.route("/img/kitten3")
def kitten3():
    write_to_file("kitten3")

    return render_template("/img/kitten3.html")

@app.route("/img/puppy3")
def puppy3():
    write_to_file("puppy3")

    return render_template("/img/puppy3.html")


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


app.run(debug=True, host='10.144.203.127', port=int("80"))
