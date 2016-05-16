# coding: utf-8


class User(object):

    def __init__(self, id, username, first_name, last_name, photo, bio):
        self.id = id
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.photo = photo
        self.bio = bio
