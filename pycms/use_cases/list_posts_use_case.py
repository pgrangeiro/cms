# coding: utf-8
from pycms.repositories import PostRepository


class ListPostsUseCase(object):

    def __init__(self, dao):
        self.repository = PostRepository(dao)

    def execute(self, **kwargs):
        return self.repository.filter(**kwargs)
