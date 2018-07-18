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

@app.route("/index")
def index():
    users = db.execute("SELECT * from books").fetchall()
    if users is None:
        print("In here")
        return f"No Query"
    else:
        print(users)
        return render_template("index.html", users=users)            
    #return render_template("index.html", users=users)

#@app.route("/more")
#def more():
#    headline = "bye there"
#    return render_template("more.html", headline=headline)

#@app.route("/layout")
#def layout():
#    now = datetime.datetime.now()
#    new_year = now.month == 1 and now.day == 1
#    return render_template("layout.html", newyear = new_year)

#@app.route("/example")
#def example():
#    names = ["alice", "david", "charlie"]
#    return render_template("index.html", names=names)

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

# @app.route("/")
# def main():
#    return f"hello world"
