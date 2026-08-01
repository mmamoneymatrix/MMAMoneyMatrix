-- MMAMoneyMatrix Database Schema

-- Fighters Table
CREATE TABLE fighters (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    nickname VARCHAR(255),
    height FLOAT,
    reach FLOAT,
    weight_class VARCHAR(50),
    slpm FLOAT, -- Significant Strikes Landed per Minute
    striking_accuracy FLOAT,
    sapm FLOAT, -- Significant Strikes Absorbed per Minute
    striking_defense FLOAT,
    td_avg FLOAT, -- Average Takedowns Landed per 15 minutes
    td_acc FLOAT, -- Takedown Accuracy
    td_def FLOAT, -- Takedown Defense
    sub_avg FLOAT, -- Average Submissions Attempted per 15 minutes
    gym_tier CHAR(1) DEFAULT 'C', -- S, A, B, C
    underdog_level VARCHAR(20), -- mild, medium, strong, heavy
    cardio_index INTEGER DEFAULT 50,
    damage_tolerance INTEGER DEFAULT 50,
    style_tags TEXT[], -- e.g., ['striker', 'wrestler', 'bjj']
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Fights Table
CREATE TABLE fights (
    id SERIAL PRIMARY KEY,
    fighter_a_id INTEGER REFERENCES fighters(id),
    fighter_b_id INTEGER REFERENCES fighters(id),
    winner_id INTEGER REFERENCES fighters(id),
    method VARCHAR(100), -- KO/TKO, Submission, Decision
    round INTEGER,
    time VARCHAR(10),
    event_name VARCHAR(255),
    fight_date DATE,
    context_notes TEXT, -- short notice, altitude, etc.
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Styles Table
CREATE TABLE styles (
    id SERIAL PRIMARY KEY,
    style_name VARCHAR(50) UNIQUE,
    striking_modifier FLOAT,
    grappling_modifier FLOAT,
    pace_modifier FLOAT,
    description TEXT
);

-- Insert Default Styles
INSERT INTO styles (style_name, striking_modifier, grappling_modifier, pace_modifier) VALUES
('Striker', 1.2, 0.8, 1.0),
('Wrestler', 0.8, 1.3, 1.1),
('BJJ Specialist', 0.7, 1.4, 0.9),
('All-Rounder', 1.0, 1.0, 1.0);
