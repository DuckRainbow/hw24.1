from datetime import timezone

from celery import shared_task

from users.models import User


@shared_task
def block_users():
    """Меняет статус is_active на False, если пользователь не заходил более месяца"""
    thirty_days_ago = timezone.now() - timezone.timedelta(days=30)
    users_to_block = User.objects.filter(
        is_active=True, last_login__lt=thirty_days_ago
    ).exclude(is_superuser=True)
    users = []
    for user in users_to_block:
        user.is_active = False
        user.save()
        users.append(user)
    return f"Заблокированы пользователи: {users}"
