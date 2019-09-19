-- :name create_book :insert
INSERT INTO books(published, author, title, first_sentence)
VALUES(:published, :author, :title, :first_sentence)
