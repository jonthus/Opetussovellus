from db import db

def add_exercise(name, content, correct, course_id):
    sql = "INSERT INTO exercises (name, content, correct, course_id, visible) VALUES (:name, :content, :correct, :course_id, 1)"
    db.session.execute(sql, {"name": name, "content": content, "correct": correct, "course_id": course_id})
    db.session.commit()
    return 'OK'

def get_exercise(exercise_id):
    sql = "SELECT * FROM exercises WHERE id=:id"
    result = db.session.execute(sql, {"id":exercise_id})
    return result.fetchall()

def get_exercises(course_id):
    sql = "SELECT * FROM exercises WHERE course_id=:course_id AND visible=1"
    result = db.session.execute(sql, {"course_id":course_id})
    return result.fetchall()

def remove_exercise(course_id, name):
    sql = "UPDATE exercises SET VISIBLE=0 WHERE course_id=:course_id AND name=:name"
    db.session.execute(sql, {"course_id":course_id, "name":name})
    db.session.commit()
    return 'OK'
