
import requests

from django.test import TransactionTestCase, Client
from django.contrib.auth.models import User

from action.models import ActionManagement


class ViewTestCase(TransactionTestCase):
    def setUp(self):
        self.user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        self.client = Client()
    
    def test_create(self):
        url="http://127.0.0.1:8000/create/"
        response = self.client.post(url, {"title":"test",
                               "description":"description_test",
                               "date":"2016-04-29",
                               "assigned_user":self.user.id,
                               })
        actions = ActionManagement.objects.all().first()
        self.assertEqual(actions.title, "test")
        self.assertEqual(actions.description, "description_test")
        self.assertEqual(actions.assigned_user.id, self.user.id)
