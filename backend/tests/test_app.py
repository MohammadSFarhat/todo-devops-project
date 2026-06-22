import unittest
from app import app

class TestTodoApp(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_health_check(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_get_tasks(self):
        response = self.client.get("/tasks")
        self.assertEqual(response.status_code, 200)

    def test_add_task(self):
        response = self.client.post("/tasks", json={"task": "Write DevOps assignment"})
        self.assertEqual(response.status_code, 201)

    def test_add_task_without_body(self):
        response = self.client.post("/tasks", json={})
        self.assertEqual(response.status_code, 400)

if __name__ == "__main__":
    unittest.main()
``