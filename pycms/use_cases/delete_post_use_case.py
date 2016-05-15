# coding: utf-8
from pycms.repositories import PostRepository


class DeletePostUseCase(object):

    def __init__(self, dao):
        self.repository = PostRepository(dao)

    def execute(self, id):
        self.repository.delete(id)
