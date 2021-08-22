from db import db
from flask import abort, request, session
from werkzeug.security import check_password_hash, generate_password_hash
import os

def check_role(role):
    if role > session.get("user_role", 0):
        return False

def check_csrf():
    if session["csrf_token"] != request.form["csrf_token"]:
        return False

def login(username, password):
    sql = "SELECT password, id, role FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if not user:
        return False
    else:
        hash_value = user.password
        if check_password_hash(hash_value, password):
            session["user_id"] = user[1]
            session["user_role"] = user[2]
            session["user_name"] = username
            session["csrf_token"] = os.urandom(16).hex()
            return True
        else:
            return False

def logout():
    del session["user_id"]
    del session["user_name"]
    del session["user_role"]

def register(username, password, role):
    hash_value = generate_password_hash(password)
    try:
        sql = "INSERT INTO users (username, password, role) VALUES (:username, :password, :role)"
        db.session.execute(sql, {"username":username, "password":hash_value, "role":role})
        db.session.commit()
    except:
        return False
    return login(username, password)

def get_user():
    return session.get("user_id", 0)
