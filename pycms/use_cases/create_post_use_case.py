# coding: utf-8
from pycms.repositories import PostRepository


class CreatePostUseCase(object):

    def __init__(self, dao):
        self.repository = PostRepository(dao)

    def execute(self, title, content, user_id, is_draft=True):
        self.repository.create(title, content, user_id, is_draft)
