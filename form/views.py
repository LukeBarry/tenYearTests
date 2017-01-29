from flask import render_template
from . import app
from .database import session, Entry
from flask import request, redirect, url_for

@app.route("/")
def entries():
    entries = session.query(Entry)
    entries = entries.order_by(Entry.datetime.desc())
    entries = entries.all()
    return render_template("base.html", entries=entries)
    