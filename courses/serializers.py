from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from courses.models import Course, Lesson


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class CourseDetailSerializer(ModelSerializer):
    lessons_count = SerializerMethodField()

    def get_lessons_count(self, obj):
        return Lesson.objects.filter(course=self)

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'lessons_count']


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'title', 'preview', 'description', 'video_link', 'course']
