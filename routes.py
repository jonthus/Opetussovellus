from app import app
from db import db
from flask import Flask
from flask import redirect, render_template, request, session
import users, courses

@app.route("/course/<int:id>")
def course(id):
    sql = "SELECT name FROM courses WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    name = result.fetchall()
    return render_template("course.html", id=id, name=name)

@app.route("/")
def index():
    list = courses.get_list()
    return render_template("index.html", courses=list)

@app.route("/add", methods=["GET", "POST"])
def add_course():
    users.check_role(2)

    if request.method == "GET":
        return render_template("add.html")

    if request.method == "POST":
        users.check_csrf()
        name = request.form["name"]

    if courses.add_course(name):
        return redirect("/")

@app.route("/remove", methods=["GET", "POST"])
def remove_course():
    users.check_role(2)

    if request.method == "GET":
        return render_template("remove.html")

    if request.method == "POST":
        users.check_csrf()
        course = request.form["name"]
    if courses.remove_course(course):
        return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":
        username = request.form["username"]
        if len(username) < 1 or len(username) > 30:
            return render_template("error.html", message="Käyttäjätunnus on väärän pituinen")
        password1 = request.form["password1"]
        password2 = request.form["password2"]

        if password1 != password2:
            return render_template("error.html", message="Salasanat ovat erit")
        role = request.form["role"]
        if users.register(username, password1, role):
            return redirect("/")
        else:
            return render_template("error.html", message="Rekisteröinti epäonnistui")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

    if users.login(username, password):
        return redirect("/")
    else:
        return render_template("error.html", message="Väärä käyttäjätunnus tai salasana")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")
