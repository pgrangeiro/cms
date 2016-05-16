# coding: utf-8
from pycms.domain import Category, User
from pycms.exceptions import UnexpectedCategoryObject, UnexpectedUserObject


class Post(object):

    def __init__(self, id, title, content, created_at, updated_at, categories, user, is_draft):
        if not isinstance(user, User):
            raise UnexpectedUserObject

        self.id = id
        self.title = title
        self.content = content
        self.created_at = created_at
        self.updated_at = updated_at
        self.categories = []
        self.user = user
        self.is_draft = is_draft or False

        for category in categories:
            self.add_category(category)

    def add_category(self, category):
        if not isinstance(category, Category):
            raise UnexpectedCategoryObject
        self.categories.append(category)
