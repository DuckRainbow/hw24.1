from django.urls import path

from courses.apps import CoursesConfig
from courses.models import Lesson
from courses.serializers import LessonSerializer
from courses.views import LessonList

app_name = CoursesConfig.name

urlpatterns = [
    path('lessons/', LessonList.as_view(queryset=Lesson.objects.all(), serializer_class=LessonSerializer),
         name='lesson-list')
]
