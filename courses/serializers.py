from rest_framework.serializers import ModelSerializer

from courses.models import Lesson, Course


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ['title', 'preview', 'description']


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['title', 'preview', 'description', 'video_link', 'course']
