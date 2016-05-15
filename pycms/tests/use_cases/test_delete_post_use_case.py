# coding: utf-8
import unittest
from mock import Mock, patch

from pycms.use_cases import DeletePostUseCase


class DeletePostUseCaseTestCase(unittest.TestCase):

    def setUp(self):
        self.dao = Mock()
        self.repository = patch('pycms.use_cases.delete_post_use_case.PostRepository').start()

    def test_initializes_instance_correctly(self):
        instance = DeletePostUseCase(self.dao)

        self.repository.assert_called_once_with(self.dao)
        self.assertEqual(self.repository(), instance.repository)

    def test_execute_calls_repository_correctly(self):
        instance = DeletePostUseCase(self.dao)

        instance.execute(1)
        self.repository().delete.assert_called_once_with(1)
