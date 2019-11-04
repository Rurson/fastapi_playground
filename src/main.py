import os
from collections import defaultdict
from dataclasses import dataclass

from fastapi import FastAPI, Form
from pony.orm import db_session, commit, select
from starlette.requests import Request
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from db import db
from db.entities.user import User
from db.repositories.user_repository import UserRepository

my_list = ["Hello", "World"]
api = FastAPI()
templates = Jinja2Templates(directory="templates")
api.mount("/static", StaticFiles(directory="static"), name="static")

provider = os.getenv("DATABASE_PROVIDER", "postgres")
user = os.getenv("DATABASE_USER", "postgres")
password = os.getenv("DATABASE_PASSWORD", "pass")
host = os.getenv("DATABASE_HOST", "localhost")
database = os.getenv("DATABASE_DATABASE", "fastapi")

db.bind(
    provider=provider,
    user=user,
    password=password,
    host=host,
    database=database,
)
db.generate_mapping(create_tables=True)
user_repo = UserRepository()


@dataclass
class User_Entity:
    name: str
    password: str
    id: int = None


db_d = defaultdict(list)


@api.get("/")
async def index(request: Request):
    return templates.TemplateResponse(
        "index.html", context={"request": request, "my_list": my_list}
    )


@api.get("/registration")
async def user_get(request: Request):
    return templates.TemplateResponse(
        "forms/registration.html", context={"request": request}
    )


@api.post("/registration")
async def user_post(
        request: Request, username: str = Form(...), password: str = Form(...)
):
    user_repo.create(username, password)
    users = user_repo.get_all()
    return templates.TemplateResponse(
        "users.html", context={"request": request, "users": users}
    )


@api.get("/users")
async def user_get(request: Request):
    users = user_repo.get_all()
    return templates.TemplateResponse(
        "users.html", context={"request": request, "users": users}
    )
