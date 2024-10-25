from django.urls import path
from rest_framework.routers import SimpleRouter

from courses.apps import CoursesConfig
from courses.views import (CourseViewSet, LessonCreateAPIView,
                           LessonDestroyAPIView, LessonListAPIView,
                           LessonRetrieveAPIView, LessonUpdateAPIView, SubscriptionListAPIView,
                           SubscriptionRetrieveAPIView, SubscriptionDestroyAPIView)

app_name = CoursesConfig.name

router = SimpleRouter()
router.register('', CourseViewSet)

urlpatterns = [
    path('lessons/', LessonListAPIView.as_view(), name='lessons_list'),
    path('lessons/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lessons_retrieve'),
    path('lessons/create/', LessonCreateAPIView.as_view(), name='lessons_create'),
    path('lessons/<int:pk>/delete/', LessonDestroyAPIView.as_view(), name='lessons_delete'),
    path('lessons/<int:pk>/update/', LessonUpdateAPIView.as_view(), name='lessons_update'),
    path('subscription/', SubscriptionListAPIView.as_view(), name='subscriptions'),
    path('subscription/<int:pk>/', SubscriptionRetrieveAPIView.as_view(), name='subscriptions_retrieve'),
    path('subscription/<int:pk>/update/', LessonListAPIView.as_view(), name='lessons_list'),
    path('subscription/<int:pk>/delete/', SubscriptionDestroyAPIView.as_view(), name='subscriptions_delete'),
]

urlpatterns += router.urls
