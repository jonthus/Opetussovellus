from db import db

def check_answer(exercise_id, user_id, answer, course_id):
    sql = "SELECT correct FROM exercises WHERE id=:id"
    correct = db.session.execute(sql, {"id":exercise_id}).fetchone()
    string_correct = str(correct).strip('(),')
    fixed_correct = string_correct.replace("'", "")

    if answer == fixed_correct:
        append_correct(exercise_id, user_id, course_id)
        return True
    else:
        append_incorrect(exercise_id, user_id, course_id)
        return False

def append_correct(exercise_id, user_id, course_id):
    sql = "INSERT INTO answers (exercise_id, user_id, correct, course_id) VALUES (:exercise_id, :user_id, 1, :course_id)"
    db.session.execute(sql, {"exercise_id":exercise_id, "user_id":user_id, "course_id":course_id})
    db.session.commit()

def append_incorrect(exercise_id, user_id, course_id):
    sql = "INSERT INTO answers (exercise_id, user_id, incorrect, course_id) VALUES (:exercise_id, :user_id, 1, :course_id)"
    db.session.execute(sql, {"exercise_id":exercise_id, "user_id":user_id, "course_id":course_id})
    db.session.commit()

def count_correct(user_id):
    sql = """ SELECT COUNT(answers.correct) FROM answers
              INNER JOIN courses ON courses.id = answers.course_id
              INNER JOIN exercises ON exercises.id = answers.exercise_id
              WHERE exercises.visible=1
              AND courses.visible=1
              AND answers.user_id=:user_id """
    list = db.session.execute(sql, {"user_id":user_id}).fetchall()
    return list

def count_incorrect(user_id):
    sql = """ SELECT COUNT(answers.incorrect) FROM answers
              INNER JOIN courses ON courses.id = answers.course_id
              INNER JOIN exercises ON exercises.id = answers.exercise_id
              WHERE exercises.visible=1
              AND courses.visible=1
              AND answers.user_id=:user_id """
    list = db.session.execute(sql, {"user_id":user_id}).fetchall()
    return list
