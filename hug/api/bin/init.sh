#!/bin/sh

sqlite-utils insert ./var/books.db books --csv ./share/books.csv --detect-types --pk=id
sqlite-utils create-index ./var/books.db books published author title --unique
