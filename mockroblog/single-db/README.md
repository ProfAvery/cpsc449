# Sample API calls

**`createUser(username, email, password)`**

> ```shell-session
> $ http POST localhost:5000/users/ username=tester email=test@example.com password=testing
> ```

**`authenticateUser(username, password)`**

> ```shell-session
> $ http GET 'localhost:5000/users/?username=ProfAvery&password=password'
> ```

**`addFollower(username, usernameToFollow)`**

> ```shell-session
> $ http POST localhost:5000/followers/ follower_id=4 following_id=2
> ```

**`removeFollower(username, usernameToRemove)`**

> ```shell-session
> $ id=$(http GET 'localhost:5000/followers/?follower_id=4&following_id=2' | jq .resources[0].id)
> $ http DELETE localhost:5000/followers/$id
> ```

**`getUserTimeline(username)`**

> ```shell-session
> $ http GET 'localhost:5000/posts/?user_id=1&sort=-timestamp'
> ```

**`getPublicTimeline()`**

> ```shell-session
> $ http GET localhost:5000/posts/?sort=-timestamp
> ```

**`getHomeTimeline(username)`**

> ```shell-session
> $ http GET 'localhost:5100/mockroblog/home.json?_facet=username&username=ProfAvery&_shape=array'
> ```

**`postTweet(username, text)`**

> ```shell-session
> $ http POST localhost:5000/posts/ user_id=4 text='This is a test.'
> ```
