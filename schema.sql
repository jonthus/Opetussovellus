CREATE TABLE Messages (
    id SERIAL PRIMARY KEY,
    content, TEXT
);

CREATE TABLE Users (
    id SERIAL PRIMARY KEY,
    name TEXT,
    password TEXT,
    role INTEGER
);

CREATE TABLE Courses (
    id SERIAL PRIMARY KEY,
    creator_id INTEGER REFERENCES users,
    name TEXT,
    visible INTEGER
);

CREATE TABLE Exercises (
    id SERIAL PRIMARY KEY,
    course_id INTEGER REFERENCES courses,
    content TEXT,
);

CREATE TABLE Answers (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    exercise_id INTEGER REFERENCES exercises,
    sent_at TIMESTAMP,
    result INTEGER
);

CREATE TABLE Grade (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    course_id INTEGER REFERENCES courses,
    grade INTEGER,
    comment TEXT
);
