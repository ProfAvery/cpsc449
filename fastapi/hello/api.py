# uvicorn api:app --reload
# $ http POST localhost:8000/greet first_name=Prof last_name=Avery

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


class Person(BaseModel):
    first_name: str
    last_name: str


@app.get("/")
def show_form():
    return RedirectResponse("/static/form.html")


@app.post("/greet")
def return_greeting(person: Person):
    full_name = f"{person.first_name} {person.last_name}"
    print(full_name)

    return {"name": full_name}
