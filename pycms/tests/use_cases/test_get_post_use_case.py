# coding: utf-8
import unittest
from mock import Mock, patch

from pycms.use_cases import GetPostUseCase


class GetPostUseCaseTestCase(unittest.TestCase):

    def setUp(self):
        self.dao = Mock()
        self.repository = patch('pycms.use_cases.get_post_use_case.PostRepository').start()

    def test_initializes_instance_correctly(self):
        instance = GetPostUseCase(self.dao)

        self.repository.assert_called_once_with(self.dao)
        self.assertEqual(self.repository(), instance.repository)

    def test_execute_calls_repository_correctly(self):
        instance = GetPostUseCase(self.dao)

        post = instance.execute(1)
        self.repository().get.assert_called_once_with(1)
        self.assertEqual(self.repository().get(), post)
