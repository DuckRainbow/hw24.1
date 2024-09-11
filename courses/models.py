from django.db import models


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