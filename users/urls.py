from django.urls import path
from rest_framework.routers import DefaultRouter

from users.apps import UsersConfig
from users.views import (UserCreateAPIView, UserListAPIView, UserUpdateAPIView, UserRetrieveAPIView,
                         UserDestroyAPIView, PaymentListAPIView)

app_name = UsersConfig.name

router = DefaultRouter()

urlpatterns = [
    path('create/', UserCreateAPIView.as_view(), name='user_create'),
    path('', UserListAPIView.as_view(), name='user_list'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='user_update'),
    path('<int:pk>/', UserRetrieveAPIView.as_view(), name='user_retrieve'),
    path('delete/<int:pk>', UserDestroyAPIView.as_view(), name='user_delete'),
    path('payments/', PaymentListAPIView.as_view(), name='payment_list'),
]
