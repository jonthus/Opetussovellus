from app import app
from db import db
from flask import Flask, flash, redirect, render_template, request, session
import users, courses, exercises, signups, answers

@app.route("/profile", methods=["GET", "POST"])
def profile():
    user_id = users.get_user()
    signups_list = signups.get_signups(user_id)
    correct = answers.count_correct(user_id)
    incorrect = answers.count_incorrect(user_id)

    signups_fixed = []
    for value in signups_list:
        stripped_value = str(value).strip('(),')
        fixed_value = stripped_value.replace("'", "")
        signups_fixed.append(fixed_value)

    correct_list = []
    for value in correct:
        correct_list.append(str(value).strip('(),'))

    incorrect_list = []
    for value in incorrect:
        incorrect_list.append(str(value).strip('(),'))

    return render_template("profile.html", signups=signups_fixed, correct=correct_list, incorrect=incorrect_list)

@app.route("/result", methods=["POST"])
def check_answer():
    exercise_id = request.form["exercise_id"]
    answer = request.form["answer"]
    course_id = request.form["course_id"]
    user_id = users.get_user()

    try:
        correct = answers.check_answer(exercise_id, user_id, answer, course_id)
        return render_template("result.html", correct=correct, exercise_id=exercise_id)
    except:
        return render_template("error.html", message="Virhe vastausta tarkistettaessa. Jotain meni rikki!")

@app.route("/signup", methods=["POST"])
def signup():
    user_id = users.get_user()
    users.check_csrf()
    course_id = request.form["course_id"]
    try:
        if signups.sign_up(user_id, course_id):
            return redirect("/course/" + str(course_id))
    except:
        return render_template("error.html", message="Virhe ilmoittautumisessa. Jotain meni rikki!")

@app.route("/removesignup", methods=["POST"])
def remove_signup():
    user_id = users.get_user()
    users.check_csrf()
    course_id = request.form["course_id"]
    try:
        if signups.remove_signup(user_id, course_id):
            return redirect("/course/" + str(course_id))
    except:
        return render_template("error.html", message="Virhe poistamisessa. Jotain meni rikki!")

@app.route("/exercise/<int:exercise_id>", methods=["GET", "POST"])
def get_exercise(exercise_id):
    exercise_list = exercises.get_exercise(exercise_id)
    course_id = exercises.get_course(exercise_id)
    string_course = str(course_id).strip("(),")
    user_id = users.get_user()
    check = signups.check_signup(user_id, string_course)
    return render_template("exercise.html", exercises=exercise_list, exercise_id=exercise_id, course_id=string_course, check_signup=check)

@app.route("/add/<int:course_id>", methods=["POST"])
def add_exercise(course_id):
    users.check_role(2)
    users.check_csrf()

    name = request.form["name"]
    content = request.form["content"]
    correct = request.form["correct"]

    try:
        if len(content) < 1 or len(content) > 50:
            return render_template("error.html", message="Tehtävä on liian pitkä! Pidä tehtävä 1-50 merkin pituisena.")
        value = exercises.add_exercise(name, content, correct, course_id)
        if value == True:
            return redirect("/course/" + str(course_id))
        else:
            return render_template("error.html", message="Virhe tehtävää lisätessä.")
    except:
        return render_template("error.html", message="Jotain meni vikaan tehtävää lisätessä.")

@app.route("/remove/<int:course_id>", methods=["POST"])
def remove_exercise(course_id):
    users.check_role(2)
    users.check_csrf()

    exercise_name = request.form["exercise_name"]
    try:
        value = exercises.remove_exercise(course_id, exercise_name)
        if value == True:
            return redirect("/course/" + str(course_id))
        else:
            return redirect("error.html", message="Virhe tehtävää poistaessa. Kirjoititko tehtävän nimen oikein?")
    except:
        return render_template("error.html", message="Jotain meni vikaan tehtävää poistaessa.")

@app.route("/course/<int:course_id>")
def course(course_id):
    user_id = users.get_user()
    exercise_list = exercises.get_exercises(course_id)
    check = signups.check_signup(user_id, course_id)
    name = courses.get_name(course_id)
    string_name = str(name).strip('(),')
    string_fixed = string_name.replace("'", "")
    return render_template("course.html", course_id=course_id, exercises=exercise_list, check=check, course_name=string_fixed)

@app.route("/")
def index():
    course_list = courses.get_list()
    return render_template("index.html", courses=course_list)

@app.route("/add", methods=["GET", "POST"])
def add_course():
    users.check_role(2)

    if request.method == "GET":
        course_list = courses.get_list()
        return render_template("add.html", courses=course_list)

    if request.method == "POST":
        users.check_csrf()
        name = request.form["name"]
        if len(name) < 1 or len(name) > 20:
            return render_template("error.html", message="Kurssin nimi ei vastaa vaatimuksia. Sen täytyy olla 1-20 merkkiä pitkä.")
    try:
        value = courses.add_course(name)
        if value == True:
            return redirect("/add")
        else:
            return render_template("error.html", message="Jotain meni vikaan kurssia luodessa.")
    except:
        return render_template("error.html", message="Jotain meni vikaan! Kurssin luominen epäonnistui.")

@app.route("/remove", methods=["GET", "POST"])
def remove_course():
    users.check_role(2)

    if request.method == "GET":
        course_list = courses.get_list()
        return render_template("remove.html", courses=course_list)

    if request.method == "POST":
        users.check_csrf()
        name = request.form["name"]

    try:
        value = courses.remove_course(name)
        if value == True:
            return redirect("/remove")
        else:
            return render_template("error.html", message="Jotain meni vikaan kurssia poistaessa.")
    except:
        return render_template("error.html", message="Jotain meni vikaan! Kurssin poistaminen epäonnistui.")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":
        username = request.form["username"]
        if len(username) < 1 or len(username) > 20:
            return render_template("error.html", message="Käyttäjätunnus on väärän pituinen. Sen täytyy olla 1-20 merkkiä pitkä.")
        password1 = request.form["password1"]
        password2 = request.form["password2"]

        if password1 != password2:
            return render_template("error.html", message="Salasanat ovat erit. Kokeile uudestaan.")
        role = request.form["role"]
        if users.register(username, password1, role):
            return redirect("/")
        else:
            return render_template("error.html", message="Rekisteröinti epäonnistui. Onko käyttäjä jo olemassa?")

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
        return render_template("error.html", message="Väärä käyttäjätunnus tai salasana.")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")
