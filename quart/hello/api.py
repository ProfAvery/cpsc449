from quart import Quart, request, redirect, url_for

app = Quart(__name__)


@app.route("/")
async def show_form():
    return redirect(url_for("static", filename="form.html"))


@app.route("/greet", methods=["POST"])
async def return_greeting():
    data = await request.get_json()

    full_name = f"{data['first_name']} {data['last_name']}"
    app.logger.debug(full_name)

    return {"name": full_name}
