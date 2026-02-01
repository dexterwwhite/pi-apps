CREATE TABLE IF NOT EXISTS password(
    id INTEGER PRIMARY KEY,
    site TEXT NOT NULL,
    username TEXT,
    password TEXT NOT NULL,
    email TEXT,
    notes TEXT,
    created TEXT,
    last_modified TEXT
) STRICT;