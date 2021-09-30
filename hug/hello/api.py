# $ http POST localhost:8000/greet first_name=Prof last_name=Avery
import hug


@hug.static("/static")
def server_static():
    return ("static",)


@hug.get("/")
def show_form():
    hug.redirect.to("/static/form.html")


@hug.post("/greet")
def return_greeting(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    print(full_name)

    return {"name": full_name}
