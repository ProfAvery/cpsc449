from quart import Quart, request, render_template

app = Quart(__name__)


@app.route("/")
async def show_form():
    return await render_template("form.html")


@app.route("/greet", methods=["POST"])
async def show_greeting():
    form = await request.form

    full_name = f"{form['first_name']} {form['last_name']}"
    app.logger.debug(full_name)

    return await render_template("form.html", name=full_name)
