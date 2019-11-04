from pony.orm import db_session, select

from db.repositories.repository import Repository
from db.entities.user import User
from db import db


class UserRepository(Repository):
    @db_session
    def create(self, name, password):
        user = User(name=name, password=password)
        db.commit()
        return user

    def read(self):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def delete(self):
        raise NotImplementedError

    def get_all(self):
        return select(u for u in User)
