from django.test import TestCase
from django.contrib.auth.models import User
from .models import Todo, Category

class TodoTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.category = Category.objects.create(name='Work')
        self.todo = Todo.objects.create(
            title='Test Todo',
            description='This is a test todo',
            due_date='2024-06-30T00:00:00Z',
            urgency='medium',
            status='todo',
            category=self.category,
            author=self.user
        )
        self.todo.assigned_to.set([self.user])

    def test_todo_creation(self):
        self.assertEqual(self.todo.title, 'Test Todo')
        self.assertEqual(self.todo.description, 'This is a test todo')
        self.assertEqual(self.todo.urgency, 'medium')
        self.assertEqual(self.todo.status, 'todo')
        self.assertEqual(self.todo.category.name, 'Work')
        self.assertEqual(self.todo.author.username, 'testuser')
        self.assertEqual(list(self.todo.assigned_to.all()), [self.user])

    def test_get_todos(self):
        response = self.client.get('/todos/')
        self.assertEqual(response.status_code, 200)

    def test_create_todo(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post('/todos/', {
            'title': 'New Todo',
            'description': 'New Todo Description',
            'due_date': '2024-07-01T00:00:00Z',
            'urgency': 'high',
            'status': 'in_progress',
            'category': self.category.id,
            'assigned_to': [self.user.id]
        }, content_type='application/json')
        self.assertEqual(response.status_code, 201)
