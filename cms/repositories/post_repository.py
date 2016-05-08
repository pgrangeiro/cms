# coding: utf-8


class PostRepository(object):

    def __init__(self, dao):
        self.dao = dao

    def create(self, **kwargs):
        self.dao.create(**kwargs)
