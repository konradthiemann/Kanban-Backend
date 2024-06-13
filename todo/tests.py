from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework.settings import api_settings
from rest_framework_simplejwt.tokens import AccessToken
from .models import Todo, Category
import jwt

class TodoTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.category = Category.objects.create(name='Work', description='Work-related tasks')
        self.todo = Todo.objects.create(
            title='Test Todo',
            description='This is a test todo',
            due_date=1718082165,
            urgency='medium',
            status='todo',
            category=self.category,
            author=self.user
        )
        self.todo.assigned_to.set([self.user])
        self.client = APIClient()
    
    def _get_access_token(self, user):
        access_token = AccessToken.for_user(user)
        return str(access_token)
    
    # def _get_jwt_token(self, user):
    #     payload = {
    #         'username': user.username,
    #         'email': user.email,
    #     }
    #     jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    #     jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
    #     payload = jwt_payload_handler(user)
    #     token = jwt_encode_handler(payload)
    #     return token

    def test_todo_creation(self):
        token = self._get_access_token(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

        response = self.client.post('/todos/', {
            'title': 'New Todo',
            'description': 'New Todo Description',
            'due_date': 1718082165,
            'urgency': 'high',
            'status': 'in_progress',
            'category': self.category.id,
            'assigned_to': [self.user.id]
        }, format='json')
        print(response.data)
        self.assertEqual(response.status_code, 201)

    def test_get_todos(self):
        token = self._get_access_token(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

        response = self.client.get('/todos/')
        
        print(response.data)
        self.assertEqual(response.status_code, 200)

    # def test_create_todo(self):
    #     self.client.login(username='testuser', password='12345')
    #     response = self.client.post('/todos/', {
    #         'title': 'New Todo',
    #         'description': 'New Todo Description',
    #         'due_date': '2024-07-01T00:00:00Z',
    #         'urgency': 'high',
    #         'status': 'in_progress',
    #         'category': self.category.id,
    #         'assigned_to': [self.user.id]
    #     }, content_type='application/json')
    #     self.assertEqual(response.status_code, 201)
