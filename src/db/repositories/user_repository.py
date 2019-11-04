from db.repositories.repository import Repository
from db.entities.user import User


class UserRepository(Repository):
    def create(self, user: User):
        raise NotImplementedError

    def read(self):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def delete(self):
        raise NotImplementedError
