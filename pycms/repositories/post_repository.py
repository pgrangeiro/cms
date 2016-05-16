# coding: utf-8
from datetime import date


class PostRepository(object):

    def __init__(self, dao):
        self.dao = dao

    def create(self, **kwargs):
        created_at = date.today()
        self.dao.create(created_at=created_at, **kwargs)

    def delete(self, id):
        self.dao.delete(id=id)

    def filter(self, **kwargs):
        return self.dao.filter(**kwargs)

    def update(self, id, **kwargs):
        updated_at = date.today()
        self.dao.update(id=id, updated_at=updated_at, **kwargs)

    def get(self, id):
        return self.dao.get(id=id)
