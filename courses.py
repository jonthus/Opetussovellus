from db import db

def add_course(name, content, user_id):
    sql = "INSERT INTO courses (user_id, name) VALUES (:user_id, :name)"
    db.session.execute(sql, {"user_id":user_id, "name":name})
    sql = "INSERT INTO exercises (exercise_id, content)"
    db.session.execute(sql, {"exercise_id":exercise_id, "content":content})
    db.session.commit() 

def remove_course(course_id)
    sql = "UPDATE courses SET VISIBLE=0 WHERE id=:id"
    db.session.execute(sql, {"id":course_id})
    db.session.commit()
