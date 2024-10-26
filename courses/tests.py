from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from courses.models import Course, Lesson, Subscription
from users.models import User


class LessonsTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='admin@sky.pro')
        self.course = Course.objects.create(title='Тестовый курс')
        self.lesson = Lesson.objects.create(
            title='Тестовый урок',
            video_link='https://www.youtube.com/q',
            creator=self.user,
        )
        self.client.force_authenticate(user=self.user)

    def test_lesson_create(self):
        url = reverse('courses:lessons_create')
        data = {
            'title': 'Тестовый урок 2',
            'video_link': 'https://www.youtube.com/qw',
            'course': self.course.pk,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_lesson_list(self):
        url = reverse('courses:lessons_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()['results']), 1)

    def test_lesson_retrieve(self):
        url = reverse('courses:lessons_retrieve', args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('title'), self.lesson.title)
        self.assertEqual(data.get('course'), self.lesson.course)

    def test_lesson_update(self):
        url = reverse('courses:lessons_update', args=(self.lesson.pk,))
        data = {'title': 'Тестовый урок 3'}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            Lesson.objects.get(pk=self.lesson.pk).title, 'Тестовый урок 3'
        )

    def test_lesson_delete(self):
        url = reverse('courses:lessons_delete', args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)


class SubscriptionsTestCase(APITestCase):

    def setUp(self):
        # Подготовка данных перед каждым тестом
        self.user = User.objects.create(email='admin@sky.pro')
        self.course = Course.objects.create(
            title='Тестовая подписка',
        )
        self.client.force_authenticate(user=self.user)
        self.url = reverse("courses:subscriptions_create")

    def test_subscription_create(self):
        data = {"user": self.user.pk, "course": self.course.pk}
        response = self.client.post(self.url, data)
        temp_data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(temp_data.get("message"), "Подписка добавлена")
        self.assertEqual(Subscription.objects.all().count(), 1)

    def test_subscribe_delete(self):
        Subscription.objects.create(user=self.user, course=self.course)
        data = {
            "user": self.user.id,
            "course": self.course.id,
        }
        response = self.client.post(self.url, data=data)
        temp_data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(temp_data.get("message"), "Подписка удалена")
        self.assertEqual(Subscription.objects.all().count(), 0)