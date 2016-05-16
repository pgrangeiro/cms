# coding: utf-8
import unittest

from datetime import date
from mock import Mock

from pycms.repositories import PostRepository


class PostRepositoryTestCase(unittest.TestCase):

    def setUp(self):
        self.dao = Mock()
        self.kwargs = {
            'title': 'Title',
            'content': 'Content',
            'user_id': 'User ID',
        }

    def test_initializes_instance_correctly(self):
        instance = PostRepository(self.dao)
        self.assertEqual(self.dao, instance.dao)

    def test_create_calls_dao_correctly(self):
        instance = PostRepository(self.dao)

        instance.create(**self.kwargs)
        self.dao.create.assert_called_once_with(created_at=date.today(), **self.kwargs)

    def test_delete_calls_dao_correctly(self):
        instance = PostRepository(self.dao)

        instance.delete(id=1)
        self.dao.delete.assert_called_once_with(id=1)

    def test_filter_calls_dao_correctly(self):
        instance = PostRepository(self.dao)

        posts = instance.filter(**self.kwargs)
        self.dao.filter.assert_called_once_with(**self.kwargs)
        self.assertEqual(self.dao.filter(), posts)

    def test_update_calls_dao_correctly(self):
        instance = PostRepository(self.dao)

        instance.update(id=1, **self.kwargs)
        self.dao.update.assert_called_once_with(id=1, updated_at=date.today(), **self.kwargs)

    def test_get_calls_dao_correctly(self):
        instance = PostRepository(self.dao)

        post = instance.get(id=1)
        self.dao.get.assert_called_once_with(id=1)
        self.assertEqual(self.dao.get(), post)
