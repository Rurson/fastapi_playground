from collections import defaultdict
from dataclasses import dataclass

import uvicorn
from fastapi import FastAPI, Form
from starlette.requests import Request
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

my_list = ["Hello", "World"]
api = FastAPI()
templates = Jinja2Templates(directory="templates")
api.mount("/static", StaticFiles(directory="static"), name="static")


@dataclass
class User:
    name: str
    password: str
    id: int = None


db = defaultdict(list)


@api.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", context={"request": request, "my_list": my_list})


@api.get("/registration")
async def user_get(request: Request):
    return templates.TemplateResponse("forms/registration.html", context={"request": request})


@api.post("/registration")
async def user_post(request: Request, username: str = Form(...), password: str = Form(...)):
    db["users"].append(User(name=username, password=password))
    return templates.TemplateResponse("users.html", context={"request": request, "users": db["users"]})


@api.get("/users")
async def user_get(request: Request):
    return templates.TemplateResponse("users.html", context={"request": request, "users": db["users"]})
