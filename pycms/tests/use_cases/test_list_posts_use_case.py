# coding: utf-8
import unittest
from mock import Mock, patch

from pycms.use_cases import ListPostsUseCase


class ListPostsUseCaseTestCase(unittest.TestCase):

    def setUp(self):
        self.dao = Mock()
        self.repository = patch('pycms.use_cases.list_posts_use_case.PostRepository').start()
        self.kwargs = {
            'title': 'Title',
            'content': 'Content',
            'user_id': 'User ID',
        }

    def test_initializes_instance_correctly(self):
        instance = ListPostsUseCase(self.dao)

        self.repository.assert_called_once_with(self.dao)
        self.assertEqual(self.repository(), instance.repository)

    def test_execute_calls_repository_correctly(self):
        instance = ListPostsUseCase(self.dao)

        posts = instance.execute(**self.kwargs)
        self.repository().filter.assert_called_once_with('Title', 'Content', 'User ID')
        self.assertEqual(self.repository().filter(), posts)
