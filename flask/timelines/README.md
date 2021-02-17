# Skeleton code for the Timelines API

This directory contains skeleton code for a microservice implementing
the Timelines API.

This code:

* includes the [Flask SQLite 3 helper
  routines](https://flask.palletsprojects.com/en/1.1.x/patterns/sqlite3/)

* sets the database to `mockroblog.db`

* provides routes and API functions for all methods in the Timelines
  API specified below

* hard-codes all methods to return an empty JSON object or list


## API

API call                                     | Route                          | Action
-------------------------------------------- | -------------------------------| ------------------------------------------------------------
`getPublicTimeline()`                        | `GET  /`                       | Returns recent tweets from all users.
`getUserTimeline(username)`                  | `GET  /<string:username>/`     | Returns recent tweets from a user.
`postTweet(username, text)`                  | `POST /<string:username>/`     | Post a new tweet.
`getHomeTimeline(username)`                  | `GET  /<string:username>/home` | Returns recent tweets from all users that this user follows.

