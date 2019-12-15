from django.contrib.auth.models import User
from django.test import TestCase


class LogInTest(TestCase):
    def test_login_correctSuperuser_runAdmin(self):
        self.credentials = {
            'username': 'sasha',
            'password': 'kirill2000',
            'is_superuser': True,
            'is_staff': True,
        }
        User.objects.create_user(**self.credentials)
        # send login data
        response = self.client.post('/admin/login/?next=/admin/', {'username': 'sasha', 'password': 'kirill2000'},
                                    follow=True)
        # should be logged in now
        self.assertTrue(response.context['user'].is_active)

    def test_login_correctSuperuserWithoutStaffAndSuperuser_NotRunAdmin(self):
        self.credentials = {
            'username': 'sasha',
            'password': 'kirill2000',
            'is_superuser': False,
            'is_staff': False,
        }
        User.objects.create_user(**self.credentials)
        # send login data
        response = self.client.post('/admin/login/?next=/admin/', {'username': 'sasha', 'password': 'kirill2000'},
                                    follow=True)
        # should be logged in now
        self.assertFalse(response.context['user'].is_active)

    def test_login_correctSuperuserWithoutStaff_NotRunAdmin(self):
        self.credentials = {
            'username': 'sasha',
            'password': 'kirill2000',
            'is_superuser': True,
            'is_staff': False,
        }
        # send login data
        response = self.client.post('/admin/login/?next=/admin/', {'username': 'sasha', 'password': 'kirill2000'},
                                    follow=True)
        # should be logged in now
        self.assertFalse(response.context['user'].is_active)

    def test_login_correctSuperuserWithoutSuperuser_NotRunAdmin(self):
        self.credentials = {
            'username': 'sasha',
            'password': 'kirill2000',
            'is_superuser': False,
            'is_staff': True,
        }
        # send login data
        response = self.client.post('/admin/login/?next=/admin/', {'username': 'sasha', 'password': 'kirill2000'},
                                    follow=True)
        # should be logged in now
        self.assertFalse(response.context['user'].is_active)

    def test_login_wrongUsernameSuperuser_NotRunAdmin(self):
        self.credentials = {
            'username': 'sasha',
            'password': 'kirill2000',
            'is_superuser': True,
            'is_staff': True,
        }
        # send login data
        response = self.client.post('/admin/login/?next=/admin/', {'username': 'kirill', 'password': 'kirill2000'},
                                    follow=True)
        # should be logged in now
        self.assertFalse(response.context['user'].is_active)

    def test_login_wrongPasswordSuperuser_NotRunAdmin(self):
        self.credentials = {
            'username': 'sasha',
            'password': 'kirill2000',
            'is_superuser': True,
            'is_staff': True,
        }
        # send login data
        response = self.client.post('/admin/login/?next=/admin/', {'username': 'sasha', 'password': '2000'},
                                    follow=True)
        # should be logged in now
        self.assertFalse(response.context['user'].is_active)

    def test_login_wrongPasswordAndUsernameSuperuser_NotRunAdmin(self):
        self.credentials = {
            'username': 'sasha',
            'password': 'kirill2000',
            'is_superuser': True,
            'is_staff': True,
        }
        # send login data
        response = self.client.post('/admin/login/?next=/admin/', {'username': 'kirill', 'password': '2000'},
                                    follow=True)
        # should be logged in now
        self.assertFalse(response.context['user'].is_active)
