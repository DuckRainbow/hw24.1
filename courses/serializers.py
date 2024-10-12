from rest_framework import serializers

from courses.models import Lesson, Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['title', 'preview', 'description']
