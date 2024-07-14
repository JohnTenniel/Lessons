from flask import Flask, render_template, request, flash, g
import sqlite3
import os
from db_work import DataBaseWork

DEBUG = True
SECRET_KEY = 'a39e6c12f31952feb976c7ba631c2609d84b5da7'

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path, 'course.db')))


def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con


def create_db():
    db = connect_db()
    with app.open_resource('create_db.sql', "r") as f:
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
    dbase = DataBaseWork(db)
    return render_template('index.html', menu=dbase.get_menu(), title="Pricing", courses=dbase.get_course_annonce())


@app.route("/add_course", methods=["POST", "GET"])
def add_course():
    db = get_db()
    dbase = DataBaseWork(db)
    if request.method == "POST":
        if len(request.form["name"]) > 4 and len(request.form["price"]) > 3 and len(request.form["course"]) > 10:
            res = dbase.add_course(request.form["name"], request.form["price"], request.form["course"])
            if not res:
                flash("Ошибка добавления курса", category='error')
            else:
                flash("Курс добавлен успешно", category='success')
        else:
            flash("Ошибка добавления курса", category='error')
    return render_template('add_course.html', menu=dbase.get_menu(), title="Добавление курса")


@app.route("/course/<int:id_course>")
def show_course(id_course):
    db = get_db()
    dbase = DataBaseWork(db)
    title, price, course = dbase.get_course(id_course)
    return render_template('course.html', menu=dbase.get_menu(), title=title, price=price, course=course)


@app.route("/info")
def info():
    db = get_db()
    dbase = DataBaseWork(db)
    return render_template('info.html', menu=dbase.get_menu(), title="About Us")



@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


@app.errorhandler(404)
def page_not_found(error):
    db = get_db()
    dbase = DataBaseWork(db)
    return render_template('page_404.html', title="Страница не найдена", menu=dbase.get_menu())


if __name__ == '__main__':
    app.run()
