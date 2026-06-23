import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

class TestIntegration(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        app.testing = True

    def test_full_task_workflow(self):
        # Add a task
        response = self.client.post(
            '/tasks',
            json={"task": "Integration test task"}
        )
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        task_id = data['task']['id']

        # Get all tasks and verify it exists
        response = self.client.get('/tasks')
        self.assertEqual(response.status_code, 200)
        tasks = response.get_json()
        self.assertTrue(any(t['id'] == task_id for t in tasks))

        # Mark as done
        response = self.client.put(f'/tasks/{task_id}/done')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.get_json()['task']['done'])

        # Delete it
        response = self.client.delete(f'/tasks/{task_id}')
        self.assertEqual(response.status_code, 200)

    def test_add_and_verify_multiple_tasks(self):
        response1 = self.client.post('/tasks', json={"task": "Task A"})
        response2 = self.client.post('/tasks', json={"task": "Task B"})
        self.assertEqual(response1.status_code, 201)
        self.assertEqual(response2.status_code, 201)

        response = self.client.get('/tasks')
        tasks = response.get_json()
        self.assertGreaterEqual(len(tasks), 2)

    def test_delete_nonexistent_task(self):
        response = self.client.delete('/tasks/99999')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()