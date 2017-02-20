from flask import render_template
from . import app
from .database import session, Entry
from flask import request, redirect, url_for

@app.route("/chief45scores")
def entries():
    entries = session.query(Entry)
    entries = entries.all()
    return render_template("entries.html", entries=entries)

@app.route("/", methods=["GET"])
def add_entry_get():
    return render_template("base.html")

@app.route("/", methods=["POST"])
def add_entry_post():
    entry = Entry(
        student_id=request.form["student_id"],
        student_name=request.form["student_name"],
        parent_name=request.form["parent_name"],
        site_location=request.form["site_location"],
        phone_number=request.form["phone_number"],
        alt_number=request.form["alt_number"],
        notes=request.form["notes"],
        # datetime=request.form["datetime"]      
    )
    session.add(entry)
    session.commit()
    return redirect("/")


@app.route("/chief45scores", methods=["GET"])
def view():
    return render_template("entries.html")
    

@app.route("/chief45scores", methods=["POST"])
def view_post():
    entry = Entry(
        student_id=request.form["student_id"],
        student_name=request.form["student_name"],
        parent_name=request.form["parent_name"],
        site_location=request.form["site_location"],
        phone_number=request.form["phone_number"],
        alt_number=request.form["alt_number"],
        notes=request.form["notes"],
        # datetime=request.form["datetime"]      
    )
    session.add(entry)
    session.commit()
    return redirect("/chief45scores")  

  
  
  
