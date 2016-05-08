# coding: utf-8

class PostRepository(object):
    pass


class CreatePostUseCase(object):

    def __init__(self, dao):
        self.repository = PostRepository(dao)

    def execute(self, title, content, user_id):
        self.repository.create(title, content, user_id)
