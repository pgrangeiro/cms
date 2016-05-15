# coding: utf-8
from pycms.repositories import PostRepository


class GetPostUseCase(object):

    def __init__(self, dao):
        self.repository = PostRepository(dao)

    def execute(self, id):
        return self.repository.get(id)
