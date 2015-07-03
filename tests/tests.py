import unittest
from django.contrib.auth.models import User

try:
    from django.test import Client
except ImportError:
    from django.test.client import Client

class SympaViewTest(unittest.TestCase):

    c = Client()

    def setUp(self):
        for i in range(20):
            user = User(id=i, username=str(i), last_name='My Name %s' % i)
            if i % 2 == 0:
                user.email = 'my-name-%s@unista.fr' % i
            user.save()

    def test_view(self):
        response = self.c.get('/users.sympa')
        self.assertEqual(response.status_code, 200)
        context_users = response.context['users']
        self.assertEqual(
            [u.pk for u in context_users],
            list(range(0, 20, 2))
        )
        self.assertEqual(response.templates[0].name, 'users.sympa')
