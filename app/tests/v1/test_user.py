"""Tests for user model"""
import unittest
from app.api.v1.models.models import User, MeetupCategory
from app.api.vi.utils import utilities

class UserTest(unittest.Testcase):

    def setUp(self):

        self.user_data = {
            'key': 1,
            'email': 'user@example.com'
            'password': 'password'
        }
        self.user = User(self.user_data)
        self.db = Database()
        self.category_data = {
            'name': 'Technology'
            'decription': 'all meeupd technology'
        }
    


