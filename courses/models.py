from django.db import models

from config import settings


class Course(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name="Название курса",
        blank=True,
        null=True,
        help_text='Введите название курса.'
    )
    preview = models.ImageField(
        verbose_name='превью',
        blank=True,
        null=True,
    )
    description = models.CharField(
        max_length=100,
        verbose_name="Описание курса",
        blank=True,
        null=True,
        help_text='Введите описание курса.'
    )
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Создатель',
    )


class Lesson(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name="Название урока",
        blank=True,
        null=True,
        help_text='Введите название урока.'
    )
    description = models.CharField(
        max_length=100,
        verbose_name="Описание урока",
        blank=True,
        null=True,
        help_text='Введите описание урока.'
    )

    preview = models.ImageField(
        verbose_name='превью',
        blank=True,
        null=True,
    )
    video_link = models.URLField(
        verbose_name='Ссылка на видео',
    )
    course = models.ForeignKey(
        Course,
        verbose_name='Курс',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Создатель',
    )


class Subscription(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Пользователь',
    )
    course = models.ForeignKey(
        Course,
        verbose_name='Курс',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return f"Пользователь {self.user}, подписан на курс: {self.course}"

    class Meta:
        db_table = "subscription"
        verbose_name = "Подписка"
        verbose_name_plural = "Подиписки"
        ordering = ("user",)