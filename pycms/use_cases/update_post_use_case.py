# coding: utf-8
from pycms.repositories import PostRepository


class UpdatePostUseCase(object):

    def __init__(self, dao):
        self.repository = PostRepository(dao)

    def execute(self, id, **kwargs):
        self.repository.update(id, **kwargs)
