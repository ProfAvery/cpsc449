import hug


@hug.get("/", output=hug.output_format.html)
def show_form():
    return """
        <!DOCTYPE html>
        <html lang="en">
            <head>
                <title>Dynamically-generated form</title>
            </head>
            <body>
                <form method="POST" action="/greet">
                    <p>
                        <label for="first">First name:</label>
                        <input type="text" id="first" name="first_name" />
                    </p>

                    <p>
                        <label for="last">Last name:</label>
                        <input type="text" id="last" name="last_name" />
                    </p>

                    <p>
                        <input type="submit" />
                    </p>
                </form>
            </body>
        </html>
    """


@hug.post("/greet", output=hug.output_format.html)
def show_greeting(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    print(full_name)

    return f"""
        <!DOCTYPE html>
        <html lang="en">
            <head>
                <title>Dynamically-generated form</title>
            </head>
            <body>
                <form method="POST" action="/greet">
                    <p>
                        <label for="first">First name:</label>
                        <input type="text" id="first" name="first_name" />
                    </p>

                    <p>
                        <label for="last">Last name:</label>
                        <input type="text" id="last" name="last_name" />
                    </p>

                    <p>
                        <input type="submit" />
                    </p>
                </form>

                    <p>
                        Hello, {full_name}!
                    </p>
            </body>
        </html>
    """
