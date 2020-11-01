PRAGMA foreign_keys=ON;

CREATE TABLE IF NOT EXISTS users (
    id        INTEGER PRIMARY KEY,
    username  TEXT NOT NULL UNIQUE,
    email     TEXT NOT NULL UNIQUE,
    password  TEXT NOT NULL
);
INSERT INTO users VALUES(1, 'ProfAvery', 'kavery@fullerton.edu', 'password');
INSERT INTO users VALUES(2, 'KevinAWortman', 'kwortman@fullerton.edu', 'qwerty');
INSERT INTO users VALUES(3, 'Beth_CSUF', 'beth.harnick.shapiro@fullerton.edu', 'secret');

CREATE TABLE IF NOT EXISTS followers (
    id            INTEGER PRIMARY KEY,
    follower_id   INTEGER NOT NULL,
    following_id  INTEGER NOT NULL,

    FOREIGN KEY(follower_id) REFERENCES users(id),
    FOREIGN KEY(following_id) REFERENCES users(id),
    UNIQUE(follower_id, following_id)
);
INSERT INTO followers(follower_id, following_id) VALUES(1, 2);
INSERT INTO followers(follower_id, following_id) VALUES(1, 3);
INSERT INTO followers(follower_id, following_id) VALUES(2, 1);
INSERT INTO followers(follower_id, following_id) VALUES(2, 3);
INSERT INTO followers(follower_id, following_id) VALUES(3, 2);

CREATE TABLE IF NOT EXISTS posts (
    id          INTEGER PRIMARY KEY,
    user_id     INTEGER NOT NULL,
    text        TEXT NOT NULL,
    timestamp   INTEGER DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(user_id) REFERENCES users(id)
);
INSERT INTO posts(user_id, text) VALUES(1, 'Meanwhile, at the R1 institution down the street... https://uci.edu/coronavirus/messages/200710-sanitizer-recall.php');
INSERT INTO posts(user_id, text) VALUES(1, 'FYI: https://www.levels.fyi/still-hiring/');
INSERT INTO posts(user_id, text) VALUES(1, 'Yes, the header file ends in .h. C++ is for masochists.');
INSERT INTO posts(user_id, text) VALUES(2, 'If academia were a video game, then a 2.5 hour administrative meeting that votes to extend time 15 minutes is a fatality. FINISH HIM');
INSERT INTO posts(user_id, text) VALUES(2, 'I keep seeing video from before COVID, of people not needing to mask or distance, and doing something like waiting in line at Burger King. YOU''RE WASTING IT!');
INSERT INTO posts(user_id, text) VALUES(3, '#cpsc315 #engr190w NeurIPS is $25 for students and $100 for non-students this year! https://medium.com/@NeurIPSConf/neurips-registration-opens-soon-67111581de99');

CREATE INDEX IF NOT EXISTS post_user_id_idx ON posts(user_id);
CREATE INDEX IF NOT EXISTS post_timestamp_idx ON posts(timestamp);

CREATE VIEW IF NOT EXISTS home
AS
    SELECT users.username, friends.username as friendname, text, timestamp
    FROM users, followers, users AS friends, posts
    WHERE
        users.id = followers.follower_id AND
        followers.following_id = friends.id AND
        friends.id = posts.user_id;

