# coding: utf-8
import unittest
from mock import Mock, patch

from pycms.use_cases import UpdatePostUseCase


class UpdatePostUseCaseTestCase(unittest.TestCase):

    def setUp(self):
        self.dao = Mock()
        self.repository = patch('pycms.use_cases.update_post_use_case.PostRepository').start()
        self.kwargs = {
            'id': 1,
            'title': 'Title',
            'content': 'Content',
            'user_id': 'User ID',
            'is_draft': True,
        }

    def test_initializes_instance_correctly(self):
        instance = UpdatePostUseCase(self.dao)

        self.repository.assert_called_once_with(self.dao)
        self.assertEqual(self.repository(), instance.repository)

    def test_execute_calls_repository_correctly(self):
        instance = UpdatePostUseCase(self.dao)

        instance.execute(**self.kwargs)
        self.repository().update.assert_called_once_with(1, title='Title', content='Content', user_id='User ID', is_draft=True)
