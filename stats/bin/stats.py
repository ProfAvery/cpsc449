#!/usr/bin/env python3

import contextlib
import datetime
import random
import sqlite3

import faker

DATABASE = './var/stats.db'
SCHEMA = './share/stats.sql'

NUM_STATS = 1_000_000
NUM_USERS = 100_000
YEAR = 2022

random.seed(YEAR)
fake = faker.Faker()
fake.seed(YEAR)
with contextlib.closing(sqlite3.connect(DATABASE)) as db:
    with open(SCHEMA) as f:
        db.executescript(f.read())
    for _ in range(NUM_USERS):
        while True:
            try:
                profile = fake.simple_profile()
                db.execute('INSERT INTO users(username) VALUES(:username)', profile)

            except sqlite3.IntegrityError:
                continue
            break
    db.commit()
    jan_1 = datetime.date(YEAR, 1, 1)
    today = datetime.date.today()
    num_days = (today - jan_1).days
    i = 0
    while i < NUM_STATS:
        while True:
            try:
                user_id = random.randint(1, NUM_USERS)
                game_id = random.randint(1, num_days)
                finished = jan_1 + datetime.timedelta(random.randint(0, num_days))
                # N.B. real game scores aren't uniformly distributed...
                guesses = random.randint(1, 6)
                # ... and people mostly play to win
                won = random.choice([False, True, True, True])
                db.execute(
                    """
                    INSERT INTO games(user_id, game_id, finished, guesses, won)
                    VALUES(?, ?, ?, ?, ?)
                    """,
                    [user_id, game_id, finished, guesses, won]
                )
            except sqlite3.IntegrityError:
                continue
            i += 1
            break
    db.commit()
