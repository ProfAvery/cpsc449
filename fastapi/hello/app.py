# uvicorn app:app --reload

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def show_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})


@app.post("/greet", response_class=HTMLResponse)
def return_greeting(
    request: Request, first_name: str = Form(...), last_name: str = Form(...)
):
    full_name = f"{first_name} {last_name}"
    print(full_name)

    return templates.TemplateResponse(
        "form.html", {"request": request, "name": full_name}
    )
