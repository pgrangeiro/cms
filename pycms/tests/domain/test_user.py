# coding: utf-8
from unittest import TestCase
from pycms.domain import User


class UserTestCase(TestCase):

    def test_initializes_obj_correctly(self):
        instance = User(1, 'username', 'name', 'surname', 'photo', 'bio')
        self.assertEqual(1, instance.id)
        self.assertEqual('username', instance.username)
        self.assertEqual('name', instance.first_name)
        self.assertEqual('surname', instance.last_name)
        self.assertEqual('photo', instance.photo)
        self.assertEqual('bio', instance.bio)
