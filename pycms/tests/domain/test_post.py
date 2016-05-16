# coding: utf-8
from unittest import TestCase
from pycms.domain import Post


class PostTestCase(TestCase):

    def test_initializes_obj_correctly(self):
        instance = Post(1, 'title', 'content', 'created_at', 'updated_at', [1], 'user', True)
        self.assertEqual(1, instance.id)
        self.assertEqual('title', instance.title)
        self.assertEqual('content', instance.content)
        self.assertEqual('created_at', instance.created_at)
        self.assertEqual('updated_at', instance.updated_at)
        self.assertEqual([1], instance.categories)
        self.assertEqual('user', instance.user)
        self.assertEqual(True, instance.is_draft)
