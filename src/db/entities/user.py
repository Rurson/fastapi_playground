from pony.orm.core import Required

from db import db


class User(db.Entity):
    name = Required(str)
    password = Required(str)
