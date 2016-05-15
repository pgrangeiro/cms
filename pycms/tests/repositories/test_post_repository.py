# coding: utf-8
import unittest
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
        self.dao.create.assert_called_once_with(**self.kwargs)
