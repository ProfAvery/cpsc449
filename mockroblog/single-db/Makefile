.PHONY: clean

mockroblog.db: mockroblog.sql
	sqlite3 $@ < $<

clean:
	rm -f mockroblog.db
