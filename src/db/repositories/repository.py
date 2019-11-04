from pony.orm.core import Entity


class Repository:
    def create(self, entity: Entity):
        raise NotImplementedError

    def read(self):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def delete(self):
        raise NotImplementedError
