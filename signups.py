from db import db
from flask import Flask, session

def sign_up(user_id, course_id):
    sql = "INSERT INTO signups (user_id, time, course_id) VALUES (:user_id, NOW(), :course_id)"
    db.session.execute(sql, {"user_id": user_id, "course_id": course_id})
    db.session.commit()
    return 'OK'

def check_signup(user_id, course_id):
    sql = "SELECT 1 FROM signups WHERE user_id=:user_id AND course_id=:course_id"
    check = db.session.execute(sql, {"user_id": user_id, "course_id": course_id}).fetchone()
    if not check:
        check = False
        return check
    else:
        check = True
        return check

def get_signups(user_id):
    sql = "SELECT * FROM signups WHERE user_id=:user_id"
    list = db.session.execute(sql, {"user_id": user_id}).fetchall()
    return list


