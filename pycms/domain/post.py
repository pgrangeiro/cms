# coding: utf-8


class Post(object):

    def __init__(self, id, title, content, created_at, updated_at, categories, user, is_draft):
        self.id = id
        self.title = title
        self.content = content
        self.created_at = created_at
        self.updated_at = updated_at
        self.categories = categories or []
        self.user = user
        self.is_draft = is_draft or False

    def add_category(self, category):
        self.categories.append(category)
