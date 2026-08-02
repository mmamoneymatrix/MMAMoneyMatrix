CREATE TABLE fighters (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL,
    nickname VARCHAR(100),
    age INT,
    height_cm INT,
    reach_cm INT,
    stance VARCHAR(50),
    gym VARCHAR(100),
    gym_tier INT DEFAULT 3, -- 1 elite, 5 low-tier
    updated_at TIMESTAMP DEFAULT NOW()
);
CREATE TABLE abilities (
    id SERIAL PRIMARY KEY,
    fighter_id INT REFERENCES fighters(id) ON DELETE CASCADE,
    striking INT,
    grappling INT,
    wrestling INT,
    cardio INT,
    power INT,
    chin INT,
    fight_iq INT,
    aggression INT,
    defense INT,
    UNIQUE(fighter_id)
);
CREATE TABLE stats (
    id SERIAL PRIMARY KEY,
    fighter_id INT REFERENCES fighters(id) ON DELETE CASCADE,
    wins INT DEFAULT 0,
    losses INT DEFAULT 0,
    ko_wins INT DEFAULT 0,
    sub_wins INT DEFAULT 0,
    decision_wins INT DEFAULT 0,
    ko_losses INT DEFAULT 0,
    sub_losses INT DEFAULT 0,
    avg_fight_time FLOAT,
    sig_strikes_landed FLOAT,
    sig_strikes_absorbed FLOAT,
    takedown_accuracy FLOAT,
    takedown_defense FLOAT,
    control_time FLOAT,
    UNIQUE(fighter_id)
);
CREATE TABLE stats (
    id SERIAL PRIMARY KEY,
    fighter_id INT REFERENCES fighters(id) ON DELETE CASCADE,
    wins INT DEFAULT 0,
    losses INT DEFAULT 0,
    ko_wins INT DEFAULT 0,
    sub_wins INT DEFAULT 0,
    decision_wins INT DEFAULT 0,
    ko_losses INT DEFAULT 0,
    sub_losses INT DEFAULT 0,
    avg_fight_time FLOAT,
    sig_strikes_landed FLOAT,
    sig_strikes_absorbed FLOAT,
    takedown_accuracy FLOAT,
    takedown_defense FLOAT,
    control_time FLOAT,
    UNIQUE(fighter_id)
);
CREATE TABLE fight_history (
    id SERIAL PRIMARY KEY,
    fighter_id INT REFERENCES fighters(id) ON DELETE CASCADE,
    opponent_name VARCHAR(100),
    result VARCHAR(20), -- Win/Loss/Draw/NC
    method VARCHAR(50), -- KO, SUB, DEC, etc.
    round INT,
    time VARCHAR(10),
    event VARCHAR(100),
    event_date DATE
);
CREATE TABLE matchups (
    id SERIAL PRIMARY KEY,
    fighter_a INT REFERENCES fighters(id),
    fighter_b INT REFERENCES fighters(id),
    created_at TIMESTAMP DEFAULT NOW()
);
CREATE TABLE simulation_results (
    id SERIAL PRIMARY KEY,
    matchup_id INT REFERENCES matchups(id) ON DELETE CASCADE,
    fighter_a_win_prob FLOAT,
    fighter_b_win_prob FLOAT,
    finish_prob FLOAT,
    decision_prob FLOAT,
    rounds_json TEXT, -- JSON of round-by-round scoring
    created_at TIMESTAMP DEFAULT NOW()
);

