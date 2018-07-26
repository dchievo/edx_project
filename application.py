import os
#
from flask import Flask, session, render_template, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import datetime

app = Flask(__name__)

dburl = os.getenv("DATABASE_URL")
# # Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")
else: 
    print(dburl)

# # Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# # Set up database
engine = create_engine(dburl)
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
    return "this is the parent body of the site"

@app.route("/signup")
def signup():
    users = "users"
    # users = db.execute("SELECT * from books").fetchall()
    # if users is None:
    #     print("In here")
    #     return f"No Query"
    # else:
    #     print(users)
    return render_template("index.html", users=users)            
    #return render_template("index.html", users=users)

@app.route("/registration", methods=["POST"])
def registration():
    if request.form.get("email") is None:
        email = "No email listed"
    else:
        email = request.form.get("email")

    if request.form.get("username") is None:
        username = "No username specified"
    else:
        username = request.form.get("username")

    if request.form.get("password") is None:
        password = "No password specified"
    else:
        password = request.form.get("password")

    return render_template("success.html", email=email, username=username, password=password)

@app.route("/submitted", methods=["GET","POST"])
def submitted():
    newyear = '2018'
    return render_template("submitted.html", newyear = newyear)

@app.route("/login")
def login():
   return render_template("login.html")

@app.route("/logout")
def logout():
   return render_template("logout.html")
# @app.route("/index", methods=["GET","POST"])
# def index():
#     #users = db.execute("SELECT username1, password FROM credentials WHERE id = 1").fetchall()
#     if users is None:
#         users = "DChi"

#     if session.get("notes") is None:
#         session["notes"] = []

#     note = request.form.get("note")
#     session["notes"].append(note)
#     return render_template("index.html", notes = session["notes"], users=users)

@app.route("/searchBooks")
def searchBooks():
   return render_template("searchbooks.html")

@app.route("/searchResults", methods=["GET","POST"])
def searchResults():
    bookTitle = request.form.get("title")
    if bookTitle is None:
        bookTitle = "None submitted"

    # users = db.execute("SELECT * FROM credentials WHERE id = {{ bookTitle }}").fetchall()
    # if users is None:
    #     users = "DChi"

    # if session.get("notes") is None:
    #     session["notes"] = []

    # note = request.form.get("note")
    # session["notes"].append(note)
    return render_template("results.html", bookTitle=bookTitle)   