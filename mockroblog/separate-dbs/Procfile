users: sandman2ctl -p $PORT sqlite+pysqlite:///users.db
timelines: sandman2ctl -p $PORT sqlite+pysqlite:///timelines.db
user-queries: datasette -p $PORT --reload users.db
timeline-queries: datasette -p $PORT --reload timelines.db
