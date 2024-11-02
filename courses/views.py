from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView, get_object_or_404)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from courses.models import Course, Lesson, Subscription
from courses.paginators import PagePagination
from courses.serializers import CourseSerializer, LessonSerializer, CourseDetailSerializer, LessonListSerializer, \
    SubscriptionSerializer
from users.permissions import IsModerator, IsCreator
from courses.tasks import updating_mail


class CourseViewSet(ModelViewSet):
    """Класс для просмотра, обновления и удаления курсов"""
    pagination_class = PagePagination

    def get_serializer_class(self):
        """Метод для выбора сериализатора"""
        if self.action == 'retrieve':
            return CourseDetailSerializer
        return CourseSerializer

    def get(self, request):
        queryset = Course.objects.all()
        paginated_queryset = self.paginate_queryset(queryset)
        serializer = self.get_serializer_class(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)

    def perform_create(self, serializer):
        course = serializer.save()
        course.creator = self.request.user
        course.save()

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = (~IsModerator,)
        elif self.action in ['update', 'retrieve']:
            self.permission_classes = (IsModerator | IsCreator,)
        elif self.action == 'destroy':
            self.permission_classes = (IsCreator | ~IsModerator,)
        return super().get_permissions()

    def perform_update(self, serializer):
        """Метод фиксирует обновления курсов"""
        course = serializer.save()
        updating_mail.delay(course.id)
        course.save()


class LessonCreateAPIView(CreateAPIView):
    """Класс для создания урока"""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (~IsModerator, IsAuthenticated)

    def perform_create(self, serializer):
        lesson = serializer.save()
        lesson.creator = self.request.user
        lesson.save()


class LessonListAPIView(ListAPIView):
    """Класс для просмотра списка уроков"""
    pagination_class = PagePagination

    def get(self, request):
        queryset = Lesson.objects.all()
        paginated_queryset = self.paginate_queryset(queryset)
        serializer = LessonListSerializer(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)


class LessonRetrieveAPIView(RetrieveAPIView):
    """Класс для просмотра урока"""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsModerator | IsCreator, IsAuthenticated)


class LessonUpdateAPIView(UpdateAPIView):
    """Класс для обновления урока"""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsModerator | IsCreator, IsAuthenticated)


class LessonDestroyAPIView(DestroyAPIView):
    """Класс для удаления урока"""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsCreator, IsAuthenticated | ~IsModerator)


class SubscriptionCreateAPIView(CreateAPIView):
    """Класс для создания подписки"""
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

    def post(self, *args, **kwargs):
        """Метод для добавления/удаления подписки пользователю"""
        user = self.request.user
        course_id = self.request.data.get('course')
        course_item = get_object_or_404(Course, pk=course_id)
        subs_item = Subscription.objects.filter(user=user, course=course_item)

        # Если подписка у пользователя на этот курс есть - удаляем ее
        if subs_item.exists():
            subs_item.delete()
            message = "Подписка удалена"
        # Если подписки у пользователя на этот курс нет - создаем ее
        else:
            Subscription.objects.create(user=user, course=course_item)
            message = "Подписка добавлена"
        return Response({"message": message})


class SubscriptionListAPIView(ListAPIView):
    """Класс для просмотра списка подписок"""
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer


class SubscriptionRetrieveAPIView(RetrieveAPIView):
    """Класс для просмотра подписки"""
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer


class SubscriptionUpdateAPIView(UpdateAPIView):
    """Класс для обновления подписки"""
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

    def post(self, *args, **kwargs):
        """Метод для добавления/удаления подписки пользователю"""
        user = self.request.user
        course_id = self.request.data.get('course')
        course_item = get_object_or_404(Course, pk=course_id)
        subs_item = Subscription.objects.filter(user=user, course=course_item)

        # Если подписка у пользователя на этот курс есть - удаляем ее
        if subs_item.exists():
            subs_item.delete()
            message = "Подписка удалена"
        # Если подписки у пользователя на этот курс нет - создаем ее
        else:
            Subscription.objects.create(user=user, course=course_item)
            message = "Подписка добавлена"
        return Response({"message": message})


class SubscriptionDestroyAPIView(DestroyAPIView):
    """Класс для удаления подписки"""
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
