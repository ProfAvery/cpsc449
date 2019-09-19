-- :name book_by_id :one
SELECT * FROM books
WHERE id = :id;
