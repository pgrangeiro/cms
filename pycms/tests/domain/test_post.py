# coding: utf-8
from unittest import TestCase

from pycms.domain import Category, Post, User
from pycms.exceptions import UnexpectedCategoryObject, UnexpectedUserObject


class PostTestCase(TestCase):

    def test_initializes_obj_correctly(self):
        category, user = Category(1, 'category'), User(2, 'username', 'name', 'surname', 'photo', 'bio')

        instance = Post(1, 'title', 'content', 'created_at', 'updated_at', [category], user, True)

        self.assertEqual(1, instance.id)
        self.assertEqual('title', instance.title)
        self.assertEqual('content', instance.content)
        self.assertEqual('created_at', instance.created_at)
        self.assertEqual('updated_at', instance.updated_at)
        self.assertEqual([category], instance.categories)
        self.assertEqual(user, instance.user)
        self.assertEqual(True, instance.is_draft)

    def test_init_raises_exception_if_user_is_not_an_user_instance(self):
        category = Category(1, 'category')

        self.assertRaises(UnexpectedUserObject, Post, 1, 'title', 'content', 'created_at', 'updated_at', [category], 'user', True)

    def test_add_category_raises_exception_if_categories_has_a_non_category_obj(self):
        category, user = Category(1, 'category'), User(2, 'username', 'name', 'surname', 'photo', 'bio')
        self.assertRaises(UnexpectedCategoryObject, Post, 1, 'title', 'content', 'created_at', 'updated_at', [category, 2], user, True)
