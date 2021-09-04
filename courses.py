from db import db

def get_list():
    sql = "SELECT * FROM courses WHERE visible=1"
    result = db.session.execute(sql)
    return result.fetchall()

def add_course(name):
    sql = "INSERT INTO courses (name, visible) VALUES (:name, 1)"
    db.session.execute(sql, {"name":name})
    db.session.commit()
    return True

def remove_course(name):
    sql = "UPDATE courses SET VISIBLE=0 WHERE name=:name"
    db.session.execute(sql, {"name":name})
    db.session.commit()

    course_id = get_id(name)
    fixed_id = str(course_id).strip('(),')
    sql = "DELETE FROM answers WHERE course_id=:course_id"
    db.session.execute(sql, {"course_id":fixed_id})
    db.session.commit()
    return True

def get_name(course_id):
    sql = "SELECT name FROM courses WHERE id=:id"
    name = db.session.execute(sql, {"id":course_id}).fetchone()
    return name

def get_id(name):
    sql = "SELECT id FROM courses WHERE name=:name"
    id = db.session.execute(sql, {"name":name}).fetchone()
    return id

