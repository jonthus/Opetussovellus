CREATE TABLE Users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
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
    content TEXT
);
