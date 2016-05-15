# coding: utf-8
import unittest
from mock import Mock, patch

from pycms.use_cases import CreatePostUseCase


class CreatePostUseCaseTestCase(unittest.TestCase):

    def setUp(self):
        self.dao = Mock()
        self.repository = patch('pycms.use_cases.create_post_use_case.PostRepository').start()
        self.kwargs = {
            'title': 'Title',
            'content': 'Content',
            'user_id': 'User ID',
        }

    def test_initializes_instance_correctly(self):
        instance = CreatePostUseCase(self.dao)

        self.repository.assert_called_once_with(self.dao)
        self.assertEqual(self.repository(), instance.repository)

    def test_execute_calls_repository_correctly(self):
        instance = CreatePostUseCase(self.dao)

        instance.execute(**self.kwargs)
        self.repository().create.assert_called_once_with('Title', 'Content', 'User ID', True)

    def test_execute_calls_repository_correctly_with_draft_param(self):
        self.kwargs['is_draft'] = False
        instance = CreatePostUseCase(self.dao)

        instance.execute(**self.kwargs)

        self.repository().create.assert_called_once_with('Title', 'Content', 'User ID', False)
