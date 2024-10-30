from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Model

from courses.models import Course, Lesson


class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True,
        verbose_name='Email'
    )
    token = models.CharField(
        max_length=100,
        verbose_name='Token',
        blank=True,
        null=True,
    )
    phone_num = models.IntegerField(
        verbose_name='Phone',
        blank=True,
        null=True,
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


class Payment(Model):
    amount = models.PositiveIntegerField(
        verbose_name='сумма оплаты',
        blank=True,
        null=True
    )
    session_id = models.CharField(
        max_length=255,
        verbose_name='Id сессии',
        blank=True,
        null=True,
    )
    link = models.URLField(
        max_length=400,
        verbose_name='Ссылка на оплату',
        blank=True,
        null=True,
    )
    payment_method = models.CharField(
        max_length=255,
        verbose_name='способ оплаты: наличные или перевод на счет.',
        blank=True,
        null=True,
        help_text='Введите способ оплаты (наличные или перевод).'
    )
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

    class Meta:
        verbose_name = 'Оплата'
        verbose_name_plural = 'Оплаты'

    def __str__(self):
        if self.paid_course is None:
            view = 'урок'
            payment = self.paid_lesson
        else:
            view = 'курс'
            payment = self.paid_course
        return f'Пользователь {self.user} оплатил {self.amount} за {view} "{payment}" {self.date_of}'
