CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    user_name VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);


CREATE TABLE IF NOT EXISTS surveys (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    created_by INT,
    created_at TIMESTAMP DEFAULT NOW(),
    is_anonymous BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (created_by) REFERENCES users(id) ON DELETE SET NULL
);


CREATE TABLE IF NOT EXISTS options (
    id SERIAL PRIMARY KEY,
    description TEXT,
    created_at TIMESTAMP DEFAULT NOW(),
    survey_id INT NOT NULL,
    FOREIGN KEY (survey_id) REFERENCES surveys(id) ON DELETE SET NULL
);


CREATE TABLE IF NOT EXISTS votes (
    id SERIAL PRIMARY KEY,
    survey_id INT NOT NULL,
    user_id INT,
    voter_ip VARCHAR(50),
    created_at TIMESTAMP DEFAULT NOW(),
    FOREIGN KEY (survey_id) REFERENCES surveys(id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE SET NULL,
    UNIQUE (survey_id, user_id),
    UNIQUE(survey_id, voter_ip)
);


CREATE TABLE IF NOT EXISTS vote_options (
    id SERIAL PRIMARY KEY,
    vote_id INT NOT NULL,
    option_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    FOREIGN KEY (vote_id) REFERENCES votes(id) ON DELETE CASCADE,
    FOREIGN KEY (option_id) REFERENCES options(id) ON DELETE CASCADE,
    UNIQUE (vote_id, option_id)
);
