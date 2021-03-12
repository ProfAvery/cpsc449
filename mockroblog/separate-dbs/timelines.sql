PRAGMA foreign_keys=ON;

CREATE TABLE IF NOT EXISTS posts (
    id          INTEGER PRIMARY KEY,
    username    INTEGER NOT NULL,
    text        TEXT NOT NULL,
    timestamp   INTEGER DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO posts(username, text) VALUES('ProfAvery', 'Meanwhile, at the R1 institution down the street... https://uci.edu/coronavirus/messages/200710-sanitizer-recall.php');
INSERT INTO posts(username, text) VALUES('ProfAvery', 'FYI: https://www.levels.fyi/still-hiring/');
INSERT INTO posts(username, text) VALUES('ProfAvery', 'Yes, the header file ends in .h. C++ is for masochists.');
INSERT INTO posts(username, text) VALUES('KevinAWortman', 'If academia were a video game, then a 2.5 hour administrative meeting that votes to extend time 15 minutes is a fatality. FINISH HIM');
INSERT INTO posts(username, text) VALUES('KevinAWortman', 'I keep seeing video from before COVID, of people not needing to mask or distance, and doing something like waiting in line at Burger King. YOU''RE WASTING IT!');
INSERT INTO posts(username, text) VALUES('Beth_CSUF', '#cpsc315 #engr190w NeurIPS is $25 for students and $100 for non-students this year! https://medium.com/@NeurIPSConf/neurips-registration-opens-soon-67111581de99');

CREATE INDEX IF NOT EXISTS post_username_idx ON posts(username);
CREATE INDEX IF NOT EXISTS post_timestamp_idx ON posts(timestamp);

