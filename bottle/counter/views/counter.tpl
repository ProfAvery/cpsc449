<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Counter example</title>
    </head>
    <body>
        <h1>Counter 1: {{ counter1 }}</h1>
        <h1>Counter 2: {{ counter2 }}</h1>
        <p>
            <form method="POST" action="/increment">
                <input type="submit" value="Increment Counter 2" />
            </form>
        </p>
        <p>
            <form method="POST" action="/reset">
                <input type="submit" value="Reset" />
            </form>
        </p>
    </body>
</html>
