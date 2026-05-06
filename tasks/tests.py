from django.test import TestCase, Client
from django.urls import reverse
from .models import Task


class TaskModelTest(TestCase):
    def test_create_task(self):
        task = Task.objects.create(title='Test task')
        self.assertEqual(task.title, 'Test task')
        self.assertFalse(task.completed)
        self.assertEqual(str(task), 'Test task')

    def test_task_default_not_completed(self):
        task = Task.objects.create(title='Another task')
        self.assertFalse(task.completed)

    def test_task_ordering(self):
        task1 = Task.objects.create(title='First')
        task2 = Task.objects.create(title='Second')
        tasks = list(Task.objects.all())
        # Most recently created appears first (-created_at ordering)
        self.assertEqual(tasks[0], task2)
        self.assertEqual(tasks[1], task1)


class TaskViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.task = Task.objects.create(title='Sample task', description='A description')

    def test_task_list_view(self):
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Sample task')

    def test_task_create_get(self):
        response = self.client.get(reverse('task_create'))
        self.assertEqual(response.status_code, 200)

    def test_task_create_post(self):
        response = self.client.post(reverse('task_create'), {'title': 'New task', 'description': ''})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Task.objects.filter(title='New task').exists())

    def test_task_create_invalid(self):
        response = self.client.post(reverse('task_create'), {'title': ''})
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Task.objects.filter(title='').exists())

    def test_task_update_get(self):
        response = self.client.get(reverse('task_update', args=[self.task.pk]))
        self.assertEqual(response.status_code, 200)

    def test_task_update_post(self):
        response = self.client.post(
            reverse('task_update', args=[self.task.pk]),
            {'title': 'Updated task', 'description': 'Updated desc'}
        )
        self.assertEqual(response.status_code, 302)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, 'Updated task')

    def test_task_toggle(self):
        self.assertFalse(self.task.completed)
        response = self.client.post(reverse('task_toggle', args=[self.task.pk]))
        self.assertEqual(response.status_code, 302)
        self.task.refresh_from_db()
        self.assertTrue(self.task.completed)

        # Toggle back
        self.client.post(reverse('task_toggle', args=[self.task.pk]))
        self.task.refresh_from_db()
        self.assertFalse(self.task.completed)

    def test_task_delete_get(self):
        response = self.client.get(reverse('task_delete', args=[self.task.pk]))
        self.assertEqual(response.status_code, 200)

    def test_task_delete_post(self):
        response = self.client.post(reverse('task_delete', args=[self.task.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Task.objects.filter(pk=self.task.pk).exists())

    def test_task_not_found(self):
        response = self.client.get(reverse('task_update', args=[9999]))
        self.assertEqual(response.status_code, 404)
