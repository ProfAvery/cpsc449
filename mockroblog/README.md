# Mockroblog - Mock APIs for Microblogging

**Q.** What's the minimum amount of code needed to mock up a miniature
       clone of Twitter?

**A.** How comfortable are you with SQL?

## Getting started

Use the following commands to get up and running:

```shell-session
$ python3 -m pip install sandman2 datasette   # install utilities
$ make                                        # create database
$ foreman start                               # start services
```

## Tools

See the following references for more information:

* [sandman2](https://github.com/jeffknupp/sandman2)
* [datasette](https://github.com/simonw/datasette)
* [make](https://en.wikipedia.org/wiki/Makefile)
* [sqlite3](https://sqlite.org/cli.html)
* [foreman](https://ddollar.github.io/foreman/)
* [http](https://httpie.org/)
* [jq](https://stedolan.github.io/jq/)

## Client-side API

As a reminder, here is the original API client contract:

API call                                     | Action
-------------------------------------------- | -----------------------------------------------------------------------------------------------------------
`createUser(username, email, password)`      | Registers a new user account.
`authenticateUser(username, password)`       | Returns true if the password parameter matches the password stored for that username.
`addFollower(username, usernameToFollow)`    | Start following a new user.
`removeFollower(username, usernameToRemove)` | Stop following a user.
`getUserTimeline(username)`                  | Returns recent posts from a user.
`getPublicTimeline()`                        | Returns recent posts from all users.
`getHomeTimeline(username)`                  | Returns recent posts from all users that this user follows.
`postTweet(username, text)`                  | Post a new tweet.

### Server-side API implementations

The effect of each of these API calls can be duplicated by connecting
`sandman2` and Datasette to SQLite databases and calling the APIs supplied
by those tools.

Note that this is *not* as nice an experience as using a well-designed
custom API. There are multiple cases where `sandman2` requires a
primary key (e.g. user ID) where a different key (e.g. username) would
be preferable.

There are two different versions:
 * `single-db/`: one database with tables connected by foreign keys
 * `separate-dbs/`: two databases, one for users and one for posts

