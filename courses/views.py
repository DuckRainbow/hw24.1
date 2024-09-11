from django.shortcuts import render

from courses.models import Lesson
from courses.serializers import LessonSerializer
from rest_framework import generics


class LessonList(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer




