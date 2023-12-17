"""Tests"""
from django.test import TestCase
from .models import User  # Import your User model


class UserFollowingFollowersTestCase(TestCase):
    def setUp(self):
        """Create users"""

        self.user1 = User.objects.create(username='user1')
        self.user2 = User.objects.create(username='user2')
        self.user3 = User.objects.create(username='user3')

        self.user1.following_set.add(self.user2, self.user3)
        self.user2.following_set.add(self.user1)
        self.user3.following_set.add(self.user1)

        self.user2.followers_set.add(self.user1)
        self.user3.followers_set.add(self.user1)
        self.user1.followers_set.add(self.user2, self.user3)

    def test_user_following(self):
        """Test that user1 is following user2 and user3"""
        self.assertIn(self.user2, self.user1.following_set.all())
        self.assertIn(self.user3, self.user1.following_set.all())

    def test_user_followers(self):
        """Test that user2 and user3 are followers of user1"""
        self.assertIn(self.user1, self.user2.followers_set.all())
        self.assertIn(self.user1, self.user3.followers_set.all())
        self.assertIn(self.user2, self.user1.followers_set.all())
        self.assertIn(self.user3, self.user1.followers_set.all())
