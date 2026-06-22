import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_get_tasks(self):
        response = self.client.get('/tasks')
        self.assertEqual(response.status_code, 200)

    def test_add_task(self):
        response = self.client.post('/tasks', json={"task": "Test"})
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()