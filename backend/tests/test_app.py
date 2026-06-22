import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

class TestTodoApp(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        app.testing = True

    def test_health_check(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_get_tasks_empty(self):
        response = self.client.get('/tasks')
        self.assertEqual(response.status_code, 200)

    def test_add_task(self):
        response = self.client.post(
            '/tasks',
            json={"task": "Buy groceries"}
        )
        self.assertEqual(response.status_code, 201)

    def test_add_task_missing_field(self):
        response = self.client.post(
            '/tasks',
            json={}
        )
        self.assertEqual(response.status_code, 400)

    def test_delete_task(self):
        self.client.post('/tasks', json={"task": "Task to delete"})
        response = self.client.delete('/tasks/0')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()