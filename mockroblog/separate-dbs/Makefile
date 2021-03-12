.PHONY: all clean

all: users.db timelines.db

users.db: users.sql
	sqlite3 $@ < $<

timelines.db: timelines.sql
	sqlite3 $@ < $<

clean:
	rm -f users.db timelines.db
