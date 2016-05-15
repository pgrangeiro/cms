# coding: utf-8
from datetime import date


class PostRepository(object):

    def __init__(self, dao):
        self.dao = dao

    def create(self, **kwargs):
        created_at = date.today()
        self.dao.create(created_at=created_at, **kwargs)
