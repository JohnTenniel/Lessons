from flask import Flask, render_template, request, flash
import sqlite3
import os

DEBUG = True
SECRET_KEY = 'a39e6c12f31952feb976c7ba631c2609d84b5da7'

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flsk.db')))


def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con


def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', "r") as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()

@app.route("/")
def index():
    db = get_db()
    return render_template('index.html')

