# foreman start -m gateway=1,users=1,timelines=3,user-queries=1,timeline-queries=1
gateway: python3 -m bottle --bind=localhost:$PORT --debug --reload gateway
users: sandman2ctl -p $PORT sqlite+pysqlite:///../../mockroblog/separate-dbs/users.db
timelines: sandman2ctl -p $PORT sqlite+pysqlite:///../../mockroblog/separate-dbs/timelines.db
user-queries: datasette -p $PORT --reload ../../mockroblog/separate-dbs/users.db
timeline-queries: datasette -p $PORT --reload ../../mockroblog/separate-dbs/timelines.db
