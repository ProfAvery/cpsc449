# $ http POST 127.0.0.1:5000/greet first_name=Prof last_name=Avery

from bottle import get, post, static_file, redirect, request


@get("/")
def show_form():
    return redirect("/static/form.html")


@get("/static/<filepath:path>")
def server_static(filepath):
    return static_file(filepath, root="./static")


@post("/greet")
def return_greeting():
    data = request.json

    full_name = f"{data['first_name']} {data['last_name']}"
    print(full_name)

    return {"name": full_name}
