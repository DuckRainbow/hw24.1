from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Model

from courses.models import Course, Lesson


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')
    token = models.CharField(
        max_length=100,
        verbose_name='Token',
        blank=True,
        null=True,
    )
    phone_num = models.IntegerField(
        verbose_name='Phone',
        blank=True
    )
    avatar = models.ImageField(
        verbose_name='Avatar',
        blank=True,
        null=True,
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        permissions = [
            ('can_block_user', 'Can block user')
        ]

    def __str__(self):
        return self.email


class Payments(Model):
    user = models.ForeignKey(
        User,
        verbose_name='пользователь',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    date_of = models.DateTimeField(
        verbose_name="Дата оплаты",
        blank=True,
        null=True
    )
    paid_course = models.ForeignKey(
        Course,
        verbose_name='оплаченный курс',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    paid_lesson = models.ForeignKey(
        Lesson,
        verbose_name='оплаченный урок',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    summ_of = models.IntegerField(
        verbose_name='сумма оплаты',
        blank=True,
        null=True
    )
    payment_method = models.CharField(
        max_length=255,
        verbose_name='способ оплаты: наличные или перевод на счет.',
        blank=True,
        null=True
    )
