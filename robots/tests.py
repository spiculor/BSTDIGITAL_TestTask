from django.test import TestCase, Client
from django.urls import reverse
from robots.models import Robot

class RobotCreateViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('robot-create')

    def test_create_robot_success(self):
        data = {
            "model": "R2",
            "version": "D2",
            "created": "2022-12-31 23:59:59"
        }
        response = self.client.post(self.url, data, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn("robot_id", response.json())
        robot = Robot.objects.get(id=response.json()["robot_id"])
        self.assertEqual(robot.model, "R2")
        self.assertEqual(robot.version, "D2")

    def test_create_robot_missing_fields(self):
        data = {
            "model": "R2"
        }
        response = self.client.post(self.url, data, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json())

    def test_create_robot_invalid_date_format(self):
        data = {
            "model": "R2",
            "version": "D2",
            "created": "invalid-date"
        }
        response = self.client.post(self.url, data, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn("Invalid date format", response.json()["error"])

