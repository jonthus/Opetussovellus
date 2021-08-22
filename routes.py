from app import app
from db import db
from flask import Flask, flash, redirect, render_template, request, session
import users, courses, exercises, signups, answers

@app.route("/profile", methods=["GET", "POST"])
def profile():
    user_id = users.get_user()
    list = signups.get_signups(user_id)
    correct = answers.count_correct(user_id)
    incorrect = answers.count_incorrect(user_id)
    return render_template("profile.html", signups=list, correct=correct, incorrect=incorrect)

@app.route("/result", methods=["POST"])
def check_answer():
    exercise_id = request.form["exercise_id"]
    answer = request.form["answer"]
    user_id = users.get_user()

    try:
        correct = answers.check_answer(exercise_id, user_id, answer)
        return render_template("result.html", correct=correct, exercise_id=exercise_id)
    except:
        return render_template("error.html", message="Error")

def check_signup():
    user_id = users.get_user()
    check = signups.check_signup(user_id, course_id)
    if check == None:
        return render_template("error.html", message="Error checking signup.", check=check)
    else:
        return render_template("course.html", course_id=course_id)

@app.route("/signup", methods=["POST"])
def signup():
    user_id = users.get_user()
    course_id = request.form["course_id"]
    try:
        if signups.sign_up(user_id, course_id):
            return redirect("/")
    except:
        return render_template("error.html", message="Error trying to signup.")

@app.route("/exercise/<int:exercise_id>", methods=["GET", "POST"])
def exercise(exercise_id):
    list = exercises.get_exercise(exercise_id)
    return render_template("exercise.html", exercises=list, exercise_id=exercise_id)

@app.route("/add/<int:course_id>", methods=["POST"])
def add_exercise(course_id):
    users.check_role(2)

    name = request.form["name"]
    content = request.form["content"]
    correct = request.form["correct"]
    if len(content) < 1 or len(content) > 50:
        return redirect("/")
    if exercises.add_exercise(name, content, correct, course_id):
        return redirect("/course/" + str(course_id))

@app.route("/remove/<int:course_id>", methods=["POST"])
def remove_exercise(course_id):
    users.check_role(2)
    
    exercise_name = request.form["exercise_name"]
    exercises.remove_exercise(course_id, exercise_name)
    return redirect("/course/" + str(course_id))

@app.route("/course/<int:course_id>")
def course(course_id):
    user_id = users.get_user()
    list = exercises.get_exercises(course_id)
    check = signups.check_signup(user_id, course_id)
    return render_template("course.html", course_id=course_id, exercises=list, check=check)

@app.route("/")
def index():
    list = courses.get_list()
    return render_template("index.html", courses=list)

@app.route("/add", methods=["GET", "POST"])
def add_course():
    users.check_role(2)

    if request.method == "GET":
        list = courses.get_list()
        return render_template("add.html", courses=list)

    if request.method == "POST":
        users.check_csrf()
        name = request.form["name"]
        if len(name) < 1 or len(name) > 30:
            return render_template("error.html", message="Kurssin nimi ei vastaa vaatimuksia.")
    try:
        if courses.add_course(name):
            return redirect("/add")
    except:
        return render_template("error.html", message="Kurssi on jo olemassa.")

@app.route("/remove", methods=["GET", "POST"])
def remove_course():
    users.check_role(2)

    if request.method == "GET":
        list = courses.get_list()
        return render_template("remove.html", courses=list)

    if request.method == "POST":
        users.check_csrf()
        course = request.form["name"]
    if courses.remove_course(course):
        return redirect("/remove")

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
