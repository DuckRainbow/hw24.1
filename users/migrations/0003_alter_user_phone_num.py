# Generated by Django 4.2.2 on 2024-10-15 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_options_remove_user_username_user_avatar_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_num',
            field=models.IntegerField(blank=True, verbose_name='Phone'),
        ),
    ]