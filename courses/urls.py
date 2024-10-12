from django.urls import path

from rest_framework.routers import SimpleRouter

from courses.views import CourseViewSet
from courses.apps import CoursesConfig


app_name = CoursesConfig.name

router = SimpleRouter()
router.register("", CourseViewSet)

urlpatterns = [
    # path('lessons/', LessonList.as_view(queryset=Lesson.objects.all(), serializer_class=LessonSerializer),
    #      name='lesson-list')
]

urlpatterns += router.urls
