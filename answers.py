from db import db

def check_answer(exercise_id, user_id, answer):
    sql = "SELECT correct FROM exercises WHERE id=:id"
    correct = db.session.execute(sql, {"id":exercise_id}).fetchone()

    if answer in correct:
        append_correct(exercise_id, user_id)
        return True
    else:
        append_incorrect(exercise_id, user_id)
        return False

def append_correct(exercise_id, user_id):
    sql = "INSERT INTO answers (exercise_id, user_id, correct) VALUES (:exercise_id, :user_id, 1)"
    db.session.execute(sql, {"exercise_id":exercise_id, "user_id":user_id})
    db.session.commit()
    return 'OK'

def append_incorrect(exercise_id, user_id):
    sql = "INSERT INTO answers (exercise_id, user_id, incorrect) VALUES (:exercise_id, :user_id, 1)"
    db.session.execute(sql, {"exercise_id":exercise_id, "user_id":user_id})
    db.session.commit()
    return 'OK'

def count_correct(user_id):
    sql = "SELECT COUNT(*) FROM answers WHERE user_id=:user_id"
    list = db.session.execute(sql, {"user_id":user_id}).fetchall()
    return list

def count_incorrect(user_id):
    sql = "SELECT COUNT(incorrect) FROM answers WHERE user_id=:user_id"
    list = db.session.execute(sql, {"user_id":user_id}).fetchall()
    return list
