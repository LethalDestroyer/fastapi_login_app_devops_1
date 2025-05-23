from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from app.routes import login

app = FastAPI()
app.include_router(login.router)


# Define the templates directory
templates = Jinja2Templates(directory="app/templates")
app.mount('/static', StaticFiles(directory="app/static"), name="static")

@app.get("/")
async def root(request:Request):
    return templates.TemplateResponse("login.html", {"request": request})

