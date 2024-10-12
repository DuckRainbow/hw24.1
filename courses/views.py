from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from courses.models import Lesson, Course
from courses.serializers import CourseSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class LessonList(generics.ListCreateAPIView):
    pass
    # queryset = Lesson.objects.all()
    # serializer_class = LessonSerializer
