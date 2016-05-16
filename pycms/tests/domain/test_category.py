# coding: utf-8
from unittest import TestCase
from pycms.domain import Category


class CategoryTestCase(TestCase):

    def test_initializes_obj_correctly(self):
        instance = Category(1, 'name')
        self.assertEqual(1, instance.id)
        self.assertEqual('name', instance.name)
