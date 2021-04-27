# Skeleton code for the Timelines API

This directory contains skeleton code for a microservice implementing
the Timelines API.

This code:

* uses the [Bottle-Sqlite](https://bottlepy.org/docs/0.12/plugins/sqlite.html) plugin

* sets the database to `timelines.db`

* sets up logging, disables warnings, and configures JSON error handling

* includes convenience methods for DB access

* provides routes and API functions for all methods in the Timelines
  API specified below

* hard-codes GET methods to return an empty JSON object


## API

API call                                     | Route                          | Action
-------------------------------------------- | -------------------------------| ------------------------------------------------------------
`getPublicTimeline()`                        | `GET  /`                       | Returns recent tweets from all users.
`getUserTimeline(username)`                  | `GET  /<string:username>/`     | Returns recent tweets from a user.
`postTweet(username, text)`                  | `POST /<string:username>/`     | Post a new tweet.
`getHomeTimeline(username)`                  | `GET  /<string:username>/home` | Returns recent tweets from all users that this user follows.

