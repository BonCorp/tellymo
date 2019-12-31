from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user(email='tst@tellymo.com', username='test', password='testpass'):
    """Create sample user"""
    return get_user_model().objects.create_user(email, username, password)


class ModelTestCase(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@test.com'
        username = 'test'
        password = 'password'
        user = get_user_model().objects.create_user(
            email=email,
            username=username,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertEqual(user.username, username)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'test@Test.com'
        username = 'test'
        user = get_user_model().objects.create_user(email, username, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invlaid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test', 'test123')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'superuser@test.com', 'superuser', 'password')

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """Test the string representation"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Adventure'
        )
        self.assertEqual(str(tag), tag.name)

    def test_rating_int(self):
        """Test the integer representation"""
        rating = models.Rating.objects.create(
            user=sample_user(),
            rtng=5
        )
        self.assertEqual(int(rating), rating.rtng)
