# coding: utf-8
from pycms.repositories import PostRepository


class ListPostsUseCase(object):

    def __init__(self, dao):
        self.repository = PostRepository(dao)

    def execute(self, title, content, user_id):
        return self.repository.filter(title, content, user_id)
