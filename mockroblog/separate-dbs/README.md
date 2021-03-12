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
> $ http GET 'localhost:5100/posts/?username=ProfAvery&sort=-timestamp'
> ```

**`getPublicTimeline()`**

> ```shell-session
> $ http GET localhost:5100/posts/?sort=-timestamp
> ```

**`getHomeTimeline(username)`**

> ```shell-session
> $ friends=$(http GET 'localhost:5200/users/following.json?_facet=username&username=ProfAvery&_shape=array' | jq --raw-output 'map(.friendname) | join(",")')
> $ http GET "http://localhost:5300/timelines/posts.json?_sort_desc=timestamp&_shape=array&username__in=$friends"
> ```

**`postTweet(username, text)`**

> ```shell-session
> $ http POST localhost:5100/posts/ username=tester text='This is a test.'
> ```

