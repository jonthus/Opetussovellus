CREATE TABLE Users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT,
    role INTEGER
);

CREATE TABLE Courses (
    id SERIAL PRIMARY KEY,
    name TEXT,
    visible INTEGER
);

CREATE TABLE Exercises (
    id SERIAL PRIMARY KEY,
    name TEXT,
    content TEXT,
    correct TEXT,
    course_id INTEGER REFERENCES courses,
    visible INTEGER
);

CREATE TABLE Signups (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    time TIMESTAMP
    course_id INTEGER REFERENCES courses 
);

CREATE TABLE Answers (
    id SERIAL PRIMARY KEY,
    correct INTEGER,
    incorrect INTEGER,
    exercise_id INTEGER REFERENCES exercises,
    user_id INTEGER REFERENCES users
);
