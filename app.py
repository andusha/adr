import sqlite3
import os
from flask import (
    Flask,
    render_template,
    g,
)

from repair.FDataBase import FDataBase
from repair.forms import StatementForm
from repair.email import send_email
# конфигурация
DATABASE = "/tmp/v5.db"
DEBUG = True
SECRET_KEY = "rthtyhv475?>gfhf89dxhgfnjh,6c5h6h67h#$"
MAX_CONTENT_LENGTH = 1024 * 1024

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path, "v5.db")))


def connect_db():
    conn = sqlite3.connect(app.config["DATABASE"])
    conn.row_factory = sqlite3.Row
    return conn


def create_db():
    """Вспомогательная функция для создания таблиц БД"""
    db = connect_db()
    with app.open_resource("sq_db.sql", mode="r") as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


def get_db():
    """Соединение с БД, если оно еще не установлено"""
    if not hasattr(g, "link_db"):
        g.link_db = connect_db()
    return g.link_db


dbase = None


@app.before_request
def before_request():
    """Установление соединения с БД перед выполнением запроса"""
    global dbase
    db = get_db()
    dbase = FDataBase(db)


@app.teardown_appcontext
def close_db(error):
    """Закрываем соединение с БД, если оно было установлено"""
    if hasattr(g, "link_db"):
        g.link_db.close()


@app.route("/", methods=["POST", "GET"])
def main():
    return render_template("index.html")


@app.route("/about", methods=["POST", "GET"])
def about():
    return render_template("about.html")


@app.route("/contact", methods=["POST", "GET"])
def contact():
    form = StatementForm()
    if form.validate_on_submit():
        send_email(form.name.data, form.phone.data, form.comm.data)
        dbase.addStatement(form.name.data, form.phone.data, form.comm.data)
    return render_template("contact.html", form=form)


@app.route("/project", methods=["POST", "GET"])
def project():
    return render_template("project.html")


@app.route("/single", methods=["POST", "GET"])
def single():
    return render_template("single.html")


if __name__ == "__main__":
    app.run(debug=True)
