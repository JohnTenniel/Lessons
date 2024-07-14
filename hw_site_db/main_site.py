from flask import Flask, render_template, request, flash, g
import sqlite3
import os
from db_cr_py import DataBaseWorking

DEBUG = True
SECRET_KEY = 'a39e6c12f31952feb976c7ba631c2609d84b5da7'

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path, 'cource.db')))


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


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.route("/")
def index():
    db = get_db()
    dbase = DataBaseWorking(db)
    return render_template('index.html', menu=dbase.get_menu(), posts=dbase.get_cource_annonce())


@app.route("/add_post", methods=["POST", "GET"])
def add_cource():
    db = get_db()
    dbase = DataBaseWorking(db)
    if request.method == "POST":
        if len(request.form["name"]) > 4 and len(request.form["cource"]) > 10:
            res = dbase.add_cource(request.form["name"], request.form["cource"])
            if not res:
                flash("Ошибка добавления курса", category='error')
            else:
                flash("Курса добавлена успешно", category='success')
        else:
            flash("Ошибка добавления курса", category='error')
    return render_template('add_cource.html', menu=dbase.get_menu(), title="Добавление курса")


@app.route("/post/<int:id_post>")
def show_post(id_cource):
    db = get_db()
    dbase = DataBaseWorking(db)
    title, post = dbase.get_cource(id_cource)
    return render_template('cource.html', menu=dbase.get_menu(), title=title, cource=cource)


def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


@app.errorhandler(404)
def page_not_found(error):
    db = get_db()
    dbase = DataBaseWorking(db)
    return render_template('page_404.html', title="Страница не найдена", menu=dbase.get_menu())


if __name__ == '__main__':
    app.run()
