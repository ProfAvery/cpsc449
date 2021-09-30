# See <https://code-maven.com/using-templates-in-flask>

from bottle import get, post, request, template


@get("/")
def show_form():
    return template("form", name=None)


@post("/greet")
def show_greeting():
    full_name = f"{request.forms['first_name']} {request.forms['last_name']}"
    print(full_name)

    return template("form", name=full_name)
