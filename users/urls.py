from django.urls import path
from rest_framework.routers import DefaultRouter

from users.apps import UsersConfig
from users.views import (UserCreateAPIView, UserListAPIView, UserUpdateAPIView, UserRetrieveAPIView,
                         UserDestroyAPIView, PaymentListAPIView)

app_name = UsersConfig.name

router = DefaultRouter()

urlpatterns = [
    path('users/create/', UserCreateAPIView.as_view(), name='user_create'),
    path('users/', UserListAPIView.as_view(), name='user_list'),
    path('users/update/<int:pk>/', UserUpdateAPIView.as_view(), name='user_update'),
    path('users/<int:pk>/', UserRetrieveAPIView.as_view(), name='user_retrieve'),
    path('users/delete/<int:pk>', UserDestroyAPIView.as_view(), name='user_delete'),
    path('users/payments/', PaymentListAPIView.as_view(), name='payment_list'),
]
